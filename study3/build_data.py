"""
Study 3 data: 350 charts = the 300 follow-up charts (texts unchanged, relabeled under the study-3 rules)
+ 50 new hard cases. Writes study3/data/charts.jsonl, labels.csv and charts/*.txt. See study3/SPEC.md.

Study-3 label rules (agreed with the study lead, 2026-10-27):
  - pilot rule + R1 (face-to-face, MD/DO/NP/PA) + R2 (signed with credentials) + R3 (secondary diabetes is not type 2);
  - "addressed" follows the MEAT reading: a copied plan line with "continue regimen" or "stable" counts, and so does
    CKD named in a reviewed list of chronic conditions or problems (B2, B4, G4, A_N1b become label 1);
  - "see nephrology note" alone is not addressed; a medication change made because of kidney function is;
  - diabetes plus another cause counts as a diabetic cause;
  - new cases: the current assessment and plan governs when sections conflict; a documented stage counts even when
    the labs disagree; ESRD on dialysis supports E11.22; "CKD?" is not established; "DM with renal involvement"
    without CKD is not CKD.

Hard cases are built with the follow-up generator (unchanged) from a base scenario, then edited with recorded
string replacements and inserts; format noise is applied after the edits so evidence stays exact.

Run:  python study3/build_data.py
"""

import collections
import csv
import datetime as dt
import hashlib
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "followup"))
sys.path.insert(0, ROOT)
import generate_charts_v3 as v3  # noqa: E402  (not modified)
import generate_charts as v2     # noqa: E402  (not modified)

SEED = 20261028
YES, NO, ND = "yes", "no", "not_documented"
QIDS = ["G1", "G2", "R1", "R2", "Q1", "Q2", "Q3", "Q4"]
RELABEL_ADDRESSED = {"B2_copy_stale", "B4_per_last_visit", "G4_list_entry", "A_N1b_laundry_list"}

# hard scenario -> (description, count, label, base scenario, dev count)
HARD = {
    "H1a_conflict_hpi_no_kidney":   ("HPI says no kidney disease; the plan addresses established CKD", 4, 1, "A_P1_stage_and_link", 2),
    "H1b_conflict_stage":           ("Problem list says stage 4; the plan says stage 3a", 3, 1, "A_P2_with_convention", 2),
    "H1c_conflict_dm_type":         ("Outside records say type 1; problem list and plan say type 2", 3, 1, "A_P2_with_convention", 1),
    "H1d_conflict_plan_possible":   ("Problem list says CKD stage 3a; the plan says possible CKD, recheck", 3, 0, "A_N5_uncertain_dx", 2),
    "H2a_stage_3a_labs_stage4":     ("CKD stage 3a documented; eGFR in the stage-4 range", 6, 1, "A_P2_with_convention", 3),
    "H2b_stage_4_labs_stage3":      ("CKD stage 4 documented; eGFR in the stage-3 range", 6, 1, "A_P1_stage_and_link", 3),
    "H3a_esrd_dialysis_addressed":  ("ESRD on hemodialysis, addressed in the plan", 6, 1, "A_P1_stage_and_link", 3),
    "H3b_esrd_problem_list_only":   ("ESRD on hemodialysis on the problem list only", 3, 0, "A_N1a_problem_list_only", 1),
    "H3c_ckd5_not_on_dialysis":     ("CKD stage 5 not on dialysis, conservative care, addressed", 3, 1, "A_P1_stage_and_link", 2),
    "H4a_ckd_question_mark":        ("'CKD?' in the plan with labs to be checked", 4, 0, "A_N5_uncertain_dx", 2),
    "H4b_kidneys_ok":               ("'Kidneys OK per last labs' with low eGFR and no CKD diagnosis", 3, 0, "A_N3_labs_only", 1),
    "H4c_renal_involvement":        ("'DM with renal involvement' without a CKD diagnosis", 3, 0, "A_N3_labs_only", 2),
    "H4d_truncated_plan":           ("CKD plan line cut off mid-sentence, still giving today's status", 3, 1, "A_P1_stage_and_link", 1),
}
assert sum(v[1] for v in HARD.values()) == 50 and sum(v[4] for v in HARD.values()) == 25


def rules_answers(c):
    f = c["facts"]
    return {"R1": YES if f["encounter"] == "f2f" and f["provider_type"] in {"MD", "DO", "NP", "PA"} else NO,
            "R2": YES if f["signature"] == "full" else NO}


def rules_evidence(text):
    ev = {}
    m = re.search(r"Date of service:[^\n]*", text)
    k = re.search(r"Clinician:[^\n]*", text)
    ev["R1"] = [x.group(0) for x in (m, k) if x]
    s = re.findall(r"Electronically signed:[^\n]*|\*\*\* NOTE NOT SIGNED[^\n]*", text)
    ev["R2"] = s[-1:] if s else []
    return ev


