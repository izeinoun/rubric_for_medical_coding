# Follow-up study spec: transfer test on harder charts (draft for review)

Status: **draft, not pre-registered.** Nothing here has been generated or run. The pilot's data, pre-registration and frozen pipeline are untouched.

Decisions made with the user on 2026-10-27:

- **Transfer test only.** The frozen pilot pipeline is applied, unchanged, to a new set of harder charts. Every new chart is a test chart: no dev split, no refitting, no prompt or rubric iteration.
- **Models:** GPT-5.4 (`gpt-5.4-2026-03-05`) and Gemini 3.8 Flash (`gemini-3.8-flash`), as in the pilot.
- **Family F (outside the rubric) is a separate stress test**, not part of the headline numbers.
- **Coding rules for the new labels:** only rules that both GPT-5.4 and Gemini rated high-confidence and agreed on (section 3). No human confirmed them; this is stated as a limitation.
- Cost of a larger, longer chart set is acceptable.

## 1. Question

Does the method we froze after the pilot still beat the models' own confidence on harder charts it has never seen, and where does it break?

The pilot showed that evidence-weighted confidence (EWC, M5) ranks and calibrates far better than self-reported confidence (M1, M2) on both models. It also left gaps:

| Gap in the pilot | Evidence | What this study adds |
|---|---|---|
| Labels are a function of the rubric answers | Pre-registration section 3; M5 AUROC 1.000 on both models once the 2 flagged test charts are removed | Family F: charts whose label depends on facts the rubric does not ask about |
| Quote verification never tested | 0 quote failures on dev and test for both models; M7 identical to M5 | Format stress (family H) that makes exact quoting hard |
| Gates trivially easy | G1 and G2 macro-F1 1.000 everywhere | Family C: unclear diabetes type, secondary diabetes, CKD resolved |
| Copy-forward drives every error | SYN-0182 (F1b) was the only wrongly accepted test chart for both models | Family B: copy-forward variants with clear labels |
| Few charts in the middle of the probability range | Most M5 scores are near 0 or 1 | Family G: borderline charts |
| Small test set | 60 charts; AUROC intervals about 0.1 wide | 255 main charts |
| Weak confidence baseline | The verbal prompt gives no criteria | M9: confidence with the rubric's criteria in the prompt |

## 2. What stays frozen

Taken unchanged from the pilot freeze (`FREEZE.json`, SHA-256 e8619565…):

- Prompts (version 1), rubric (version 2), harness code, model names.
- For each model: the dev-fitted weights for M5, M7 and M8, the Platt map for M2, and the auto-accept thresholds.

The follow-up runner (`followup/run_transfer.py`, to be written) imports the frozen harness modules without editing them. It points them at the new data file and a new output folder (`followup/runs/`), and uses copies of the frozen weights whose hashes are checked against `FREEZE.json` before any call.

**What is new, and pre-registered before any model call:** the charts, the label rules in section 3, the M9 prompt, the runner, and the hypotheses in section 6.

## 3. Label rules

A chart is labeled 1 (supports E11.22 for risk-adjustment submission) only if all of these hold:

**From the pilot (unchanged):** type 2 diabetes documented (G1); CKD documented as an established diagnosis (G2); CKD addressed at this encounter (Q4); and the provider has not attributed CKD to another cause (Q3 ≠ no).

**Added, agreed high-confidence by both models** (suggestions saved in `followup/rule_suggestions/`):

| ID | Rule | Effect | Source the models gave |
|---|---|---|---|
| R1 | The note documents a face-to-face encounter with an acceptable provider type (physician or qualified non-physician practitioner) | Rejects otherwise | CMS risk-adjustment and RADV guidance (both models; exact citation not confirmed) |
| R2 | The note carries a valid provider signature with credentials | Rejects otherwise | CMS RADV medical-record standards (both models; exact citation not confirmed) |
| R3 | Secondary diabetes (drug- or chemical-induced, due to an underlying condition, post-procedural) is not type 2 diabetes | Rejects E11.22 | ICD-10-CM Official Guidelines, Chapter 4 (both models) |

**Suggested but not used**, because the two models did not both rate them high-confidence or did not agree:

- Diabetes itself must also be addressed at the visit (both models: medium).
- "History of" or "resolved" CKD is not current CKD (GPT only, medium). Charts in family C use it only where the pilot's G2 rule already covers it ("explicitly absent").
- Cloned text contradicted by the current assessment (GPT only, medium).
- Additional N18 and Z99.2 codes: these change the full code set, not whether E11.22 itself is supported.
- Audio-only telehealth: Gemini said "allowable telehealth modality" without saying which; not used.

