# Follow-up pre-registration: transfer test of the frozen EWC pipeline on harder charts

Status: draft until `followup/FREEZE.json` exists. The design is in `followup/SPEC.md`; this file fixes what will be measured, how, and what counts as a result.

## 1. Question

Does the evidence-weighted confidence (EWC) pipeline, frozen after the pilot, still beat the models' own confidence on harder synthetic charts it has never seen? Where does it fail?

## 2. What is frozen from the pilot

Everything in the pilot's `FREEZE.json` (SHA-256 e8619565765170cf00776b61628a588f75dfb8214f070706aa06dee6f9cf64fd): prompts (version 1), rubric (version 2), harness code, `config.json` (models `gpt-5.4-2026-03-05` and `gemini-3.8-flash`, 5 extraction runs and 5 verbal runs per chart, output cap 16,000 tokens), and each model's dev-fitted weights (M5, M7, M8), Platt map (M2) and auto-accept thresholds. The runner checks these hashes before every collection and evaluation. Nothing is refitted.

The only setting changed in memory is concurrency (8 calls at once instead of 4); it does not affect any result.

## 3. Data

- `followup/data/charts.jsonl`, generator v3, seed 20261027, 300 charts, SHA-256 ba93d3aa60fa44c7ec15a1f9a04da0afee5ec38f0e752cafb412ed0b2428aedb.
- Main set: 255 charts in families A–E and G (129 labeled 1). Stress test: 45 charts in family F (all labeled 0).
- Labels: the pilot rule applied to each chart's facts, plus three rules that GPT-5.4 and Gemini both rated high-confidence (R1 face-to-face encounter with an acceptable provider; R2 signature with credentials; R3 secondary diabetes is not type 2). No human coder confirmed R1–R3.
- Checks before freezing: the generator's internal assertions; `followup/check_charts_v3.py` (0 of 300 charts with problems; it caught 7 of 7 deliberately planted errors); and the user's review of 40 stage-1 charts (`followup/review/`). The review outcome is recorded in `CHANGELOG.md` before the freeze.

## 4. Stages

- **Stage 1:** the 100 charts listed in `followup/stage1_ids.txt` (85 main, chosen in proportion to each scenario; 15 stress test, 5 per type), drawn with seed 101 before the freeze.
- **Stage 2:** the other 200 charts.

**Go/no-go after stage 1, per model, on technical grounds only:**

- errors (calls that never succeeded) at most 2%;
- unparseable responses at most 2%;
- quote failures below 50% (a higher rate means verification is broken, not that charts are hard);
- input tokens per chart at most 1.5 times the estimate.

If all four pass, stage 2 runs with nothing changed, and the final analysis uses all 300 charts. If a check fails, the cause is fixed, the change is logged, the follow-up is frozen again, and stage 2 runs. Stage 1 is then reported as a rehearsal and excluded from the final analysis, which uses the 200 stage-2 charts. **Stage-1 results (AUROC, calibration, coverage) are never a reason to change anything.** The user may stop after stage 1 for cost or other reasons; stage 1 is then reported as a directional result.

## 5. Methods

M1–M8 exactly as frozen in the pilot. One new baseline:

- **M9, criteria-informed verbal confidence** (prompt version 1, in `followup/run_transfer.py`): the pilot's verbal-confidence question, with the rubric's questions and guidance added as "criteria to consider". One run per chart. It is not Platt-scaled, because there is no dev split; it is compared on AUROC.

## 6. Hypotheses and pass marks

Computed per model on the main set of the final analysis set (section 4), with 95% bootstrap intervals (2,000 resamples, seed 0).

| ID | Claim | Pass mark |
|---|---|---|
| H1–H5 | As in the pilot pre-registration | Pilot pass marks, unchanged (frozen harness checks) |
| H6 | EWC ranks better than self-reported confidence | M5 AUROC − M2 AUROC ≥ 0.10, and the lower bound of the paired bootstrap interval > 0 |
| H7 | EWC ranks better than criteria-informed confidence | M5 AUROC − M9 AUROC > 0; paired interval reported |
| H8 | Quote verification helps | Tested only if at least 3% of yes/no answers fail verification: M5 beats M7 on ECE or AUROC. Otherwise reported as untested |
| H9 | The frozen auto-accept threshold transfers | Precision of M5 at the frozen threshold, with coverage (descriptive; the target is 0.95) |
| H10 | Out-of-rubric failure is measured | Family F: mean M5 score and share of charts above the frozen threshold, overall and per type (descriptive) |

Also reported, without pass marks: results by family; the frozen pilot report (extraction accuracy per question, quote failures, reproducibility) for each stage.

## 7. Analysis rules

- Each model's evaluation runs once per stage and once for the combined set (the runner refuses a second evaluation).
- Ambiguous answer fields (listed per chart) are reported separately for extraction accuracy, as in the pilot.
- No chart is excluded after results are seen. Charts that fail collection after retries are reported as missing.
- Any deviation from this document is logged in `CHANGELOG.md` with the reason, and reported.

## 8. Limitations stated in advance

- Synthetic charts written from phrase banks; labels decided by rules applied to the generator's facts. The main-set labels still follow mostly from rubric-visible facts; family F is the deliberate exception.
- R1–R3 were suggested by two models and not confirmed by a certified coder.
- The rubric's Q2 (eGFR criteria) is clinical validation rather than a coding rule, and the pilot's "other cause → not supported" rule may be stricter than coding guidance allows (both raised by the models). Both are kept as frozen.
- Positive rate (51% in the main set) is far above real populations.
- The generator and these charts were written with Claude, which is not one of the tested models.

## 9. Planned next study (not part of this one)

Rubric version 3 adding R1–R3 as rubric questions, with a fresh dev split, fitting and freeze. This would test whether a rubric that covers these rules removes the family-F failure.
