"""
Build the human label-review sheet for the follow-up charts: 40 charts, stratified by family, each with the
label, a plain-language reason, and what to check in the text. Writes followup/review/LABEL_REVIEW.md and
followup/review/label_review.csv (one row per chart for marking agree / disagree).

Run:  python followup/make_review_sheet.py
"""

import csv
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 40
PER_FAMILY = {"A": 6, "B": 7, "C": 7, "D": 5, "E": 3, "G": 6, "F": 6}

ANS = {"yes": "yes", "no": "no", "not_documented": "not documented"}

# scenario prefix -> (why the label is what it is, what to check in the note)
WHY = {
    "A_P1": ("Type 2 diabetes, established CKD with a stage, cause stated as diabetes, and CKD addressed in today's plan.",
             ["The plan has a CKD line with a current status or action (today's eGFR, a medication, labs ordered)."]),
    "A_P2": ("Type 2 diabetes and established CKD addressed today; no cause stated, so the ICD-10-CM 'with' convention links them.",
             ["No other cause of CKD is stated anywhere.", "The plan's CKD line has a current status or action."]),
    "A_P3": ("Diabetic CKD addressed in today's plan; no stage, which does not affect the label.",
             ["No CKD stage appears anywhere.", "The plan's CKD line has a current status or action."]),
    "A_P4": ("CKD addressed today; the diabetic cause is stated only in the HPI.",
             ["The HPI attributes the kidney disease to diabetes.", "The plan's CKD line has a current status or action."]),
    "A_F1a": ("Plan carried forward, but the CKD line uses today's results and a current action.",
              ["A copy-forward note is present.", "The CKD line cites today's eGFR (dated the visit day) and an action."]),
    "A_N1a": ("CKD appears only on the problem list; the assessment and plan does not address it.",
              ["No CKD line in the assessment and plan (a prior-visit section, if any, is not today's plan)."]),
    "A_N1b": ("CKD only named inside a list of problems in the plan, with no status or action.",
              ["CKD appears only in a 'problem list reviewed' or 'also on problem list' line."]),
    "A_N2": ("CKD is attributed to a non-diabetic cause, so E11.22 is not supported.",
             ["A non-diabetic cause is stated (hypertensive, polycystic, obstructive, IgA)."]),
    "A_N3": ("Low eGFR values but no CKD diagnosis by the provider.",
             ["No CKD diagnosis anywhere; only lab values."]),
    "A_N4": ("Type 1 diabetes, so not E11 (type 2).",
             ["The note says type 1 diabetes."]),
    "A_N5": ("CKD only possible or not yet established.",
             ["The CKD wording is 'possible', 'rule out' or 'not yet established'."]),
    "A_N6": ("Resolved acute kidney injury; CKD explicitly absent.",
             ["The note says CKD is not present / no evidence of CKD."]),
    "B1": ("Copied plan, but the CKD line cites today's eGFR with today's date and a current action.",
           ["Copy-forward marker present.", "CKD line: today's eGFR (dated the visit day) and an action."]),
    "B2": ("Plan copied from a prior visit; the CKD line refers only to an old eGFR and the old plan; nothing current.",
           ["The CKD line's eGFR is dated months before the visit.", "No eGFR from the last 30 days anywhere in the note.",
            "No other CKD status or action today."]),
    "B3": ("Copied (stale) CKD line, followed by a new line from today with today's eGFR.",
           ["The CKD item has an 'Update today' or 'Addendum' sentence with today's eGFR."]),
    "B4": ("CKD line says only 'per last visit / unchanged from <month>'; today's labs are not mentioned.",
           ["No eGFR from the last 30 days anywhere.", "The CKD line has no current status or action."]),
    "B5": ("Today's renal labs are reviewed in the interval history, and the copied plan line refers to them.",
           ["The HPI reviews today's labs (eGFR) with the patient.", "The CKD plan line points to today's results and an action."]),
    "C1": ("Diabetes with no type documented: ICD-10-CM defaults to type 2 (E11). CKD addressed today.",
           ["No diabetes type anywhere ('type 1', 'type 2', 'T2DM' absent).", "The plan's CKD line has a current status or action."]),
    "C2": ("Type 2 diabetes on insulin is still type 2. CKD addressed today.",
           ["The note says type 2 and lists insulin.", "The plan's CKD line has a current status or action."]),
    "C3": ("Type 1 diabetes (stated in the HPI) even though the plan says just 'diabetes', so not E11.",
           ["The HPI says type 1 diabetes.", "Nowhere says type 2."]),
    "C4": ("Secondary diabetes (steroid-induced or after pancreatectomy) is not type 2 (rule R3).",
           ["The diabetes is described as steroid-induced or due to pancreatectomy.", "Nowhere says type 2."]),
    "C5": ("'History of CKD' in the HPI, and the plan gives CKD a current status and action.",
           ["The plan's CKD line has a current status or action."]),
    "C6": ("CKD removed from the problem list: repeat testing shows normal kidney function.",
           ["The plan says the patient does not have CKD / CKD ruled out."]),
    "D_": ("Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).",
           ["Label 1 only if the plan has a CKD line with a current status or action.",
            "The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence)."]),
    "E1": ("CKD due to diabetes and hypertension; diabetes is a stated cause. CKD addressed today.",
           ["The plan states both diabetes and hypertension as causes.", "The plan's CKD line has a current status or action."]),
    "E2": ("'Likely diabetic nephropathy' with a CKD stage; the cause is hedged but not another disease. CKD addressed today.",
           ["The plan's CKD line has a current status or action."]),
    "E3": ("The diabetic cause appears only in a dated prior-visit section; today's plan addresses CKD without another cause.",
           ["The prior-visit section links CKD to diabetes; today's plan does not name another cause.",
            "Today's CKD line has a current status or action."]),
    "G1": ("Borderline: 'renal function reviewed, stable' counts as a current status.",
           ["The plan's CKD line is just 'renal function reviewed, stable'. Do you agree this counts as addressed?"]),
    "G2": ("Borderline: 'see nephrology note' gives no status or action today.",
           ["The plan's CKD line only points to nephrology. Do you agree this is not addressed?"]),
    "G3": ("Borderline: metformin reduced because of the eGFR counts as treating the kidney disease, even though CKD is not named in that line.",
           ["CKD is on the problem list; the diabetes plan reduces metformin because of eGFR. Do you agree this counts as addressed?"]),
    "G4": ("Borderline: CKD only in a 'chronic conditions reviewed' list, no status or action.",
           ["Do you agree this is not addressed?"]),
    "G5": ("Borderline: 'CKD 3a, stable on losartan' as its own line counts as status plus treatment.",
           ["Do you agree this minimal line counts as addressed?"]),
    "F1": ("Stress test: everything looks supported, but the visit is by a nurse or dietitian only, not an acceptable provider (rule R1).",
           ["Header and signature show RN or RD.", "Otherwise the chart would support E11.22."]),
    "F2": ("Stress test: everything looks supported, but the note is unsigned or signed without credentials (rule R2).",
           ["The note is marked not signed, or the signature has no MD/DO/NP/PA credential."]),
    "F3": ("Stress test: everything looks supported, but it is a chart-review e-consult; the patient was not seen (rule R1).",
           ["The header and HPI say the patient was not seen."]),
}


