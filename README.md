# EWC pilot: 200 synthetic E11.22 charts (generator v2)

## Paper

*Evidence-Weighted Confidence: Auditable, Calibrated Scoring of LLM Outputs*, Issam Zeinoun, 2026.
This version (with the experiments): https://doi.org/10.5281/zenodo.23745059. All versions: https://doi.org/10.5281/zenodo.23651100.
Source and PDFs in `paper/`: `medium.pdf` (the paper, 11 pages), `long.pdf` (extended version, 25 pages) and `short.pdf` (3-page summary). The studies are in `harness/` (pilot), `followup/` (transfer test) and `study3/` (main study).

Synthetic outpatient office-visit notes for piloting evidence-weighted confidence (EWC). Every chart is scored against one candidate code, **E11.22** (type 2 diabetes mellitus with diabetic chronic kidney disease). All patients, providers and dates are fictional.

## Files

| File | Contents |
|---|---|
| `PREREGISTRATION.md` | Success and kill criteria. Review and freeze before running any extraction |
| `CHANGELOG.md` | Every version of the data and pipeline, with what changed and why |
| `CLAUDE.md` | Instructions Claude Code reads automatically: hard rules for running the pilot |
| `harness/` | The experiment code. Start with `harness/RUNNING.md` |
| `generate_charts.py` | The generator (Python 3, standard library only, seed 20261024; same seed gives identical output) |
| `data/charts/SYN-0001.txt` … `SYN-0200.txt` | One plain-text note per chart. **Only these go to the model under test** |
| `data/charts.jsonl` | Full record per chart: label, scenario, intended rubric answers, evidence strings, facts, flags, split, note text |
| `data/labels.csv` | One row per chart: id, split, label, scenario, intended answers, ambiguous fields, flags |
| `data/rubric_questions.json` | The six rubric questions and the meaning of each answer value |

Regenerate with `python generate_charts.py data`.

## Ground truth

Label 1 means the note supports reporting E11.22 for a risk-adjustment submission. The rule:

> label = 1 if G1 = yes, G2 = yes, Q3 ≠ no, and Q4 = yes

This encodes four requirements: type 2 diabetes documented; CKD documented as an established diagnosis; CKD addressed in this face-to-face encounter; and the provider has not attributed CKD to another cause. ICD-10-CM's "with" convention presumes the diabetes-CKD link when no other cause is stated, so silence on Q3 does not block the code. The label means "acceptable for risk-adjustment submission," which is stricter than "codable."

| ID | Question |
|---|---|
| G1 | Type 2 diabetes mellitus documented as a current diagnosis |
| G2 | Chronic kidney disease documented as an established diagnosis |
| Q1 | CKD stage documented |
| Q2 | eGFR below 60 on two results at least 90 days apart |
| Q3 | Provider attributes CKD to diabetes |
| Q4 | CKD addressed this encounter (monitored, evaluated, assessed or treated) |

| Answer | Meaning |
|---|---|
| yes | The note affirmatively documents the fact |
| no | The note explicitly documents the opposite, or says the fact is not established |
| not_documented | The note is silent |

## Scenarios

| Scenario | Count | Test | Label | What the note shows |
|---|---|---|---|---|
| P1_stage_and_link | 32 | 10 | 1 | CKD with stage, explicitly due to type 2 diabetes in the assessment, addressed in plan |
| P2_with_convention | 28 | 8 | 1 | CKD with stage, no cause stated, addressed in plan |
| P3_link_no_stage | 14 | 4 | 1 | Diabetic CKD addressed in plan, stage not documented |
| P4_link_in_hpi | 8 | 2 | 1 | CKD addressed in plan; diabetic cause stated only in the HPI |
| F1a_copy_fwd_current | 6 | 2 | 1 | Plan carried forward, but the CKD line uses today's results and a current action |
| F1b_copy_fwd_stale | 6 | 2 | 0 | Plan carried forward with a stale eGFR and no sign of current CKD evaluation (flag `label_needs_review`) |
| N1a_problem_list_only | 18 | 5 | 0 | CKD on the problem list only |
| N1b_laundry_list | 12 | 4 | 0 | CKD named in a list of problems inside the plan, with no status or action |
| N2_other_cause | 20 | 6 | 0 | CKD attributed to hypertensive nephrosclerosis, polycystic kidney disease, obstructive uropathy or IgA nephropathy; in the assessment (about 60%) or only in the HPI |
| N3_labs_only | 18 | 6 | 0 | Two low eGFR values, no CKD diagnosis |
| N4_type1 | 14 | 4 | 0 | Type 1 diabetes with CKD |
| N5_uncertain_dx | 14 | 4 | 0 | Possible, rule-out or not-yet-established CKD |
| N6_aki_not_ckd | 10 | 3 | 0 | Resolved acute kidney injury, CKD explicitly absent |
| **Total** | **200** | **60** | 88 / 112 | |

Within each scenario the stage (3a, 3b, 4), the number of eGFR results, the wording, the medications, the section order and two to six unrelated problems vary. About 10% of ordinary charts also carry a copy-forward marker, and about 25% list some unrelated problems in a bare "problem list reviewed" line, so neither feature predicts the label.

## Using the data

- Give the model only the `.txt` note. Never pass `charts.jsonl` fields.
- Score extraction accuracy against `intended_answers`. Report fields listed in `ambiguous_fields` separately, because two answers are defensible there (N3 G2; N5, N6, N1b and F1b Q4).
- Report headline metrics with and without the six `label_needs_review` charts (F1b).
- `evidence` lists strings inserted verbatim for each answer; use them to check whether a model's quotes point at the right part of the note.
- Keep `split = test` charts closed until the pipeline is frozen (see the pre-registration).

## Review so far

An independent review of 20 charts (two per scenario, read blind) agreed with every label. It flagged an over-confident copy-forward label, label-leaking phrases and several clinical inconsistencies; version 2 addresses them (see `CHANGELOG.md`). Labels have not been reviewed by a certified coder. Spot-checking 20–30 charts before relying on them is recommended.

## Known limitations

- **Deterministic labels.** The label is a function of the rubric facts, so perfect extraction gives near-perfect separation. The pilot tests extraction, verification and scoring mechanics, not real-world calibration.
- **Template regularity.** Notes come from phrase banks and one note template. They are cleaner and more uniform than real charts, and some negative scenarios still use recognizable wording (for example "possible" or "rule out" CKD), because that wording is the fact itself.
- **Same-model risk.** The phrase banks were written with Claude. Run extraction with at least one non-Claude model.
- **Prevalence.** 44% of charts are positive, far above a real diabetic population. Fitted intercepts will not transfer to real data.
