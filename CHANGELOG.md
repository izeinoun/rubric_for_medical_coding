# Changelog

Log every change to data, rubric, prompts or scoring here, with the date, what changed, why, and dev metrics once extraction runs exist. Test-set results are recorded only once, for the frozen pipeline.

## 2026-10-24 — data v2

No extraction has been run yet; no metrics.

Changes after an independent blind review of 20 v1 charts (all 20 labels agreed):

- Split copy-forward into F1a (current CKD evaluation, label 1) and F1b (stale eGFR, no current evaluation, label 0, flagged `label_needs_review`). v1 labeled every copied-forward chart 1.
- Added N1b (CKD in a bare problem list inside the plan) so that "CKD appears in the plan" no longer implies label 1.
- Added P4 (diabetic cause stated only in the HPI) and moved about 40% of other-cause attributions in N2 to the HPI, so the cause has to be found outside the assessment.
- Widened phrase banks for possible CKD, resolved AKI, other causes, CKD plans and copy-forward markers. Added copy-forward markers and bare problem-list lines to some ordinary charts. Varied the plan heading and section order.
- Defined answer semantics (yes / no / not_documented). G2 for possible CKD and resolved AKI is now "no" (explicitly not established), not "not_documented."
- Clinical fixes: "stable" now matches the eGFR change; the ACE inhibitor or ARB is named; no SGLT2 inhibitor for polycystic kidney disease; albuminuria below 30 mg/g in AKI and possible-CKD charts; no GLP-1 escalation for patients already on semaglutide; type 1 diabetes age at onset made consistent; continuous glucose monitor listed in medications.

## 2026-10-24 — data v1

Initial 200 charts, 10 scenarios. Superseded by v2; not used for any results.

## 2026-10-24 — pre-registration: fitting procedure

- Fixed the M5 weight-fitting procedure in PREREGISTRATION.md to match Appendix A of the paper: reference coding, L2 log-loss with unpenalized intercept, 13-value C grid, repeated stratified 5-fold CV, lowest-log-loss selection, edge-of-grid rule.
- Code check only: ran the reference implementation on dev intended answers to confirm it executes. The chosen C was at the upper grid edge (expected separability). No weights or metrics were inspected; test charts were not touched.

## 2026-10-24 — pre-registration: verification rule

- Added the quote verification rule: failed quotes become not_documented; a failed gate or "no" answer also flags the chart for human review. Semantic verification is explicitly out of scope for the pilot (paper Section 8, extensions).

## 2026-10-24 — harness v1 (prompt version 1, rubric version 1)

- Added `harness/`: providers (Anthropic, OpenAI, Gemini, offline mock), prompts, rubric file, collection with caching, verification, scoring and fitting (Appendix A), baselines M1–M3, ablations M6–M8, metrics with bootstrap intervals, pre-registered checks, report, and a freeze guard that refuses the test split until the pipeline is frozen and unchanged.
- M3 (self-consistency) uses the "supported" field of the 5 verbal-confidence runs instead of 5 separate calls, to save cost. Recorded here as a deviation from the pre-registration wording; same information.
- Tested end to end with the offline mock provider on dev only. Mock results deleted; no real model has been run.

## 2026-10-24 — metrics: precision-first decision metrics, per-class extraction metrics

- Payer focus chosen: decision quality reported as precision (headline), recall and F0.5 at the dev-chosen auto-accept threshold (applied unchanged to test) and at 0.5.
- Extraction quality now per-class precision and recall, macro-F1 and confusion matrices; plain agreement kept for reference only. H1 changed to macro-F1 >= 0.90 and "no" recall >= 0.90 on every question; the gate kill criterion uses the same measures.
- Harness updated to match; retested with the mock provider on dev (results deleted).

## 2026-10-25 — faithfulness reported per question

- Quote-failure rate now reported per question (criterion level) as well as overall, in the harness report and the pre-registration metrics table. Retested with the mock provider on dev (results deleted).

## 2026-10-25 — CLAUDE.md added

- Added project instructions for Claude Code (hard rules: no test split before freeze, no changes to pre-registered parts without approval, logging and versioning of prompt changes, keys from environment only).

## 2026-10-25 — Claude model set to Opus 5.5

- `harness/config.json`: Claude model changed from `claude-sonnet-5-5` to `claude-opus-5-5` (user choice, before any real collection). OpenAI and Gemini model names still to be set.

## 2026-10-26 — OpenAI and Gemini models set; output cap and Gemini token accounting