def study3_label(a):
    """The study-3 label from intended answers (all hard-case rules are expressed through the answers)."""
    return int(a["G1"] == YES and a["G2"] == YES and a["R1"] == YES and a["R2"] == YES
               and a["Q3"] != NO and a["Q4"] == YES)

# --------------------------------------------------------------------------- existing 300


def relabel(c):
    c = json.loads(json.dumps(c))
    a = c["intended_answers"]
    if c["scenario"] in RELABEL_ADDRESSED:
        a["Q4"] = YES
        c["ambiguous_fields"] = [q for q in c["ambiguous_fields"] if q != "Q4"]
    a.update(rules_answers(c))
    c["intended_answers"] = {q: a[q] for q in QIDS}
    c["flags"] = [f for f in c["flags"] if f != "label_needs_review"]
    ev = c.get("evidence", {})
    ev.update({q: v for q, v in rules_evidence(c["text"]).items() if v})
    c["evidence"] = ev
    old = c["label"]
    c["label"] = study3_label(c["intended_answers"])
    if c["family"] != "F":
        expected = 1 if c["scenario"] in RELABEL_ADDRESSED else old
        assert c["label"] == expected, (c["chart_id"], c["scenario"], c["label"])
    else:
        assert c["label"] == 0
    c["study3_relabeled"] = c["label"] != old
    c["source"] = "followup"
    return c

# --------------------------------------------------------------------------- hard cases


def build_clean(rng, idx, base, patch=None, egfr=None, stage_text=None):
    """Build a base chart with the follow-up generator, without format noise, with optional fact patches."""
    orig_sp, orig_noise = v3.scenario_params, v3.apply_noise
    saved_r, saved_t = dict(v3.EGFR_RANGE), dict(v3.STAGE_TEXT)
    try:
        def sp(s, r):
            p = orig_sp(s, r)
            p.update(patch or {})
            return p
        v3.scenario_params = sp
        v3.apply_noise = lambda t, e, r, cid, visit: (t, e)
        if egfr:
            v3.EGFR_RANGE.update(egfr)
        if stage_text:
            v3.STAGE_TEXT.update(stage_text)
        c = v3.build_chart(rng, idx, base)
    finally:
        v3.scenario_params, v3.apply_noise = orig_sp, orig_noise
        v3.EGFR_RANGE.clear(); v3.EGFR_RANGE.update(saved_r)
        v3.STAGE_TEXT.clear(); v3.STAGE_TEXT.update(saved_t)
    return c


def edit(c, pairs):
    """Replace text in the note and in every evidence string; each `old` must occur in the note."""
    for old, new in pairs:
        assert old in c["text"], (c["chart_id"], old)
        c["text"] = c["text"].replace(old, new)
        c["evidence"] = {q: [s.replace(old, new) for s in v] for q, v in c["evidence"].items()}


def plan_line(c):
    return c["evidence"]["Q4"][0]


def hpi_insert(c, sentence):
    head = "HISTORY OF PRESENT ILLNESS\n"
    i = c["text"].index(head) + len(head)
    first_stop = c["text"].index(". ", i) + 2
    c["text"] = c["text"][:first_stop] + sentence + " " + c["text"][first_stop:]


def ap_insert(c, item):
    """Add an item as the second line of the assessment and plan (renumbering is not needed for meaning)."""
    m = re.search(r"\n(ASSESSMENT AND PLAN|ASSESSMENT/PLAN|IMPRESSION AND PLAN)\n(?:\([^\n]*\)\n)?1\. [^\n]*\n", c["text"])
    c["text"] = c["text"][:m.end()] + "1b. " + item + "\n" + c["text"][m.end():]


def pl_insert(c, line):
    m = re.search(r"PAST MEDICAL HISTORY / PROBLEM LIST\n", c["text"])
    c["text"] = c["text"][:m.end()] + "- " + line + "\n" + c["text"][m.end():]


