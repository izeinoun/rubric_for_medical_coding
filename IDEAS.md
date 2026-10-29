# Ideas for future studies

A running list. Each item says where it came from and what it would test. Items marked **study 4** are in the plan in `study4/PLAN.md`; the rest wait for a later study. Add new ideas at the end of their group.

## Making the evidence itself carry confidence

1. **Evidence-quality checks on each quote (study 4).** Code, not the model, rates the text behind each answer: which section the quote came from (assessment and plan, problem list, history, prior visit), hedging words ("possible", "likely", "?"), pointers to another note ("see nephrology note", "per last visit"), whether the quoted text is dated today or earlier, and whether other quotes contradict it. Used as a review flag and as extra inputs to the fitted model. *From:* the study lead's point that per-question confidence must come from the evidence, not from the model; most remaining errors were Q4 "yes" based on "see nephrology note".
2. **Let code do the date arithmetic for Q2 (study 4).** The model extracts each eGFR value and date; code decides whether two results below 60 are at least 90 days apart. *From:* Q2 was the weakest question on three models (macro-F1 0.74–0.86), mostly date errors near the 90-day boundary. Same principle as the method: the LLM reads, code decides.
3. **Semantic check of quotes by a second model.** A model from a different family judges whether each quote, shown with its section, supports the answer. *From:* paper, Section 9; the remaining errors are real quotes misread.
4. **Check only the answers that matter.** Run costly checks only on answers whose removal would move a chart across the auto-accept threshold, plus a random sample of the rest. *From:* paper, Section 9.

## Data and design

5. **Oversample contradictions (study 4).** 20–30 charts per question whose correct answer is "no", so the value of keeping "contradicted" separate from "not documented" can be measured. *From:* paper, note 1 (only 5 of 350 charts had a documented other cause).
6. **Real charts labeled by certified coders.** De-identified notes (for example MIMIC, or a partner's data), two or more coders, inter-rater agreement reported, and coder review of the rubric and label rules (including the MEAT reading of copied-forward lines). *From:* paper limitations and note 5; the main external-validity question.
7. **Realistic prevalence.** A test set near the real share of supported charts, with the intercept shifted as in Appendix A.4, and calibration rechecked. *From:* paper limitations (58% positive here).
8. **More codes, layered rubrics.** A generic layer (encounter and signature rules), a family layer (diabetes with complications) and code overrides; partial pooling of weights across a family. *From:* paper, Section 8.
9. **How many labels are enough.** A learning curve: fit the weights on 25, 50, 100 and 150 development charts and track calibration on test. *From:* the "10–20 positives per weight" rule of thumb in Section 6, never tested.
10. **Stress the quote check.** Notes with heavier OCR noise, line breaks inside words and near-duplicate text, so quotes fail more often and the value of verification can be measured. *From:* paper limitations (models almost never misquoted).

## Methods and analyses not yet run

11. **Ablations from the protocol that were never run:** drop the gates; naive Bayes instead of logistic regression. *From:* paper, Section 6.
12. **The model computes its own score from the fitted weights (M6), on all five models.** Run only in the pilot (GPT-5.4 ranked as well as code but was far worse calibrated). *From:* pilot results.
13. **DeLong z-tests and a chart-by-chart comparison page** for the study-3 test results. Exploratory; uses existing data, no new calls. *From:* planned during study 3, not yet done.
14. **Stability over time.** Re-run the frozen pipeline on the same charts after model updates to measure drift; monitor answer rates and quote failures as label-free signals. *From:* paper, Section 9.
15. **Evidence across several documents.** An agent fetches earlier visits or lab reports when evidence is missing; scoring stays fixed. *From:* paper, Section 9.
16. **Cost controls.** One call per chart for all questions, prompt caching, batch APIs; report cost per chart. *From:* paper, Section 9.

## Ideas considered and set aside

- **Asking the model for a confidence on each answer.** Rejected: it brings back the self-reported confidence the method removes. A check on the frozen study-3 data also showed the errors are systematic: answers that varied across the 5 extraction runs caught only 2 of 19 GPT-5.4 errors and 7 of 19 Flash-Lite errors, while flagging many correct charts.