- `harness/config.json`: OpenAI model `gpt-5.4-2026-03-05` (dated, pinned) and Gemini model `gemini-3.8-flash` (no dated name is offered, so the version cannot be pinned). User choice, before any real collection.
- `max_output_tokens` raised from 4000 to 16000. In test calls on dev charts (not saved to `runs/`), Gemini 3.8 Flash used 400 to 5,300 hidden thinking tokens per extraction call. Thinking counts against the cap, so one call was cut off mid-JSON at 4000. The cap is a ceiling only and does not change answers. GPT-5.4 used 0 reasoning tokens with the default settings.
- `providers.py`: Gemini usage now counts thinking tokens as output tokens, since Google bills them as output and OpenAI's reported output tokens already include reasoning. Before this change, Gemini's reported tokens would have been too low.
- No prompt, rubric, scoring or pre-registered element changed. No metrics yet.

## 2026-10-26 — first full dev run: GPT-5.4 (prompt version 1, rubric version 1)

- Collected 5 extraction and 5 verbal runs on all 140 dev charts; 1,400 calls, 0 errors, 1.32M input and 0.25M output tokens. Evaluated on dev.
- M5 (fitted weights): ECE 0.029, AUROC 0.962, coverage at precision 0.95 = 0.16. M2 (Platt): ECE 0.094, AUROC 0.598. M3: AUROC 0.796. M1 verbal confidence near 0.9–1.0 on every chart (ECE 0.506).
- C = 10 (inside the grid). Quote failures 0; per-chart score SD 0.
- H1 not met: Q2 macro-F1 0.813, Q4 0.574. Most disagreements are the model answering "no" where the answer key says not_documented (Q4 on problem-list-only, labs-only, AKI and uncertain-CKD charts; Q2 on uncertain-CKD charts; Q1 on CKD without a stage). Q4 "yes" on copy-forward-stale (F1b) and laundry-list (N1b) charts is the main source of high scores on label-0 charts.
- No changes made yet; M6 not yet collected.

## 2026-10-26 — rubric v2: no versus not_documented on Q1, Q2, Q4 (dev only)

Plan agreed with the user: finish this pilot as registered (rubric fix on dev, Gemini, freeze, test once), then run a harder follow-up study under its own pre-registration.

Why: in the GPT-5.4 dev run (prompt v1, rubric v1), H1 failed because the model answered "no" where the answer key says not_documented. Q4 macro-F1 0.574 (23 of 25 scored not_documented answers given as "no": problem-list-only, labs-only, AKI and uncertain-CKD charts); Q2 macro-F1 0.813 (10 uncertain-CKD charts with the latest eGFR below 60 but only one low result, answered "no"); Q1 macro-F1 0.971 (5 CKD-without-stage charts answered "no"). The key never uses "no" for Q1 or Q4, and uses it for Q2 only when the latest eGFR is 60 or above; the v1 guidance did not say so.

What changed (`rubric_e1122.json`, version 1 → 2; guidance text only, question text unchanged):
- Q1: an unstated stage is not_documented, not no.
- Q2: yes, no and not_documented spelled out to match the key; "no" only when the latest eGFR is 60 or above.
- Q4: CKD not addressed at this visit is not_documented, not no. Added "a list of diagnoses (including a line saying the problem list was reviewed)" to the cases that do not count; this targets the N1b laundry-list errors and restates the existing rule.
- No change to prompts, answer key, labels, scoring, metrics or the fitting procedure. The copy-forward-stale (F1b) Q4 errors were left alone: those charts are already flagged ambiguous and label_needs_review.
- Archived the v1 run to `harness/runs/archive/gpt_prompt1_rubric1/` (dev results and the weights fitted on them).

## 2026-10-26 — GPT rubric-v2 dev collection interrupted (OpenAI credits exhausted)

- The re-collection stopped when the OpenAI account ran out of credits: 556 of 700 extraction responses saved (113 charts with at least one run), 139 errors (HTTP 429 insufficient_quota), 0 verbal runs. Rerunning `collect` retries only the failed calls. No evaluation yet.
- Preview on the 556 chart-runs collected under both versions (not a report; the 5 remaining dev scenarios are not all covered): Q1 errors 14 → 0, Q3 5 → 0, Q4 (unambiguous fields) 94 → 1, N1b laundry-list Q4 "yes" 15 → 0. Q2 unchanged: 37 "no" where the key says not_documented (all N5, latest eGFR below 60 with only one low result; the model's rationale states the not_documented case but it still answers "no"), plus 6 new "not_documented" where the key says yes (N3; for example 2026-01-17 to 2026-04-28, 101 days, judged under 90 days — a date-arithmetic error).
