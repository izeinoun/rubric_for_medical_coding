# Pilot pre-registration: evidence-weighted confidence on synthetic E11.22 charts

**Status: DRAFT. Review, edit, then freeze before running any extraction.**
To freeze: fill in the date below and commit this file (or record its SHA-256) so later changes are visible.

- Frozen on: Oct 25 11:45 pm EDT ____________
- Frozen by: Issam Zeinoun

## 1. Purpose

Decide privately whether evidence-weighted confidence (EWC) is worth pursuing, changing, or dropping, before any public version of the paper. This pilot tests the mechanics: extraction, quote verification, deterministic scoring, and weight fitting. It does not test real-world performance.

## 2. Data

- 200 synthetic outpatient office-visit notes from `generate_charts.py` v2 (seed 20261024): 88 positive, 112 negative, 13 scenarios.
- Six charts (scenario F1b) are flagged `label_needs_review`. Every headline metric is reported with and without them.
- Candidate code for every chart: **E11.22** (type 2 diabetes mellitus with diabetic chronic kidney disease).
- Ground truth: label 1 if the note supports E11.22 for a risk-adjustment submission, else 0, assigned by construction (see README).
- Split, stratified by scenario: **dev = 140, test = 60**. The split is written into the data file.

**Test-set rule:** test charts are not opened, extracted, or scored until the method, prompts, rubric and weight-fitting procedure are final. They are then run exactly once.

## 3. Known limitation stated up front

Labels are deterministic functions of the documented facts the rubric asks about. With perfect extraction, a fitted rubric should separate the classes almost perfectly. Strong results on this pilot therefore show that extraction and scoring work, not that the method is calibrated on real charts. Real charts (for example MIMIC-IV-Note) are needed for that claim.

The notes were written from phrase banks authored with Claude. To limit same-model advantage, run extraction with at least one non-Claude model and report results per model.

## 4. Methods compared

| ID | Method |
|---|---|
| M1 | Verbalized confidence: the model states a 0–100 confidence that E11.22 is supported |
| M2 | M1 after Platt scaling fitted on dev |
| M3 | Self-consistency: share of 5 sampled yes/no answers that say "supported" |
| M4 | EWC rubric with the expert weights from the paper (Section 5), unfitted |
| M5 | EWC rubric with L2-regularized logistic-regression weights fitted on dev, as specified in Appendix A of the paper (see the fitting procedure below) |
| M6 | Ablation: M5 inputs, but the LLM computes the final score itself |
| M7 | Ablation: M5 without quote verification |
| M8 | Ablation: M5 with two-way answers (not documented merged into no) |

### Quote verification rule (all EWC methods)

- Exact quote check after normalization (case folding, whitespace collapsing). A yes or no answer whose quote is not found becomes not_documented.
- If the failed answer is a gate answer or a no answer, the chart is also flagged `needs_review` and cannot be auto-accepted, whatever its score. Report how many charts this flags.
- No semantic (second-model) verification in this pilot; it is listed as an extension in the paper, not part of the method under test.

### Fitting procedure for M5 (fixed in advance)

- Training charts: dev charts that pass both gates (G1 = yes, G2 = yes) after verification.
- Encoding: two indicators per weighted question (yes, no); not_documented is the reference category.
- Objective: L2-regularized log-loss, intercept unpenalized (scikit-learn `LogisticRegression`, solver `lbfgs`).
- C grid: 13 values, `numpy.logspace(-3, 3, 13)`. Cross-validation: stratified 5-fold, repeated 10 times, `random_state=0`.
- Selection rule: **lowest mean cross-validated log-loss** (choose here; change to the one-standard-error rule only before freezing).
- If the chosen C is at the edge of the grid, extend the grid to 10^6 and report that the indicators separate the classes.
- Refit on all qualifying dev charts with the chosen C; freeze and version the weight table before touching test.
- No prior adjustment for the pilot: train and test share the same prevalence by construction.
- Expected on this pilot: because labels are deterministic functions of the rubric answers, the classes are likely separable. An early check of the code on intended answers (dev only) selected C at the upper grid edge, which is consistent with that.

## 5. Metrics (all on test, with 95% bootstrap confidence intervals, 2,000 resamples)

| Property | Metric |
|---|---|
| Calibration | Expected calibration error (10 equal-width bins), Brier score, reliability diagram |
| Discrimination | AUROC |
| Operational value | Coverage at precision ≥ 0.95 (share of charts auto-accepted at that precision) |
| Decision quality at operating thresholds | **Precision (headline)**, recall and F0.5 at (a) the auto-accept threshold chosen on dev as the lowest score giving precision ≥ 0.95, applied unchanged to test, and (b) a fixed 0.5 threshold. F0.5 weights precision over recall, reflecting the payer's priority on not accepting unsupported codes |
| Reproducibility | Median standard deviation of the score over 5 extraction runs per chart |
| Extraction quality | For each question (G1, G2, Q1–Q4): precision and recall for each answer type (yes, no, not documented), macro-F1, and a confusion matrix against the intended answers. Plain agreement is reported for reference only, because answer types are imbalanced |
| Faithfulness | Share of yes/no answers whose quote fails verification, overall and per question |

With 60 test charts the intervals will be wide. Decisions below use point estimates plus the intervals, and are go/no-go judgments, not claims for publication.

## 6. Hypotheses and decision criteria

| ID | Hypothesis | Pass if |
|---|---|---|
| H1 | Extraction is accurate | Macro-F1 ≥ 0.90 on every question, and recall of "no" answers ≥ 0.90 on every question where "no" occurs |
| H2 | Quotes are faithful | ≤ 5% of yes/no answers fail verification |
| H3 | Deterministic scoring is reproducible | Median score SD over 5 runs ≤ 0.05 for M5, and lower than for M1 |
| H4 | EWC is at least as good as the best confidence baseline | M5 AUROC ≥ M2 AUROC − 0.02 and M5 ECE ≤ M2 ECE |
| H5 | Design choices matter | M5 beats M6, M7 and M8 on ECE or AUROC |

**Kill or rethink criteria** (decided now, not after seeing results):

- If M5 is worse than M2 on both AUROC and ECE, with intervals that do not overlap, EWC does not earn its complexity in this form. Rethink before running more.
- If H1 fails on a gate question (G1 or G2: macro-F1 or "no" recall below 0.90) after rubric and prompt iteration on dev, the extraction approach needs redesign before any calibration claim.
- If H5 fails for every ablation, the paper must not claim that verification, three-way answers or deterministic scoring improve results.

## 7. Iteration policy

- Prompts, rubric wording and the extraction schema may be changed freely, **on dev only**.
- Every version is logged in `CHANGELOG.md` with the date, what changed and why, and its dev metrics.
- The final paper reports how many versions were tried.
- Weights are fitted on dev only. Test is scored once with the final frozen pipeline.