def why_for(scenario):
    for k in sorted(WHY, key=len, reverse=True):
        if scenario.startswith(k):
            return WHY[k]
    raise KeyError(scenario)


def main():
    charts = [json.loads(l) for l in open(os.path.join(HERE, "data", "charts.jsonl"))]
    rng = random.Random(SEED)
    picked = []
    for fam, n in PER_FAMILY.items():
        pool = [c for c in charts if c["family"] == fam]
        by_s = {}
        for c in pool:
            by_s.setdefault(c["scenario"], []).append(c)
        scen = sorted(by_s)
        rng.shuffle(scen)
        chosen = [rng.choice(by_s[s]) for s in scen[:n]]           # one per scenario first
        rest = [c for c in pool if c not in chosen]
        chosen += rng.sample(rest, n - len(chosen)) if len(chosen) < n else []
        picked += chosen
    picked.sort(key=lambda c: c["chart_id"])
    assert len(picked) == 40

    out = os.path.join(HERE, "review")
    os.makedirs(out, exist_ok=True)
    L = ["# Label review: 40 follow-up charts", "",
         "For each chart, read the note and decide whether the **label** (does the note support reporting E11.22 "
         "for risk adjustment?) is right, using the reason and the checks given. You do not need to check the "
         "rubric answers. Record your verdict in `label_review.csv` (agree / disagree, plus a short note), or just "
         "list the chart IDs you disagree with.", "",
         "About 45% of charts have deliberate 'format noise' (letters swapped with digits such as 'C1inician', words "
         "broken across lines, a stray page header). That is intended and is not an error.", "",
         "Label rules: supported (1) only if type 2 diabetes is documented (untyped diabetes defaults to type 2), CKD is "
         "an established diagnosis, CKD is addressed at this visit, no non-diabetic cause is given for the CKD, the visit "
         "is face-to-face with an MD, DO, NP or PA (R1), and the note is signed with credentials (R2). Secondary diabetes "
         "is not type 2 (R3).", ""]
    rows = []
    for i, c in enumerate(picked, 1):
        why, checks = why_for(c["scenario"])
        lab = "1 (supports E11.22)" if c["label"] else "0 (does not support E11.22)"
        L += [f"## {i}. {c['chart_id']} — {c['scenario']}", "",
              f"**Label: {lab}.** {why}", "", "Check:"] + [f"- [ ] {x}" for x in checks] + \
             ["", "<details><summary>Note text</summary>", "", "```", c["text"].rstrip("\n"), "```", "", "</details>", ""]
        rows.append([c["chart_id"], c["family"], c["scenario"], c["label"], why, "", ""])
    with open(os.path.join(out, "LABEL_REVIEW.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(out, "label_review.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["chart_id", "family", "scenario", "label", "reason", "verdict (agree/disagree)", "note"])
        w.writerows(rows)
    print(f"wrote {len(picked)} charts to {out}")


if __name__ == "__main__":
    main()
