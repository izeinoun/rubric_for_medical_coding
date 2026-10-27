# Follow-up pre-registration: transfer test of the frozen EWC pipeline on harder charts

Status: draft until `followup/FREEZE.json` exists. Simplified on 2026-10-27 at the user's request to one comparison: EWC against the model's stated confidence, with and without the rubric's questions. The design is in `followup/SPEC.md`; this file fixes what will be measured, how, and what counts as a result.

## 1. Question

Does the evidence-weighted confidence (EWC) pipeline, frozen after the pilot, still beat the models' own confidence on harder synthetic charts it has never seen? Where does it fail?

## 2. What is frozen from the pilot

Everything in the pilot's `FREEZE.json` (SHA-256 e8619565765170cf00776b61628a588f75dfb8214f070706aa06dee6f9cf64fd): prompts (version 1), rubric (version 2), harness code, `config.json` (models `gpt-5.4-2026-03-05` and `gemini-3.8-flash`, 5 extraction runs and 5 verbal runs per chart, output cap 16,000 tokens), and each model's dev-fitted weights (M5, M7, M8), Platt map (M2) and auto-accept thresholds. The runner checks these hashes before every collection and evaluation. Nothing is refitted.

The only setting changed in memory is concurrency (8 calls at once instead of 4); it does not affect any result.

## 3. Data

- `followup/data/charts.jsonl`, generator v3, seed 20261027, 300 charts, SHA-256 689770cb9b688a8f7c8cffc6e36a35b2245d0068fa1c7555f9c7b37bc0e0105b.
- Main set: 255 charts in families A–E and G (129 labeled 1). Stress test: 45 charts in family F (all labeled 0).
- **Contested labels:** 37 main-set charts (scenarios B2 and B4, copy-forward CKD lines that cite only old results; G4, CKD only in a reviewed-problems list) are flagged `label_needs_review`. The generator labels them 0, following the frozen rubric's own rule; the human review labeled the sampled ones 1 (MEAT reading: "continue regimen" or "stable" counts as addressed). They are excluded from the primary analysis set and reported in a sensitivity analysis both ways (section 6).
- Labels: the pilot rule applied to each chart's facts, plus three rules that GPT-5.4 and Gemini both rated high-confidence (R1 face-to-face encounter with an acceptable provider; R2 signature with credentials; R3 secondary diabetes is not type 2). No human coder confirmed R1–R3.
- Checks before freezing: the generator's internal assertions; `followup/check_charts_v3.py` (0 of 300 charts with problems; it caught 7 of 7 deliberately planted errors); and a human review of 40 stage-1 charts by the study lead, who used Gemini 3.1 Pro as a reading aid (`followup/review/`). Result: 34 agree, 6 disagree. Five disagreements were the contested copy-forward and list-only charts above (B2 ×3, B4, G4). One (FU-0049, scenario E1, "CKD due to type 2 diabetes and hypertension") was labeled 0 by the reviewer because a non-diabetic cause is named; the label stays 1, because coding guidance supports E11.22 when diabetes is one of the stated causes, and the review page's rule wording ("no non-diabetic cause is given") was misleading and has been corrected to "a different cause instead of diabetes". The disagreement is recorded here and in `CHANGELOG.md`.

## 4. Stages

- **Stage 1:** the 100 charts listed in `followup/stage1_ids.txt` (85 main, chosen in proportion to each scenario; 15 stress test, 5 per type), drawn with seed 101 before the freeze.
- **Stage 2:** the other 200 charts.

**Go/no-go after stage 1, per model, on technical grounds only:**

- errors (calls that never succeeded) at most 2%;
- unparseable responses at most 2%;
- quote failures below 50% (a higher rate means verification is broken, not that charts are hard);
- input tokens per chart at most 1.5 times the estimate.

If all four pass, stage 2 runs with nothing changed, and the final analysis uses all 300 charts. If a check fails, the cause is fixed, the change is logged, the follow-up is frozen again, and stage 2 runs. Stage 1 is then reported as a rehearsal and excluded from the final analysis, which uses the 200 stage-2 charts. **Stage-1 results (AUROC, calibration, coverage) are never a reason to change anything.** The user may stop after stage 1 for cost or other reasons; stage 1 is then reported as a directional result.