**Concerns the models raised about the frozen rubric** (stated as limitations, not changed):

- Q2 (two low eGFR results 90 days apart) is clinical validation, not a coding rule. This is consistent with the pilot: Q2's fitted weight was near 0 for both models.
- Gemini notes that a patient can have both hypertensive and diabetic CKD, so the pilot's "other cause → not supported" rule may be too strict. New charts avoid contested attributions (no assessment-versus-HPI conflicts about the cause).

## 4. Scenario families

Counts are for a 300-chart set: 255 main charts (families A–E and G) and 45 stress-test charts (family F). Format stress (family H) is applied across families.

### A. Carried over from the pilot (60 charts)

The 13 pilot scenarios at reduced counts, written with the new note template and format stress, so that results on familiar scenarios can be compared with the pilot. F1b (copy-forward stale) is replaced by family B.

### B. Copy-forward (45 charts, 9 per scenario)

| ID | Label | What the note shows |
|---|---|---|
| B1 | 1 | Plan copied forward; the CKD line cites today's eGFR with today's date and a current action |
| B2 | 0 | Plan copied word for word from a dated prior visit; eGFR and action both carry the prior date; no CKD content elsewhere in today's note |
| B3 | 1 | Copied CKD line followed by a new line from today ("eGFR today 41, stable; continue") |
| B4 | 0 | Copied CKD line marked "per last visit" or "unchanged from 3/2026"; today's labs are not mentioned |
| B5 | 1 | Interval history gives today's renal labs; the plan's CKD line refers to them |

Rule for writing these: the label must be decidable from the text, with no review flag. If a draft chart needs one, rewrite it or drop it.

### C. Gates made harder (36 charts, 6 per scenario)

| ID | Label | What the note shows |
|---|---|---|
| C1 | 1 | "DM" or "diabetes" with no type, on metformin; CKD due to diabetes (type 2 by ICD-10-CM default) |
| C2 | 1 | Type 2 diabetes on insulin (insulin use does not make it type 1) |
| C3 | 0 | Type 1 diabetes stated only in the HPI; the assessment says "diabetes" |
| C4 | 0 | Steroid-induced or post-pancreatectomy diabetes with CKD (rule R3) |
| C5 | 1 | "History of CKD" in the HPI, and the plan gives a current CKD status and action |
| C6 | 0 | Kidney transplant recipient; the note says CKD is resolved after transplant (CKD explicitly absent) |

### D. Lab and date edge cases for Q2 (26 charts)

eGFR exactly 60; result gaps of 89, 90 and 91 days; a missing date; creatinine without eGFR; eGFR given as "> 60"; results written in a sentence instead of a lab table. Q2 does not decide the label, so these test extraction only.

### E. Cause attribution for Q3 (24 charts, 8 per scenario)

| ID | Label | What the note shows |
|---|---|---|
| E1 | 1 | "CKD due to diabetes and hypertension" (diabetes is one stated cause) |
| E2 | 1 | "Likely diabetic nephropathy" with CKD stage stated (hedged, but attributed) |
| E3 | 1 | Diabetic cause stated only in a dated prior-visit section; no other cause stated ("with" convention) |

### G. Borderline (64 charts, about 13 per scenario)

| ID | Label | What the note shows |
|---|---|---|
| G1 | 1 | CKD addressed only by "renal function reviewed, stable"; no stage, no cause |
| G2 | 0 | CKD in the plan with only "see nephrology note"; no status or action today |
| G3 | 1 | CKD addressed by a medication change for kidney function (for example, metformin reduced for eGFR) without the word CKD in that line |
| G4 | 0 | "CKD 3a" as one entry in a list of problems, with no status or action |
| G5 | 1 | "CKD 3a, stable on losartan" as its own plan line (minimal but real status and action) |

G3 generalizes pilot chart SYN-0055, the borderline case Gemini missed on dev. G4 and G5 bracket where "a current status" starts.

### F. Stress test: outside the rubric (45 charts, 15 per scenario, reported separately)

Each chart looks positive to the rubric (all of G1, G2, Q3 and Q4 would be answered as for a positive chart), but the label is 0 under rules R1–R3.

| ID | Label | Reason |
|---|---|---|
| F1 | 0 | Visit documented by an RN or a dietitian only (R1) |
| F2 | 0 | Note unsigned, or signed without credentials (R2) |
| F3 | 0 | Interprofessional e-consult: chart review, patient not seen (R1). Changed from "stand-alone lab report" while building the generator: a lab report has no assessment and plan, so the rubric itself would already score it 0 and it would not test anything outside the rubric. |