def build_hard(rng, idx, s):
    desc, _, label, base, _ = HARD[s]
    sex_pro = None
    a_over, amb = {}, []
    if s == "H1a_conflict_hpi_no_kidney":
        c = build_clean(rng, idx, base)
        hpi_insert(c, "No history of kidney disease.")
        amb = ["G2"]
    elif s == "H1b_conflict_stage":
        c = build_clean(rng, idx, base, patch={"stage": "3a", "prior_section": False})
        pl = re.search(r"PAST MEDICAL HISTORY / PROBLEM LIST\n(?:- [^\n]*\n)*?- ([^\n]*stage 3a[^\n]*)\n", c["text"]).group(1)
        new = pl.replace("stage 3a", "stage 4")
        c["text"] = c["text"].replace("- " + pl + "\n", "- " + new + "\n", 1)
        c["evidence"] = {q: [new if x == pl else x for x in v] for q, v in c["evidence"].items()}
        amb = ["Q1"]
    elif s == "H1c_conflict_dm_type":
        c = build_clean(rng, idx, base)
        hpi_insert(c, "Outside records from 2015 list type 1 diabetes.")
        amb = ["G1"]
    elif s == "H1d_conflict_plan_possible":
        c = build_clean(rng, idx, base)
        pl_insert(c, "Chronic kidney disease stage 3a")
        c["evidence"].setdefault("Q1", []).append("Chronic kidney disease stage 3a")
        a_over = {"Q1": YES}
        amb = ["G2"]
    elif s == "H2a_stage_3a_labs_stage4":
        c = build_clean(rng, idx, base, patch={"stage": "3a"}, egfr={"3a": (20, 28)})
        amb = ["Q1"]
    elif s == "H2b_stage_4_labs_stage3":
        c = build_clean(rng, idx, base, patch={"stage": "4"}, egfr={"4": (50, 58)})
        amb = ["Q1"]
    elif s in {"H3a_esrd_dialysis_addressed", "H3c_ckd5_not_on_dialysis"}:
        c = build_clean(rng, idx, base, patch={"stage": "5"}, egfr={"5": (6, 12)}, stage_text={"5": "stage 5"})
        old_plan = plan_line(c)
        latest = c["facts"]["egfr_series"][-1][1]
        if s.startswith("H3a"):
            new_plan = (f"End-stage renal disease on hemodialysis Monday, Wednesday and Friday via nephrology; eGFR {latest}, "
                        "dry weight stable, potassium acceptable. Continue sevelamer; dialysis per nephrology.")
            stage_new = "stage 5 (ESRD), on hemodialysis"
        else:
            new_plan = (f"eGFR {latest}, stage 5 not on dialysis; conservative management chosen after shared decision-making. "
                        "Renal diet reviewed; nephrology follow-up in 1 month.")
            stage_new = "stage 5, not on dialysis"
        pairs = [(old_plan, new_plan), ("stage 5", stage_new)]
        for med in ("metformin 1000 mg twice daily", "metformin 500 mg twice daily (renally dosed)"):
            if med in c["text"]:
                pairs.append((med, "insulin glargine 12 units nightly"))
        for sg in ("empagliflozin 10 mg daily", "dapagliflozin 10 mg daily"):
            if sg in c["text"]:
                pairs.append((sg, "sevelamer 800 mg with meals"))
        edit(c, pairs)
    elif s == "H3b_esrd_problem_list_only":
        c = build_clean(rng, idx, base, patch={"stage": "5", "staged": True, "prior_section": False},
                        egfr={"5": (6, 12)}, stage_text={"5": "stage 5"})
        pairs = [("stage 5", "stage 5 (ESRD), on hemodialysis")]
        for med in ("metformin 1000 mg twice daily", "metformin 500 mg twice daily (renally dosed)"):
            if med in c["text"]:
                pairs.append((med, "insulin glargine 12 units nightly"))
        edit(c, pairs)
    elif s == "H4a_ckd_question_mark":
        c = build_clean(rng, idx, base)
        head = next(h for h in v2.POSSIBLE_CKD if h + ":" in c["text"])
        edit(c, [(head + ":", "CKD?:")])
        c["evidence"]["G2"] = ["CKD?"]
        amb = ["G2"]
    elif s == "H4b_kidneys_ok":
        c = build_clean(rng, idx, base, patch={"prior_section": False})
        ap_insert(c, "Kidneys OK per last labs.")
        amb = ["G2"]
    elif s == "H4c_renal_involvement":
        c = build_clean(rng, idx, base, patch={"prior_section": False})
        latest = c["facts"]["egfr_series"][-1][1]
        ap_insert(c, f"DM w/ renal involvement: eGFR {latest}, continue current medications.")
        amb = ["G2"]
    elif s == "H4d_truncated_plan":
        c = build_clean(rng, idx, base)
        old_plan = plan_line(c)
        first = old_plan.split(". ")[0] + "."
        cut = first + " Continue"
        edit(c, [(old_plan, cut)])
    else:
        raise KeyError(s)

    a = dict(c["intended_answers"])
    a.update(rules_answers(c))
    a.update(a_over)
    if s in {"H1a_conflict_hpi_no_kidney", "H1b_conflict_stage", "H1c_conflict_dm_type", "H2a_stage_3a_labs_stage4",
             "H2b_stage_4_labs_stage3", "H3a_esrd_dialysis_addressed", "H3c_ckd5_not_on_dialysis", "H4d_truncated_plan"}:
        assert a["Q4"] == YES and a["G2"] == YES
    c["intended_answers"] = {q: a[q] for q in QIDS}
    c["evidence"].update({q: v for q, v in rules_evidence(c["text"]).items() if v})
    c["label"] = study3_label(c["intended_answers"])
    assert c["label"] == label, (idx, s, c["intended_answers"])
    c.update(chart_id=f"S3-{idx:04d}", scenario=s, family="H", scenario_description=desc, source="study3_hard",
             study3_relabeled=False)
    c["text"] = c["text"].replace(f"FU-{idx:04d}", f"S3-{idx:04d}")
    c["evidence"] = {q: [x.replace(f"FU-{idx:04d}", f"S3-{idx:04d}") for x in v] for q, v in c["evidence"].items()}
    c["ambiguous_fields"] = sorted(set(c["ambiguous_fields"]) | set(amb))
    c["flags"] = sorted(set(f for f in c["flags"] if f != "format_stress") | {"hard_case"})
    if rng.random() < 0.5:   # format noise after the edits, so evidence stays exact
        visit = dt.date.fromisoformat(c["facts"]["visit_date"])
        c["text"], c["evidence"] = v3.apply_noise(c["text"], {q: list(v) for q, v in c["evidence"].items()}, rng, c["chart_id"], visit)
        c["evidence"] = {q: v for q, v in c["evidence"].items() if v}
        c["flags"] = sorted(set(c["flags"]) | {"format_stress"})
    for q, v in c["evidence"].items():
        for x in v:
            assert x in c["text"], (c["chart_id"], q, x)
    return c

