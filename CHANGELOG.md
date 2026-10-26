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

## 2026-10-26 — OpenAI model set to gpt-5.5-2026-04-23

- `harness/config.json`: OpenAI model set to `gpt-5.5-2026-04-23` (chosen by Claude at the user's request: newest flagship with a dated snapshot, so it cannot change during the pilot; `-pro` variants are several times the cost; undated `gpt-5.6-*`/`gpt-6-*` names avoided).
- One test extraction call on dev chart SYN-0002 (output not saved under `harness/runs`): 1,212 input tokens, 759 output tokens (516 hidden reasoning, 243 visible), valid JSON. No real collection yet. Gemini model still to be set.

## 2026-10-26 — Gemini model set to gemini-3.1-pro-preview

- `harness/config.json`: Gemini model set to `gemini-3.1-pro-preview` (strongest pinned Gemini model on the key; `-latest` aliases avoided because they move). Required enabling paid API billing; the free tier has no quota for it.
- One test extraction call on dev chart SYN-0002 (output not saved under `harness/runs`): 1,287 input tokens, 341 visible output, 685 hidden thinking, valid JSON. An earlier test of `gemini-3.8-flash` spent 3,836 of the 4,000-token output limit on thinking and returned truncated JSON. No real collection yet.