## 5. Methods compared

Three methods, all from the same models on the same charts:

| | Method | What it is |
|---|---|---|
| A | The model's stated confidence | The pilot's verbal-confidence prompt (frozen): "does this note support the code?", 0–100. Reported raw (pilot M1) and recalibrated with the frozen pilot Platt map (pilot M2). Recalibration changes calibration, not ranking. |
| B | Evidence-weighted confidence (EWC) | The frozen pilot method (pilot M5): rubric answers with exact quotes, code-verified, scored with the frozen dev-fitted weights. |
| C | Criteria-guided confidence | A's question plus the rubric's questions and guidance, with the model told to answer each criterion for itself and base its confidence on those answers (prompt version 1, in `followup/run_transfer.py`). One run per chart. Not recalibrated, because there is no dev split; compared on AUROC. |

Per chart and model: 5 extraction runs and 5 verbal runs (frozen pilot settings) and 1 run for C, 11 calls in all. The frozen pilot evaluation also reports its other variants (M3, M4, M7, M8) from the same calls; they are not part of this study's claims. M6 is not collected.

## 6. Hypotheses and pass marks

Computed per model on the **primary analysis set**: the main-set charts of the final analysis set (section 4) without contested labels (218 of 255 charts over all 300; 73 of 85 in stage 1). 95% bootstrap intervals (2,000 resamples, seed 0).

| ID | Claim | Pass mark |
|---|---|---|
| H1 | B ranks better than the model's stated confidence (A) | B AUROC − A AUROC ≥ 0.10, and the lower bound of the paired bootstrap interval > 0 |
| H2 | B ranks better than criteria-guided confidence (C) | B AUROC − C AUROC > 0, and the lower bound of the paired bootstrap interval > 0 |
| H3 | B is better calibrated than recalibrated A | B ECE ≤ A (recalibrated) ECE |
| H4 | The frozen auto-accept threshold for B transfers | Precision of B at the frozen threshold, with coverage (descriptive; target 0.95) |
| H5 | Out-of-rubric failure is measured | Family F: mean score of A, B and C, and the share of charts B would auto-accept, overall and per type (descriptive) |

Also reported, without pass marks: results by family; extraction accuracy per question and quote-failure rate (frozen pilot report); and a **sensitivity analysis** on all main-set charts with the contested charts labeled 0 (generator) and 1 (human review): AUROC of A, B and C and the paired B − A difference under each.

## 7. Analysis rules

- Each model's evaluation runs once per stage and once for the combined set (the runner refuses a second evaluation).
- Ambiguous answer fields (listed per chart) are reported separately for extraction accuracy, as in the pilot.
- No chart is excluded after results are seen. Charts that fail collection after retries are reported as missing.
- Any deviation from this document is logged in `CHANGELOG.md` with the reason, and reported.

## 8. Limitations stated in advance

- Synthetic charts written from phrase banks; labels decided by rules applied to the generator's facts. The main-set labels still follow mostly from rubric-visible facts; family F is the deliberate exception.
- R1–R3 were suggested by two models and not confirmed by a certified coder.
- The rubric's Q2 (eGFR criteria) is clinical validation rather than a coding rule, and the pilot's "other cause → not supported" rule may be stricter than coding guidance allows (both raised by the models). Both are kept as frozen.
- Positive rate (59% in the primary analysis set, 51% in the whole main set) is far above real populations.
- Copy-forward and list-only CKD lines are contested: the frozen rubric does not count them as addressed, while a MEAT reading does. The sensitivity analysis shows how much the conclusion depends on that choice.
- The label review was done by one person, the study lead, with an AI reading aid, on 40 of 300 charts.
- The generator and these charts were written with Claude, which is not one of the tested models.

## 9. Possible next study (not part of this one)

Rubric version 3 adding R1–R3 as questions (as gates, they would need no fitted weights). This would test whether covering these rules removes the family-F failure. Considered for this study as an exploratory arm and dropped on 2026-10-27 to keep the design simple.
