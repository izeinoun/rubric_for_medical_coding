"""
Build the study-3 label-review page: two charts of each new hard-case scenario and two of each scenario relabeled
under the study lead's copy-forward rule (34 charts). Writes study3/review/label_review.html.

Run:  python study3/make_review_page.py
"""

import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 34

WHY = {
    "H1a": ("Supported. The HPI says 'no history of kidney disease', but the current assessment and plan addresses established CKD; the plan governs.",
            ["The HPI contains the denial.", "The plan has a CKD line with a current status or action."]),
    "H1b": ("Supported. The problem list and the plan give different stages; the stage conflict does not affect support.",
            ["The problem list and the plan state different stages.", "The plan's CKD line has a current status or action."]),
    "H1c": ("Supported. Outside records mention type 1, but the problem list and the current plan say type 2; the plan governs.",
            ["The HPI mentions type 1 from outside records.", "The plan says type 2."]),
    "H1d": ("Not supported. The problem list says CKD stage 3a, but the current plan says CKD is only possible; the plan governs.",
            ["The plan's kidney line is 'possible', 'rule out' or 'not yet established'."]),
    "H2a": ("Supported. The provider documents stage 3a though the eGFR is in the stage-4 range; coders do not override the documented stage.",
            ["The plan addresses CKD stage 3a.", "The latest eGFR is below 30."]),
    "H2b": ("Supported. The provider documents stage 4 though the eGFR is in the stage-3 range; the documented stage counts.",
            ["The note says stage 4.", "The latest eGFR is 45 or higher."]),
    "H3a": ("Supported. ESRD on hemodialysis due to diabetes, addressed in the plan (E11.22 with N18.6 and Z99.2).",
            ["The plan addresses ESRD on hemodialysis."]),
    "H3b": ("Not supported. ESRD on hemodialysis appears only on the problem list; the plan does not address it.",
            ["No kidney line in the assessment and plan."]),
    "H3c": ("Supported. CKD stage 5 not on dialysis, with conservative management addressed in the plan.",
            ["The plan addresses stage 5 not on dialysis."]),
    "H4a": ("Not supported. 'CKD?' is not an established diagnosis.",
            ["The plan's kidney line is 'CKD?' with labs to be checked."]),
    "H4b": ("Not supported. 'Kidneys OK per last labs' is not a CKD diagnosis, even with low eGFR values.",
            ["No CKD diagnosis anywhere in the note."]),
    "H4c": ("Not supported. 'DM with renal involvement' without a CKD diagnosis codes elsewhere (E11.29), not E11.22.",
            ["The plan says 'DM w/ renal involvement'.", "The note never names CKD."]),
    "H4d": ("Supported. The CKD plan line is cut off ('... Continue') but still gives today's status.",
            ["The CKD line gives today's eGFR or status before the cut-off."]),
    "B2_": ("Supported under your rule. The plan line is copied from an earlier visit with an old eGFR, but says 'continue regimen'.",
            ["The CKD line says to continue the regimen (copied text counts)."]),
    "B4_": ("Supported under your rule. The CKD line says 'per last visit, stable'.",
            ["The CKD line gives 'stable' (copied text counts)."]),
    "G4_": ("Supported under your rule. CKD is named in a 'chronic conditions reviewed' list in the plan.",
            ["CKD appears in the reviewed list."]),
    "A_N": ("Supported under your rule. CKD is named in a 'problem list reviewed' line in the plan (the twin of the reviewed-conditions list).",
            ["CKD appears in a 'problem list reviewed' or 'also on problem list' line in the plan."]),
}


def main():
    charts = [json.loads(l) for l in open(os.path.join(HERE, "data", "charts.jsonl"))]
    rng = random.Random(SEED)
    groups = {}
    for c in charts:
        if c["family"] == "H" or c["study3_relabeled"]:
            groups.setdefault(c["scenario"], []).append(c)
    picked = []
    for s in sorted(groups):
        picked += rng.sample(sorted(groups[s], key=lambda c: c["chart_id"]), 2)
    items = []
    for c in picked:
        key = c["scenario"][:3] if c["family"] == "H" else c["scenario"][:3]
        why, checks = WHY[key if key in WHY else c["scenario"][:3]]
        items.append({"id": c["chart_id"], "family": c["family"], "scenario": c["scenario"], "label": c["label"],
                      "why": why, "checks": checks, "text": c["text"], "noise": "format_stress" in c["flags"]})
    data = json.dumps(items).replace("</", "<\\/")
    html = open(os.path.join(HERE, "review", "template.html")).read().replace("__DATA__", data)
    with open(os.path.join(HERE, "review", "label_review.html"), "w") as f:
        f.write(html)
    print(len(items), "charts:", sorted({i["scenario"] for i in items}))


if __name__ == "__main__":
    main()
