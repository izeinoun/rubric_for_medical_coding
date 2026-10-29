# Study 4 plan (draft for review)

Status: draft, 2026-10-29. Nothing built or run. Study 3 and its test data stay frozen and untouched.

## The question

Can confidence for each answer come from the **quoted evidence itself**, measured by code, so that the remaining errors are caught without asking the model how sure it is? And do three-way answers (yes / no / not documented) add value when the data actually contains contradictions?

## What study 3 left open

- Most remaining errors were real quotes misread, mainly Q4 = "yes" based on "see nephrology note" (GPT-5.4, Flash-Lite).
- Q2 (two eGFR results below 60, at least 90 days apart) was the weakest question on three models, mostly date arithmetic.
- Only 5 of 350 charts had a documented other cause (Q3 = "no"), so the value of three-way answers was not measured.

## Three changes, tested together and one at a time

| Change | What it is | Expected effect |
|---|---|---|
| **Evidence checks** | Code rates each quote: the section it came from (assessment and plan, problem list, history, prior visit), hedging words, pointers to another note, whether its date is today's, and whether other quotes contradict it. Used two ways: a **review flag** when a deciding answer rests on weak evidence, and **extra inputs** to the fitted model (for example "Q4 = yes, from the plan" vs "Q4 = yes, pointer only"). | Catches the Q4 pointer errors and stale copied-forward evidence |
| **Q2 computed by code** | The model lists each eGFR value with its date and quote; code decides the 90-day rule. | Q2 errors from date arithmetic disappear |
| **Contradictions oversampled** | Charts built so that each question has a fair number of "no" answers. | Lets the three-way vs two-way comparison mean something |

All three come from the same extraction call, so each change can also be switched off in the analysis without new calls.

## Methods compared

- **B**: the study-3 method unchanged (rubric v3; weights refitted on study-4 development charts by the same frozen procedure).
- **B+**: B with the evidence checks and Q2 computed by code.
- **A** (the model's stated confidence) and **C** (the rubric questions in the prompt), one run each, for continuity with study 3.

## Data: 300 new synthetic charts (dev 120, test 180)

| Group | Charts | What they test |
|---|---|---|
| Weak-evidence wording | 100 | 25 each: pointer to another note, hedged diagnosis, stale or prior-visit evidence, sections that disagree; about half supported |
| Contradictions | 80 | 30 with a documented other cause (Q3 = "no"); 10 each for G1, G2, R1, R2 and Q2 |
| Q2 date edge cases | 40 | eGFR pairs 80–100 days apart, values near 60 |
| Ordinary charts | 80 | The study-3 families, for comparison |

Built with the study-3 generator plus new scenarios; same label rules as study 3; checked by the built-in checker and a review sample by the study lead. About half supported.

## Models

GPT-5.4, Claude Haiku 5.5 and Gemini 3.5 Flash-Lite: the two models with most errors, plus the cheap model that did best. Optional: Claude Sonnet 5.5 or Gemini 3.8 Flash as a ceiling.

## Hypotheses (test split, per model; pass marks to agree before the freeze)

| ID | Claim | Proposed pass mark |
|---|---|---|
| H1 | B+ ranks better than B | AUROC difference > 0, paired 95% interval above 0 |
| H2 | B+ is at least as well calibrated as B | ECE of B+ ≤ ECE of B |
| H3 | The review flag catches B's errors | Flags at least half of the charts B gets wrong at 0.5, while flagging no more than 20% of the charts it gets right |
| H4 | Code computes Q2 reliably | Q2 macro-F1 ≥ 0.95 |
| H5 | Three-way answers add value | B with three-way answers beats B with two-way answers on AUROC, paired interval above 0, on the contradiction charts |

## Procedure (same safeguards as study 3)

1. Build the charts and the evidence checks; study lead reviews a sample.
2. Development: collect, fit, revise the checks if needed; every change logged in `CHANGELOG.md`.
3. Write the pre-registration; freeze with hashes.
4. Test once per model; report every hypothesis, passed or failed.

## Cost

Three calls per chart per model (one extraction, one stated confidence, one rubric prompt), about 900 calls per model: roughly a quarter of a study-3 model's calls. Study 3 showed one extraction run is enough (the median score did not change across five runs).

## Decisions for the study lead

1. Models: the three above, or add a stronger one?
2. Keep method C?
3. The pass marks in the table.
4. Evidence checks as a review flag only, as model inputs only, or both (proposed: both, with the flag reported first because it needs no extra labels).

## Not in this study

Real charts with certified coders, more codes, realistic prevalence and the other items in `IDEAS.md`. Real-chart validation is the study after this one.