# --------------------------------------------------------------------------- splits and main


def main(out_dir):
    rng = random.Random(SEED)
    fu = [json.loads(l) for l in open(os.path.join(ROOT, "followup", "data", "charts.jsonl"))]
    stage1 = {l.strip() for l in open(os.path.join(ROOT, "followup", "stage1_ids.txt")) if l.strip()}
    charts = [relabel(c) for c in fu]

    plan = [s for s, spec in HARD.items() for _ in range(spec[1])]
    hard = [build_hard(rng, 1001 + i, s) for i, s in enumerate(plan)]

    # splits: stage-1 charts (results seen) -> dev; 25 stage-2 charts stratified by family -> dev; hard: per scenario
    for c in charts:
        c["split"] = "dev" if c["chart_id"] in stage1 else "test"
    s2 = sorted((c for c in charts if c["split"] == "test"), key=lambda c: c["chart_id"])
    by_fam = collections.defaultdict(list)
    for c in s2:
        by_fam[c["family"]].append(c)
    quota = {f: len(v) * 25 / len(s2) for f, v in by_fam.items()}
    n = {f: int(q) for f, q in quota.items()}
    for f in sorted(quota, key=lambda f: quota[f] - n[f], reverse=True)[:25 - sum(n.values())]:
        n[f] += 1
    for f in sorted(by_fam):
        for c in rng.sample(by_fam[f], n[f]):
            c["split"] = "dev"
    by_s = collections.defaultdict(list)
    for c in hard:
        by_s[c["scenario"]].append(c)
    for s, cs in by_s.items():
        dev = set(x["chart_id"] for x in rng.sample(cs, HARD[s][4]))
        for c in cs:
            c["split"] = "dev" if c["chart_id"] in dev else "test"
    allc = charts + hard
    assert len(allc) == 350 and sum(c["split"] == "dev" for c in allc) == 150

    os.makedirs(os.path.join(out_dir, "charts"), exist_ok=True)
    for c in allc:
        with open(os.path.join(out_dir, "charts", f"{c['chart_id']}.txt"), "w") as f:
            f.write(c["text"])
    with open(os.path.join(out_dir, "charts.jsonl"), "w") as f:
        for c in allc:
            f.write(json.dumps(c) + "\n")
    with open(os.path.join(out_dir, "labels.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["chart_id", "split", "family", "label", "relabeled", "scenario", *QIDS, "ambiguous_fields", "flags"])
        for c in allc:
            a = c["intended_answers"]
            w.writerow([c["chart_id"], c["split"], c["family"], c["label"], int(c["study3_relabeled"]), c["scenario"],
                        *[a[q] for q in QIDS], ";".join(c["ambiguous_fields"]), ";".join(c["flags"])])
    digest = hashlib.sha256(open(os.path.join(out_dir, "charts.jsonl"), "rb").read()).hexdigest()
    cnt = collections.Counter((c["split"], c["label"]) for c in allc)
    print(f"wrote {len(allc)} charts to {out_dir}; sha256 {digest}")
    print("split/label:", dict(sorted(cnt.items())), "| relabeled:", sum(c["study3_relabeled"] for c in allc))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "data"))
