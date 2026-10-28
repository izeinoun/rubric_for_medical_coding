# Study 3 pre-registration: rubric v3 on 350 charts

Fixed before the test split is run. Plan: `study3/SPEC.md`. Changes and dev results: `CHANGELOG.md`.

## 1. Question

When a model judges whether an outpatient note supports E11.22, does evidence-weighted confidence (B: the model answers rubric-v3 questions with exact quotes; code verifies the quotes and computes the score with dev-fitted weights) give a more trustworthy confidence than (A) the model's stated confidence, and than (C) the model's confidence when it is given the same questions and told to base its confidence on them?

## 2. Data

- `study3/data/charts.jsonl` (SHA-256 1e36b6256b2650f6c9f3c2b5dbafbf4570cb0abdae47b47ac1612d04bf701966), 350 synthetic charts: the 300 follow-up charts (texts unchanged, relabeled under the study-3 rules) and 50 hard cases (conflicting statements, stage against labs, ESRD and dialysis, unclear or partial statements). Three hard-case charts keep a doubled phrase ("not on dialysis not on dialysis") deliberately.
- Labels: rules agreed with the study lead (`study3/build_data.py` docstring), including R1 (face-to-face with an MD, DO, NP or PA), R2 (signed with credentials), R3 (secondary diabetes is not type 2), the study lead's MEAT reading of "addressed", and "unresolved contradiction about CKD or diabetes type → not supported".
- Checks: builder assertions; `study3/check_data.py` (0 of 350 charts with problems; it caught 6 of 6 planted errors); human review of 74 charts in two rounds by the study lead, who used Gemini 3.1 Pro as a reading aid.
- **Dev** 150 charts (81 positive): all 100 follow-up stage-1 charts (results seen), 25 follow-up stage-2 charts, 25 hard cases. **Test** 200 charts (117 positive): 175 follow-up stage-2 charts and 25 hard cases that no model has seen.

## 3. What is frozen

`study3/FREEZE.json` hashes the data, rubric v3, the study-3 runner and data scripts, this file, the pilot harness files it uses (unchanged since the pilot), the follow-up file that holds method C's prompt, and each model's dev-fitted weights, Platt map and thresholds (including C's threshold). The runner refuses the test split if any of them changed, and evaluates test once per model.

Models: `gpt-5.4-2026-03-05` and `gemini-3.8-flash`. Per chart and model: 5 extraction runs, 5 stated-confidence runs, 1 criteria-guided run (11 calls).

## 4. Methods

| | Method | Score |
|---|---|---|
| A | Stated confidence | The model's 0–100 confidence; raw and recalibrated with the dev-fitted Platt map. |
| B | EWC, rubric v3 | Gates G1, G2, R1, R2 must be verified "yes"; then the dev-fitted logistic weights on Q1–Q4 (first extraction run). |
| C | Criteria-guided confidence | The model's 0–100 confidence with rubric-v3 questions and guidance in the prompt; not recalibrated. |

## 5. Hypotheses and pass marks (test split, per model; 95% bootstrap intervals, 2,000 resamples, seed 0)

| ID | Claim | Pass mark |
|---|---|---|
| H1 | B ranks better than A | B AUROC − A AUROC ≥ 0.10, and the lower bound of the paired bootstrap interval > 0 |
| H2 | B ranks better than C | B AUROC − C AUROC > 0, and the lower bound of the paired bootstrap interval > 0 |
| H3 | B is at least as well calibrated as recalibrated A and as C | B ECE ≤ A (recalibrated) ECE and B ECE ≤ C ECE |
| H4 | B's dev-chosen auto-accept threshold transfers | Precision of B at its frozen threshold ≥ 0.95 (with coverage and recall reported) |

Expectation stated in advance from dev: H1 and H3 likely pass for both models; H2 likely passes for GPT-5.4 and likely fails for Gemini 3.8 Flash, where C tied B on dev (AUROC 0.993 against 0.987).

## 6. Also reported (no pass marks)

- Results by family (A–H), including family F (outside the pilot rubric, now covered by R1 and R2) and family H (hard cases).
- Extraction accuracy per question and quote-failure rate (harness report).
- Secondary exploratory views from the same calls: self-consistency (M3), expert weights (M4), no quote verification (M7), two-way answers (M8), and the auto-accept view (threshold, accepted, coverage, precision, recall) for every method at its dev-chosen threshold.

## 7. Analysis rules

- No chart is excluded after results are seen; failed calls are retried, and charts still missing are reported.
- Ambiguous answer fields are reported separately for extraction accuracy.
- Any deviation is logged in `CHANGELOG.md` with its reason and reported.

## 8. Limitations stated in advance

- Synthetic charts from phrase banks; labels follow mostly from facts the rubric asks about, so B is favored by construction. C receives the same questions and guidance to keep the comparison fair.
- The label rules (R1–R3, the MEAT reading, the conflict rule) were set by the study lead with AI assistance, not confirmed by a certified coder.
- Positive rate (about 55%) is far above real populations.
- One reviewer, with an AI reading aid; a Gemini model (3.1 Pro) assisted the review and a Gemini model (3.8 Flash) is tested.
- The charts were generated with Claude, which is not tested.
