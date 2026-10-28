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

## 2026-10-27 — Gemini 3.8 Flash dev run (prompt version 1, rubric version 2)

- Collected 5 extraction and 5 verbal runs on all 140 dev charts: 1,400 calls, 0 errors, 0 unparseable; 1.48M input and 1.34M output tokens (output includes thinking; largest single call about 10,100 tokens). Evaluated on dev.
- Extraction: H1 met. Macro-F1 1.000 on G1, G2, Q1, Q2, Q3; Q4 0.987 (one miss: SYN-0055, P4, plan line about eGFR and losartan without the word CKD; Q4 "yes" on 1 of 5 runs). Ambiguous Q4 fields: agreement 0.621.
- M5: ECE 0.008, AUROC 0.999, coverage at precision 0.95 = 0.45 (threshold 0.183). M2: ECE 0.082, AUROC 0.698. M3: ECE 0.089, AUROC 0.936. M4 (expert weights): ECE 0.152, AUROC 0.983. C = 31.6, inside the grid. Quote failures 0; per-chart score SD 0.
- M7 identical to M5 (no quote failures). M6 not yet collected. Kill criteria not triggered.

## 2026-10-27 — Gemini M6 (dev)

- Collected M6 (model computes the score from the dev-fitted M5 weights): 140 calls, 0 errors. Re-evaluated on dev.
- M6: ECE 0.0084, AUROC 0.9995, coverage 0.44. M5: ECE 0.0080, AUROC 0.9987, coverage 0.45. H5 for M6 reads True only because M5's ECE is lower by 0.0004, far inside the bootstrap intervals; M5 and M6 are practically indistinguishable on these charts.

## 2026-10-27 — GPT-5.4 dev run completed under rubric v2 (prompt version 1)

- Retried the 144 extraction calls that failed for lack of credits, then 700 verbal calls: 0 errors. Total 1.39M input and 0.24M output tokens. Evaluated on dev.
- Extraction: Q1 macro-F1 0.971 → 1.000, Q4 0.574 → 1.000, Q3 0.971 → 0.985; Q2 0.813 → 0.827 (still fails H1: "no" where the key says not_documented on N5 charts, and some 90-day date-arithmetic errors). Gates 1.000.
- M5: ECE 0.047, AUROC 0.969, coverage at precision 0.95 = 0.14. M2: ECE 0.048, AUROC 0.571. H4 passes on ECE by 0.001 only. Excluding label_needs_review charts: M5 ECE 0.033, AUROC 1.000, coverage 0.48.
- The four F1b copy-forward-stale charts (label 0, label_needs_review) score 0.95–0.99 because GPT answers Q4 "yes"; they are the only label-0 charts above 0.02 and set the 95%-precision threshold.
- C = 100 (inside the grid, one step from the edge).

## 2026-10-27 — GPT M6 (dev)

- Collected M6 for GPT: 140 calls, 0 errors. Re-evaluated on dev.
- M6: ECE 0.176, AUROC 0.965, coverage 0.23. M5: ECE 0.047, AUROC 0.969, coverage 0.14. When GPT computes the score itself, ranking is about the same but calibration is much worse; H5 for M6 is met on ECE.

## 2026-10-27 — pipeline frozen

