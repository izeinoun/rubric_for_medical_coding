"""
Independent checks for the study-3 data. Reads only study3/data/charts.jsonl and the note text.

- The 300 follow-up charts: the follow-up checker (followup/check_charts_v3.py) on each, plus: text identical to the
  follow-up data, and labels equal to the study-3 rule (relabeled scenarios now 1).
- The 50 hard cases: the scenario's defining wording is in the right section, Q1 matches stage wording, Q2 is
  recomputed from the dated eGFR results in the text, R1/R2 match the header and signature, and every evidence
  string is an exact substring.

Run:  python study3/check_data.py [study3/data/charts.jsonl]
"""

import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "followup"))
import check_charts_v3 as K  # noqa: E402

RELABELED = {"B2_copy_stale", "B4_per_last_visit", "G4_list_entry", "A_N1b_laundry_list"}


def ap_section(t):
    return K.section(t, r"\n(ASSESSMENT AND PLAN|ASSESSMENT/PLAN|IMPRESSION AND PLAN)\s")


def check_hard(c):
    errs = []
    t = K.clean(c["text"])
    low, a, s = t.lower(), c["intended_answers"], c["scenario"]
    ap = ap_section(t).lower()
    hpi = K.section(t, r"\nHISTORY OF PRESENT ILLNESS\s").lower()
    pl = K.section(t, r"\nPAST MEDICAL HISTORY / PROBLEM LIST\n").lower()
    meds = K.section(t, r"\nMEDICATIONS\n").lower()
    res = K.egfr_results(t)
    latest = res[-1][1] if res else None

    need = {
        "H1a": [("no history of kidney disease" in hpi, "HPI denial missing"), (re.search(K.STAGE_WORDS, ap) is not None, "plan CKD line missing")],
        "H1b": [("stage 4" in pl, "problem list stage 4 missing"), ("stage 3a" in ap, "plan stage 3a missing")],
        "H1c": [("type 1" in hpi, "HPI type 1 missing"), (re.search(r"type 2|t2dm", ap) is not None, "plan type 2 missing")],
        "H1d": [("chronic kidney disease stage 3a" in pl, "problem list CKD missing"),
                (re.search(r"possible|rule out|not yet established|lab variation", ap) is not None, "plan 'possible' missing")],
        "H2a": [("3a" in ap, "stage 3a missing"), (latest is not None and latest < 30, "eGFR not in stage-4 range")],
        "H2b": [("stage 4" in low or "ckd 4" in low, "stage 4 missing"), (latest is not None and latest >= 45, "eGFR not in stage-3 range")],
        "H3a": [("on hemodialysis" in ap, "dialysis not in plan"), ("metformin" not in meds and "flozin" not in meds, "metformin or SGLT2 listed")],
        "H3b": [("on hemodialysis" in pl, "ESRD missing from problem list"), ("hemodialysis" not in ap, "ESRD addressed in plan")],
        "H3c": [("not on dialysis" in ap, "'not on dialysis' missing"), ("metformin" not in meds, "metformin listed")],
        "H4a": [("ckd?" in ap, "'CKD?' missing")],
        "H4b": [("kidneys ok per last labs" in ap, "'Kidneys OK' missing"), ("chronic kidney disease" not in low and "ckd" not in low, "CKD named")],
        "H4c": [("renal involvement" in ap, "'renal involvement' missing"), ("chronic kidney disease" not in low and "ckd" not in low, "CKD named")],
        "H4d": [(re.search(r"\. continue\n", ap) is not None, "plan line not cut off")],
    }[s[:3]]
    errs += [msg for ok, msg in need if not ok]
    if (a["Q1"] == "yes") != bool(re.search(K.STAGE_WORDS, low)):
        errs.append(f"Q1={a['Q1']} vs stage wording")
    if K.q2_from(res) != a["Q2"]:
        errs.append(f"Q2 recomputed {K.q2_from(res)} != {a['Q2']}")
    if a["R1"] != "yes" or "face-to-face" not in low:
        errs.append("R1")
    if a["R2"] != "yes" or not re.search(r"Electronically signed: [^\n]*" + K.CRED, t):
        errs.append("R2")
    for q, v in c["evidence"].items():
        for x in v:
            if x not in c["text"]:
                errs.append(f"evidence {q} not in text")
    return errs


def main(path):
    charts = [json.loads(l) for l in open(path)]
    fu = {json.loads(l)["chart_id"]: json.loads(l) for l in open(os.path.join(ROOT, "followup", "data", "charts.jsonl"))}
    bad = 0
    for c in charts:
        if c["source"] == "followup":
            o = fu[c["chart_id"]]
            errs = K.check(c)
            if c["text"] != o["text"]:
                errs.append("text differs from follow-up data")
            want = 1 if c["scenario"] in RELABELED else o["label"]
            if c["label"] != want:
                errs.append(f"label {c['label']} != expected {want}")
            if (c["intended_answers"]["R1"] == "yes") != (c["facts"]["encounter"] == "f2f" and c["facts"]["provider_type"] in {"MD", "DO", "NP", "PA"}):
                errs.append("R1 vs facts")
        else:
            errs = check_hard(c)
        if errs:
            bad += 1
            print(c["chart_id"], c["scenario"], "; ".join(errs))
    cnt = collections.Counter((c["split"], c["label"]) for c in charts)
    print(f"\n{len(charts)} charts; {bad} with problems")
    print("split/label:", dict(sorted(cnt.items())))
    print("hard cases by split:", dict(collections.Counter(c["split"] for c in charts if c["source"] != "followup")))
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "data", "charts.jsonl")) else 0)