EWC is expected to score these as positive, because the rubric cannot see the reason. The study measures how often and how confidently.

### H. Format stress for quote verification (across families)

About half of all charts get one or more of:

- Longer notes: median about 3,400 characters, about 1.7 times the pilot's 2,000 (review of systems, surgical, family and social history, allergies, a fuller lab table, patient education, and a prior-visit section in about a quarter of charts).
- Lab tables with irregular spacing and tab characters.
- OCR-style noise: l/1 and O/0 swaps, words broken across lines with hyphens, stray page headers in the middle of a section.
- Repeated, nearly identical lines from earlier visits, differing only by date or value.
- Non-ASCII punctuation (curly quotes, en dashes, non-breaking spaces).

Because there is no dev split, the noise level cannot be tuned against model results. The generator fixes it in advance; whether quotes fail is an outcome, not a target.

## 5. Methods

M1–M8 exactly as frozen in the pilot. One new baseline:

- **M9, criteria-informed verbal confidence.** The verbal prompt also lists the rubric's questions and guidance, and asks for a probability (1 run per chart, decided 2026-10-27 to save cost). There is no dev split to fit a Platt map, so M9 is reported raw. AUROC is unaffected by Platt scaling, so the ranking comparison is fair; ECE for M9 is uncalibrated and is reported for information only.

## 6. Draft hypotheses (to be finalized in the follow-up pre-registration)

All on the 255 main charts unless stated, per model, with 95% bootstrap intervals (2,000 resamples).

| ID | Claim | Pass mark (draft) |
|---|---|---|
| H1–H5 | As in the pilot | Pilot pass marks, unchanged |
| H6 | EWC beats self-reported confidence on ranking, on unseen harder charts | M5 AUROC − M2 AUROC ≥ 0.10, with the lower bound of the paired bootstrap interval above 0 |
| H7 | EWC beats criteria-informed confidence on ranking | M5 AUROC − M9 AUROC > 0, with the paired interval reported |
| H8 | Quote verification helps | M5 beats M7 on ECE or AUROC. Tested only if at least 3% of yes/no answers fail verification; otherwise reported as untested |
| H9 | The frozen auto-accept threshold transfers | Precision of M5 at the frozen threshold, with interval (descriptive; target 0.95) |
| H10 | Out-of-rubric failure is visible | On family F: mean M5 score and the share of charts above the frozen threshold (descriptive) |

H6 adds a paired test, so "significantly better" can be claimed directly. Results are also broken down by family.

## 7. Size and cost

- 300 charts (255 main, 45 stress test), all test (trimmed from 400 at the user's request). Positive rate in the main set 51% (129 of 255); the pilot's was 44%.
- Per model and chart: 5 extraction, 5 verbal, 1 M6 and 1 M9 call = 12 calls, so 3,600 calls per model.
- `estimate` on the real charts: about 1.6M input tokens per model for stage 1 (100 charts) and 3.1M for stage 2, plus visible output and Gemini's thinking tokens.
- Run in two stages (decided 2026-10-27): stage 1 = 100 pre-selected charts with a technical go/no-go check, then stage 2 = the other 200. Details in `followup/PREREGISTRATION.md`. `estimate` gives a firmer figure once the data exists, and it will be reported before any run, with one test call per model.

## 8. Order of work

1. Write generator v3 (`followup/generate_charts_v3.py`) with the label rules in code. The pilot's `generate_charts.py` and `data/charts.jsonl` stay unchanged.
2. Check the labels without any model call: automatic consistency checks, plus a sample read by a person (section 9).
3. Write the runner and the M9 prompt; smoke-test them with the offline mock provider (mock results not committed).
4. Write the follow-up pre-registration (`followup/PREREGISTRATION.md`), and freeze the new data, label rules, runner and M9 prompt, with hashes, before any model call.
5. Collect for both models, then evaluate once per model. Report.

## 9. Reminder: rubric v3

The rules R1–R3 are used only in the labels here. Adding them to the rubric is a separate, later study (rubric v3, new dev split, fitting and freeze); see `followup/PREREGISTRATION.md` section 9. Raise it with the user after stage 1.

## 10. Open questions for the user

1. **Label check.** With no dev split, label errors go straight into the results. Can you, or a coder, read a sample (about 40 charts, stratified by scenario) and mark each label right or wrong before the freeze?
2. **Size.** Decided: 300 charts.
3. **M9.** Keep it in? It adds 1,500 calls per model (5 per chart).