- User decisions: keep Q2 as in rubric v2 (GPT's Q2 failure is reported as a finding; Gemini scores 1.000 on Q2 under the same wording); no further prompt or rubric changes.
- Ran `python run_pilot.py freeze` at 2026-10-27T02:16:28. `FREEZE.json` SHA-256: e8619565765170cf00776b61628a588f75dfb8214f070706aa06dee6f9cf64fd.
- Frozen: PREREGISTRATION.md, prompts (version 1), rubric (version 2), harness code, config (gpt-5.4-2026-03-05, gemini-3.8-flash), data, and the dev-fitted weights, Platt maps and thresholds for GPT and Gemini.
- Test split not yet opened. It will be run once per model only when the user says so.

## 2026-10-27 — test split: collected and evaluated once per model (frozen pipeline)

- Checked before evaluating: `FREEZE.json` committed at 02:16:36 UTC (aa1e8c8); first test call 02:17:21. All frozen hashes unchanged before and after evaluation. Every test record carries prompt version 1, rubric version 2 and the frozen model name. Test evaluation reads the dev-fitted weights, Platt maps and thresholds; nothing was refitted.
- Collection: per model 300 extraction, 300 verbal and 60 M6 calls, 0 errors, 0 unparseable. Each model evaluated once (`TEST_DONE_gpt.json`, `TEST_DONE_gemini.json`).
- GPT-5.4: H1 fails (Q2 macro-F1 0.759; all other questions 1.000). M5 ECE 0.009, AUROC 0.969; M2 ECE 0.107, AUROC 0.571. At the dev threshold M5 accepts 10 charts (coverage 0.17) with precision 0.90 (below the 0.95 target). H2–H4 met; H5 met for M6 and M8, not M7. No kill criterion.
- Gemini 3.8 Flash: H1 met (all questions 1.000). M5 ECE 0.016, AUROC 0.979; M2 ECE 0.120, AUROC 0.669. At the dev threshold M5 accepts 27 charts (coverage 0.45) with precision 0.963 and recall 1.000. H2–H4 met; H5 met for M6 (AUROC higher by 0.0006 only, a tie in practice) and M8, not M7. No kill criterion.
- The only high-scoring label-0 chart for both models, and the only wrongly accepted chart, is SYN-0182 (F1b copy-forward stale, label_needs_review). Excluding the two label_needs_review test charts, M5 AUROC is 1.000 for both models.
- M7 equals M5 for both models: no quote failed verification on test, so the quote-verification ablation is untested in this pilot.

## 2026-10-27 — follow-up study: draft spec

- Added `followup/SPEC.md`: a draft design for a harder follow-up study (new scenario families, outside-rubric charts, quote-stress formatting, a criteria-informed confidence baseline M9, 400 charts, draft hypotheses H6–H10). Nothing generated or run; the pilot's data and frozen pipeline are unchanged.

## 2026-10-27 — follow-up spec revised: transfer test

- User decisions: transfer test only (frozen pilot pipeline applied unchanged to new, harder charts, all test, no dev or refitting); GPT-5.4 and Gemini 3.8 Flash; family F reported separately as a stress test; new label rules limited to those GPT-5.4 and Gemini both rated high-confidence and agreed on; larger cost acceptable.
- Asked GPT-5.4 and Gemini (one call each, 2026-10-27) for risk-adjustment rules the rubric does not capture; responses saved in `followup/rule_suggestions/`. Agreed high-confidence rules adopted for labels only: acceptable face-to-face encounter and provider (R1), valid signature with credentials (R2), secondary diabetes is not type 2 (R3). The rubric is not changed.
- `followup/SPEC.md` rewritten for the transfer design: 340 main charts plus 60 stress-test charts, M9 reported raw (no dev to fit Platt), hypotheses H6–H10 adjusted. Nothing generated or run.
- Same day: follow-up trimmed to 300 charts (255 main, 45 stress test) at the user's request; per-family counts and call estimates updated (16 calls per chart with M9, 4,800 per model).

## 2026-10-27 — follow-up: chart generator v3, data, checks and label-review sheet

- Added `followup/generate_charts_v3.py` (imports the pilot's phrase banks; the pilot generator and data are unchanged). 300 charts, all test: 255 main (families A–E, G; 129 positive, 51%) and 45 stress-test charts (family F, all label 0). Seed 20261027; `followup/data/charts.jsonl` SHA-256 ba93d3aa60fa44c7ec15a1f9a04da0afee5ec38f0e752cafb412ed0b2428aedb. Median note length 3,374 characters (pilot about 2,000); 133 charts (44%) have format stress.
- Labels come from a fact sheet using the pilot rule plus R1–R3; intended answers follow the frozen rubric v2. The generator asserts, for every chart, that the label matches the scenario and that the pilot's rubric-based label rule agrees (families A–E, G) or would wrongly say 1 (family F).
- Added `followup/check_charts_v3.py`: independent checks that read only the note text (diabetes-type, stage, cause, signature, provider and encounter wording; eGFR dates and values; Q2 recomputed from the text). Result: 0 of 300 charts with problems. The checker caught all 7 deliberately planted errors.
- Bugs found and fixed while building: family-history line "Mother: hypertension, type 2 diabetes" put "type 2" into type-1, untyped and secondary-diabetes charts (now "Mother: hypertension."); C2 (type 2 on insulin) was labeled 0; "today" in copy-forward plan lines did not match the lab date; contradictory smoking history; creatinine not tracking eGFR; nurse and dietitian notes changing medications; e-consult notes implying the patient was seen; duplicate health-maintenance sentences.
- Spec changes made while building: F3 is a chart-review e-consult (patient not seen) instead of a stand-alone lab report, which the rubric itself would already score 0; notes are about 1.7 times the pilot's length instead of 2–3 times.
- Added `followup/make_review_sheet.py` and `followup/review/` (40 charts, stratified by family, for the user's label review before the freeze).
- No model calls.

## 2026-10-27 — follow-up: staged test, runner, pre-registration draft, new review sheet

- User decisions: run OpenAI and Gemini only (a claude.ai subscription gives no API access); start with a smaller set for a sanity and directional check. Agreed design: a staged one-shot test. Stage 1 = 100 pre-selected charts (85 main in proportion to each scenario, 15 stress test), seed 101, listed in `followup/stage1_ids.txt`; stage 2 = the other 200 with nothing changed, unless a pre-registered technical go/no-go check fails. M9 cut to 1 run per chart.
- Added `followup/run_transfer.py`: imports the frozen harness without editing it, checks the pilot freeze hashes (including each model's weights) and the follow-up freeze before every call, copies the frozen weights, adds M9, paired bootstrap AUROC tests, family breakdown, the family-F stress test and the technical checks; refuses a second evaluation per model and stage. Tested end to end with the offline mock model in scratch space (results not kept); guards confirmed to refuse a real run before the freeze, `--no-freeze-check` with a real model, and mock output inside the repository.
- `estimate` on the real charts: about 1,200 calls and 1.6M input tokens per model for stage 1, 2,400 calls and 3.1M for stage 2 (plus output and Gemini thinking tokens), lower than the earlier rough estimate.
- Added `followup/PREREGISTRATION.md` (draft until the follow-up freeze), including a reminder that adding R1–R3 to the rubric (rubric v3) is a separate later study.
- Review sheet redrawn from the stage-1 charts (40 of the 100). No model calls.

## 2026-10-27 — follow-up simplified to three methods

- At the user's request the follow-up compares three methods only: A, the model's stated confidence (raw, and recalibrated with the frozen pilot map); B, EWC (frozen pilot M5); C, criteria-guided confidence (the rubric's questions in the prompt, with the model told to answer each criterion for itself and base its confidence on them).
- An exploratory rule-gate arm (M10: B set to 0 unless R1–R3 pass) was built, tested with the mock model, and dropped the same day to keep the design simple; noted as a possible next study. M6 is no longer collected.
- C's prompt (formerly "consider the criteria") now explicitly tells the model to use the criteria for its confidence.
- Pre-registration hypotheses rewritten around the comparison: H1 B vs A ranking (≥ 0.10 AUROC, paired interval above 0), H2 B vs C ranking (paired interval above 0), H3 B vs recalibrated A calibration, H4 frozen threshold precision, H5 family-F stress test.
- Per chart and model: 11 calls (5 extraction, 5 verbal, 1 for C). `estimate`: stage 1 about 1,100 calls and 1.4M input tokens per model; stage 2 about 2,200 calls and 2.8M. Mock test end to end (results not kept). No model calls.
- Same day: added an interactive review page (`followup/review/label_review.html`, built by `followup/make_review_page.py`, published as a private claude.ai artifact) because the Markdown sheet did not open in the app. Verdicts save to the artifact's database for Claude to read.

## 2026-10-27 — follow-up: human label review recorded; contested labels flagged

- Human review of 40 stage-1 charts by the study lead, with Gemini 3.1 Pro as a reading aid: 34 agree, 6 disagree (verdicts and notes in the review page's database).
- Five disagreements (FU-0031, FU-0093, FU-0300 in B2; FU-0129 in B4; FU-0002 in G4): the reviewer counts copy-forward lines with "continue regimen" or "stable", and a reviewed-problems list, as CKD addressed (MEAT); the generator follows the frozen rubric's rule that they are not. Decision: flag all 37 charts in B2, B4 and G4 `label_needs_review`, keep their labels at 0, exclude them from the primary analysis and report a sensitivity analysis with them labeled 0 and 1. The generator change adds flags only; chart texts and labels are unchanged (new data SHA-256 689770cb9b688a8f7c8cffc6e36a35b2245d0068fa1c7555f9c7b37bc0e0105b).
- One disagreement (FU-0049, E1, "CKD due to type 2 diabetes and hypertension"): the reviewer labeled 0 because a non-diabetic cause is named. Label kept at 1 (coding guidance supports E11.22 when diabetes is one of the causes). The review page's rule wording ("no non-diabetic cause is given") was misleading; corrected to "a different cause instead of diabetes".
- Runner: primary analysis set = uncontested main-set charts (218 over all 300; 73 in stage 1, 41 positive); sensitivity section added. Pre-registration and spec updated. Mock test end to end (results not kept). No model calls.

## 2026-10-27 — follow-up frozen

- Ran `python followup/run_transfer.py freeze` at 2026-10-27T21:42:28 (user approval). `followup/FREEZE.json` SHA-256 3e0bf8a1a1008ebf09b143c1b102a78762b211d9a6a57de5e22b66cd7a563fc6; it records the pilot freeze (e8619565…) and hashes the follow-up data, stage-1 list, runner (with the method C prompt), generator, checker and pre-registration. Independent checks before freezing: 0 of 300 charts with problems.
- Test calls after the freeze (one median-length stage-1 chart, 3,399 characters; extraction, method A and method C prompts; answers neither shown nor saved): all six parsed. GPT-5.4 input/output tokens: extraction 1,683/417, A 1,087/15, C 1,544/13. Gemini 3.8 Flash (output includes thinking): extraction 1,785/1,095, A 1,169/314, C 1,639/2,146. Projected stage 1 per model: GPT about 1.54M input and 0.22M output; Gemini about 1.64M input and 0.92M output.

## 2026-10-27 — follow-up stage 1 collected and evaluated (frozen pipeline)

- Both models: 1,100 calls each, 0 errors, 0 unparseable, 0 quote failures. Tokens: GPT 1.55M input / 0.17M output; Gemini 1.67M input / 1.24M output (output includes thinking). All four pre-registered go/no-go checks pass for both models, so stage 2 runs unchanged.
- Primary analysis set (73 uncontested main-set charts, 41 positive), AUROC: GPT A 0.470, B 0.932, C 0.441; B − A 0.462 (0.317 to 0.608); B − C 0.491 (0.348 to 0.645). Gemini A 0.731, B 0.979, C 0.961; B − A 0.248 (0.130 to 0.381); B − C 0.018 (−0.018 to 0.058). ECE: GPT A recalibrated 0.133, B 0.068; Gemini A recalibrated 0.185, B 0.031.
- Frozen auto-accept threshold for B: GPT 13 charts accepted, precision 0.923 (wrong: FU-0105, steroid-induced diabetes read as type 2); Gemini 42 accepted (coverage 0.58), precision 0.952 (wrong: FU-0055, FU-0223, "see nephrology note" read as CKD addressed).
- Main error sources for B: G2 "see nephrology note" read as addressed (GPT 5 charts, Gemini 2); G3 metformin reduced for eGFR not read as addressed (GPT 2, Gemini 1).
- Stress test (family F, 15 charts): mean B 0.94 (GPT) and 0.99 (Gemini); B would auto-accept 40% (GPT) and 100% (Gemini). Mean C: GPT 0.96, Gemini 0.72.
- Contested charts, sensitivity: B − A stays large under both labelings (GPT 0.41 and 0.43; Gemini 0.27 and 0.21).

## 2026-10-27 — follow-up stopped after stage 1; study 3 planned

- Study lead's decisions: stop the follow-up after stage 1 (allowed by its pre-registration; reported as directional), keeping the 200 stage-2 charts unseen; start study 3 with rubric v3 on 350 charts (300 existing plus 50 new hard cases), dev 150 / test 200, with the stage-1 charts in dev; adopt the study lead's MEAT reading of "addressed" (copy-forward "continue regimen" or "stable", and a reviewed chronic-conditions list, count).
- Added `followup/STATUS.md` (frozen follow-up files left unchanged) and `study3/SPEC.md` (one-page plan). Nothing built or run.

## 2026-10-27 — study 3: data built (350 charts) and review page

- Study lead confirmed the remaining label rules: a reviewed problem list in the plan (A_N1b) counts as addressed, like the reviewed chronic-conditions list (G4); the current assessment and plan governs conflicting sections; a documented stage counts even when labs disagree; ESRD on dialysis supports E11.22; "CKD?" is not established; "see nephrology note" alone is not addressed; a medication change made because of kidney function is.
- Added `study3/build_data.py`: the 300 follow-up charts with texts unchanged, relabeled under the study-3 rules (42 charts change from 0 to 1: B2, B4, G4, A_N1b), with intended answers for the new gates R1 and R2; plus 50 hard cases in 13 scenarios (conflicting statements; stage against labs; ESRD and dialysis; unclear or partial statements), built with the unchanged follow-up generator and recorded edits, with format noise applied after the edits. Splits: dev 150 (all 100 stage-1 charts, 25 stage-2 charts stratified by family, 25 hard cases) and test 200 (175 never-run stage-2 charts, 25 hard cases). `study3/data/charts.jsonl` SHA-256 07cca837552617424ec7bc8016957f1c1f8ab23ba1cdf54f4a9a93749fbbb7be.
- Added `study3/check_data.py`: follow-up checks on the 300 (plus unchanged text and expected labels) and scenario checks on the hard cases (defining wording in the right section, stage wording, Q2 recomputed from the text, R1/R2, exact evidence). Result: 0 of 350 charts with problems; it caught 6 of 6 planted errors in hard cases.
- Review page for the study lead (34 charts: two per hard scenario and two per relabeled scenario), published as a private artifact. No model calls.

## 2026-10-28 — study 3: conflict labels, rubric v3, runner

- From the study lead's review of 34 study-3 charts (31 agree, 3 disagree; notes drafted with Gemini 3.1 Pro and endorsed by the study lead): a contradiction about whether CKD exists, or about the diabetes type, that the note does not resolve is not supported (it needs a provider query); a contradiction only about the stage still supports E11.22. Relabeled all H1a (HPI "no history of kidney disease") and H1c (type 1 in outside records, type 2 in the plan) charts to 0, 7 charts, with G2 and G1 answers "no". All 8 sampled relabeled copy-forward and list charts were confirmed. The doubled wording "stage 5, not on dialysis not on dialysis" in 3 H3c charts is kept deliberately, at the study lead's request, to see whether it confuses the models. New data SHA-256 1e36b6256b2650f6c9f3c2b5dbafbf4570cb0abdae47b47ac1612d04bf701966; dev 150 (81 positive), test 200 (117 positive).
- Added `study3/rubric_e1122_v3.json` (version 3): gates G1, G2, R1 (face-to-face with an acceptable provider), R2 (signed with credentials); G1 guidance adds secondary diabetes and unresolved type 1/type 2 conflicts; G2 guidance spells out established, not established and unclear wording, plan-over-problem-list deferral and unresolved denials; Q1 counts a stated stage even when sections or labs disagree; Q3 counts diabetes named with another cause; Q4 follows the study lead's MEAT reading, anchored on the assessment and plan ("see nephrology note" alone is not addressed; a medication change for kidney function is). Holistic arguments from labs and medications outside the assessment and plan were deliberately not adopted, because they would make problem-list-only charts "addressed", contrary to the agreed labels. Method C receives the same questions and guidance.
- Added `study3/run_study3.py`: the pilot harness unchanged, pointed at the study-3 data, rubric v3 and `study3/runs/`; method C from the follow-up code; dev fitting; a study-3 freeze and a one-evaluation guard for test (kept in `study3/`, apart from the pilot's). Mock test end to end (results not kept). `estimate`: dev about 1,650 calls and 2.5M input tokens per model; test about 2,200 calls and 3.4M.
- Test calls before the dev run (dev chart FU-0152, 3,375 characters; all parsed; extraction returned all 8 answers). GPT-5.4 input/output tokens: extraction 2,151/403, A 1,151/15, C 1,996/15. Gemini 3.8 Flash (output includes thinking): extraction 2,303/1,607, A 1,273/192, C 2,137/301. Projected dev per model: GPT about 2.8M input and 0.3M output; Gemini about 3.0M input and 1.4M output.

## 2026-10-28 — study 3 dev run (rubric v3), both models

- Collection: GPT 1,650 calls, 0 errors. Gemini: 156 extraction and 31 verbal calls failed when the prepayment credit ran out (HTTP 402); the study lead added credit and the second pass retried them, 0 errors remaining. Evaluated on dev (weights, Platt map and thresholds fitted on dev; B and recalibrated A are out-of-fold).
- GPT-5.4 dev AUROC: A 0.542 (recalibrated; raw 0.451), B 0.919, C 0.463. B − A 0.377 (0.266 to 0.479); B − C 0.457 (0.358 to 0.561). ECE: A recalibrated 0.061, B 0.051, C 0.422. Family F (outside the old rubric): B wrong on 0 of 19 (the new gates work); C wrong on 19 of 19. Main B errors: "see nephrology note" read as addressed (6 G2 charts) despite the new guidance; unresolved contradictions (H1a ×2, H1c) not applied; ESRD on the problem list only (1). R1/R2 extraction: GPT answers R1 "no" for unsigned notes and R2 "no" for RN/RD signatures (rules merged); the gate still fails correctly, so labels are unaffected.
- Gemini 3.8 Flash dev AUROC: A 0.676 (recalibrated; raw 0.695), B 0.987, C 0.993. B − A 0.310 (0.225 to 0.401); B − C −0.006 (−0.024 to 0.008). ECE: A recalibrated 0.047, B 0.013, C 0.029. Extraction macro-F1 1.000 on every question except R1 (0.998). Only B errors: two N2 (other cause) charts scored 0.999 out-of-fold, because "other cause" answers are rare in dev and each held-out fold can lack them (C = 316, near the grid edge).

## 2026-10-28 — study 3: secondary views added, pre-registration, freeze

- Study lead's decisions: freeze rubric v3 without another dev round; add the extra views that need no extra calls. The study-3 report now also gives self-consistency (M3), expert weights (M4), no quote verification (M7), two-way answers (M8) as secondary exploratory views, and an auto-accept view for every method at a dev-chosen 95%-precision threshold. Method C's threshold is now chosen on dev the same way and stored with the frozen weights (`C_threshold.json`; GPT: none reaches 95% precision; Gemini: 0.85). M6 not added (extra calls; stage 1 already answered it).
- Added `study3/PREREGISTRATION.md`: H1 B vs A ranking (≥ 0.10, paired interval above 0), H2 B vs C ranking (paired interval above 0), H3 B calibration ≤ recalibrated A and ≤ C, H4 B precision ≥ 0.95 at its frozen threshold. Expectation stated in advance: H2 likely fails for Gemini (tie on dev).
- Ran `python study3/run_study3.py freeze` at 2026-10-28T02:59:32; `study3/FREEZE.json` SHA-256 4b8092db4ba6cbf7bcba56e46e90d80e881b7cead10be2ebc3f6a9e2cfc672f6.

## 2026-10-28 — study 3 test run started; Claude Sonnet 5.5 addendum planned

- Study lead said "run the test". Freeze check passed; test collection started for GPT-5.4 and Gemini 3.8 Flash (200 charts each).
- Added `study3/ADDENDUM_CLAUDE_SONNET.md` before any Claude call: Claude Sonnet 5.5 (study lead's choice over Opus 5.5) as a third model, with its own dev fit, addendum freeze and single test run; same-model risk stated; needs an Anthropic API key.
- Planned after the test, as exploratory analyses that read results only: a chart-by-chart side-by-side page of the methods' scores, and DeLong z-tests for paired AUROC differences.

## 2026-10-28 — study 3 test: GPT-5.4 evaluated; Gemini paused (credit)

- GPT-5.4: 2,200 calls, 0 errors; evaluated once. AUROC A 0.593 (recalibrated; raw 0.407), B 0.926, C 0.483. B − A 0.333 (0.243 to 0.417); B − C 0.443 (0.352 to 0.530). ECE A recalibrated 0.046, B 0.037, C 0.368. B at its frozen threshold: 46 charts accepted (coverage 0.23), precision 0.935, recall 0.368. Pre-registered checks: H1 pass, H2 pass, H3 pass, H4 fail (0.935 < 0.95). Family F (outside the pilot rubric): B wrong on 0 of 26, C on 25 of 26.
- Gemini 3.8 Flash: extraction complete (1,000 calls); 281 of 1,000 stated-confidence calls and the criteria-guided calls failed when the prepayment credit ran out (HTTP 402). Collection stopped; to be resumed (failed calls only) after the credit is topped up. Not evaluated.
- Anthropic key not visible in this session (a test request to api.anthropic.com returned 401); most likely added after the session started. Added `study3/HANDOFF_SONNET.md` so a new session (with the key as `ANTHROPIC_API_KEY`) can run the Sonnet addendum; it notes that `ANTHROPIC_BASE_URL` must point to https://api.anthropic.com for the runner.
- 2026-10-28: the study lead shared a screenshot of the environment settings that showed all three API keys in full; advised rotating all three and storing the new keys as network secrets. The keys in the screenshot were not used. The environment reserves `ANTHROPIC_API_KEY` for Claude Code's sign-in (it is not passed to sessions), which explains the 401. Handoff note updated: the remaining Gemini test calls and the Sonnet addendum move to a new session.

## 2026-10-28 — Claude Sonnet 5.5 addendum: runner, test calls, dev run started

- The study lead supplied a new Anthropic key for this run only, to be deleted afterwards; it is passed as an environment variable to the run's processes only (never written to a file or committed). `ANTHROPIC_BASE_URL` set to https://api.anthropic.com for those processes.
- Added `study3/run_addendum_sonnet.py`: the frozen study-3 runner unchanged, with the "claude" model overridden in memory to `claude-sonnet-5-5`; requires the study-3 freeze to be unchanged; an addendum freeze (`study3/FREEZE_CLAUDE.json`) of the Sonnet weights before test; test evaluated once.
- Test calls (dev chart FU-0152; all parsed; extraction returned 8 answers): input/output tokens: extraction 3,386/1,144, A 1,888/17, C 3,176/17. Projected: dev about 4.4M input and 0.9M output (about $18), test about 5.9M and 1.2M (about $23).
- Sonnet dev: 1,650 calls, 0 errors. Dev evaluation, the addendum freeze and the test collection were chained in one command that ran in the background by mistake, while the dev evaluation was also rerun by hand; the fitting is deterministic and all 9 files hashed in `study3/FREEZE_CLAUDE.json` (frozen 2026-10-28T12:37:19) match the files on disk, so the weights used on test are the dev fit. Sonnet dev AUROC: A 0.707 (recalibrated), B 0.977, C 0.995; B − A 0.270 (0.172 to 0.369); B − C −0.018 (−0.051 to 0.003). ECE: A recalibrated 0.100, B 0.029, C 0.086. Test collection running.
- Sonnet test: 2,200 calls, 0 errors; evaluated once. AUROC A 0.715, B 0.987, C 0.995; B − A 0.272 (0.193 to 0.360); B − C −0.008 (−0.025 to 0.003). ECE A recalibrated 0.067, B 0.021, C 0.090. B at its frozen threshold: 119 accepted (coverage 0.59), precision 0.966, recall 0.983. Pre-registered checks (addendum): H1 pass, H2 fail (tie with C), H3 pass, H4 pass. Family F: B and C wrong on 0 of 26. Same-model caveat applies (charts written with Claude).
- The Anthropic key supplied for this run should now be deleted by the study lead; it was used only as a process environment variable and appears in no file.

## 2026-10-28 — Claude Haiku 5.5 addendum

- Study lead approved a Haiku 5.5 addendum (`study3/ADDENDUM_CLAUDE_HAIKU.md`, written before any Haiku call), same procedure as Sonnet, own model key `claude_haiku`. Runner `study3/run_addendum_haiku.py` (copy of the Sonnet runner).
- Test calls (dev chart FU-0152): input/output tokens extraction 3,386/1,507, A 1,888/164, C 3,176/123. One of three extraction attempts on that chart failed to parse: Haiku put a raw control character inside a JSON string. Declared in the addendum before any dev call: for Haiku only, such responses are parsed again with `strict=False`; frozen files and other models unaffected.
- Haiku dev: 1,650 calls, 0 errors, 0 unparseable after the declared tolerant parse. Dev AUROC: A 0.836 (recalibrated), B 0.992, C 0.940; B − A 0.155 (0.085 to 0.232); B − C 0.052 (0.014 to 0.100). ECE: A recalibrated 0.072, B 0.019, C 0.233. Addendum frozen: `study3/FREEZE_CLAUDE_HAIKU.json` SHA-256 3fce64cf21fbb185a14e57002ad25d7e3eabade57ce6205ff667af78ce3ca6bf. Test collection started.
- Haiku test: 2,200 calls, 0 errors; evaluated once. AUROC A 0.772, B 0.994, C 0.917; B − A 0.222 (0.147 to 0.305); B − C 0.077 (0.031 to 0.131). ECE A recalibrated 0.111, B 0.014, C 0.234. B at its frozen threshold: 120 accepted (coverage 0.60), precision 0.967, recall 0.991. Pre-registered checks (addendum): H1, H2, H3 and H4 all pass. Family F: B wrong on 0 of 26. Family G (borderline): B wrong on 0 of 39, C on 19.
- Actual cost of dev plus test from recorded tokens at list prices: Sonnet 5.5 10.37M input / 2.31M output, about $43.82; Haiku 5.5 10.10M input / 3.62M output, about $2.82.
- Claude runs finished; the study lead can delete the Anthropic key used for them.

## 2026-10-28 — Gemini 3.8 Flash test resumed; Gemini 3.5 Flash-Lite addendum

- The study lead bought Gemini credit. Resumed the Gemini 3.8 Flash test collection (failed calls only).
- Study lead approved a Flash-Lite dev run. Added `study3/ADDENDUM_GEMINI_FLASH_LITE.md` (written before any Flash-Lite call; the Haiku tolerant JSON parse declared in advance) and `study3/run_addendum_gemini_lite.py` (model key `gemini_lite`, model `gemini-3.5-flash-lite`).
- Test calls (dev chart FU-0152; all parsed; extraction returned 8 answers): input/output tokens extraction 2,303/512, A 1,273/11, C 2,137/17; no thinking tokens (Flash-Lite does not think by default). Projected dev: about 3.0M input and 0.4M output tokens.
- Gemini 3.8 Flash test completed (failed calls retried, 0 errors) and evaluated once. AUROC A 0.647, B 1.000, C 1.000; B − A 0.353 (0.280 to 0.434); B − C 0.000. ECE A recalibrated 0.108, B 0.002, C 0.036. B at its frozen threshold: 122 accepted (coverage 0.61), precision 0.959, recall 1.000. Pre-registered checks: H1 pass, H2 fail (tie), H3 pass, H4 pass.
- Flash-Lite dev: 1,650 calls, 0 errors; evaluated on dev. AUROC A 0.711 (recalibrated), B 0.911, C 0.773; B − A 0.200 (0.106 to 0.304); B − C 0.138 (0.068 to 0.206). ECE A recalibrated 0.085, B 0.025, C 0.212. Not yet frozen; test awaits the study lead's go.
- Study lead said "run the Flash-Lite test". Addendum frozen: `study3/FREEZE_GEMINI_LITE.json` SHA-256 bba9e6e3f85df7647ad01a26e889b467dd78b1e5d66f0b2b7bfbc64e8386f69d. Test collection started.
- Flash-Lite test: 2,200 calls, 0 errors; evaluated once. AUROC A 0.692, B 0.897, C 0.779; B − A 0.205 (0.126 to 0.282); B − C 0.119 (0.055 to 0.185). ECE A recalibrated 0.076, B 0.050, C 0.246. No dev threshold reached 95% precision, so B auto-accepts nothing. Pre-registered checks (addendum): H1 pass, H2 pass, H3 pass, H4 fail (no threshold). Weakest family: G (borderline), B AUROC 0.456, 11 wrong at 0.5. Tokens dev+test: 6.76M input, 0.98M output (no thinking); Gemini 3.8 Flash for comparison: 6.72M input, 4.06M output.

## 2026-10-28 — exploratory: precision, recall and F0.5 (study 3 test)

- Added `study3/analysis/decision_metrics.py` and its output `study3/analysis/decision_metrics.md`: precision, recall and F0.5 for A (recalibrated), B and C on the study-3 test split, at 0.5 and at each method's frozen dev-chosen threshold, for all five models. Reads frozen results only; exploratory, not part of the pre-registered checks. F0.5 at 0.5 for B: GPT 0.888, Sonnet 0.976, Haiku 0.978, Gemini 3.8 Flash 1.000, Flash-Lite 0.902; for A: 0.620, 0.764, 0.827, 0.713, 0.706.

## 2026-10-28 — exploratory: does high confidence mean high accuracy? (study 3 test)

- Added `study3/analysis/calibration_table.py` and its output `study3/analysis/calibration_table.md`: for each model and method (A stated, A recalibrated, B, C), test charts grouped by confidence (under 10%, 10–50%, 50–90%, 90% and over), with the average confidence given and the share actually supported. Reads frozen results only; exploratory, not part of the pre-registered checks.
- Charts B scored 90% or more were actually supported 93–100% of the time on all five models (GPT 46 charts 93%→93%; Sonnet 117, 97%→98%; Haiku 118, 98%→98%; Gemini 3.8 Flash 117, 100%→100%; Flash-Lite 44, 93%→93%). The models' own 90%+ statements (A, as stated) were right 54–72% of the time. C was well matched for Sonnet and Gemini 3.8 Flash, overconfident for GPT-5.4 (97%→60%), Flash-Lite (100%→89%) and Haiku (94%→89%).

## 2026-10-28 — paper updated with results; short version

- Added `paper/main.tex` (and `main.pdf`): the preprint rebuilt in LaTeX from `main (7).pdf` (no source was in the repository), with a new Experiments section (study 3 design, pre-registered checks, calibration and ranking, confidence against accuracy, decision metrics, family breakdown, inexpensive models, extraction and faithfulness, secondary views, fitted weights, studies 1 and 2, deviations), an appendix with rubric v3, and the abstract, contributions, related-work status, limitations and conclusion updated to report results. The method sections are unchanged in substance.
- Added `paper/short.tex` (and `short.pdf`): a 3-page version for AI specialists, bottom line only.
- Added `study3/analysis/reliability_figure.py` and `paper/figures/reliability.{pdf,png}`: reliability diagrams on the study 3 test split for A (stated), B and C, per model. Exploratory; reads frozen results only.
- `main (7).pdf` left unchanged.
