# Study 4 plan (draft for review)

Status: draft, 2026-10-29. Nothing built or run. Study 3 and its test data stay frozen and untouched.

## The claim to test

On charts that are genuinely hard (ones two human coders would argue about), the method scores fairly: confident where the chart is clear, in the middle and sent to review where it is disputed, and almost never confidently wrong. Where the method reaches its limit, two additions recover the performance:

1. **New questions**, written from the errors found on development charts.
2. **A clarity check on each answer's quoted text**, computed by code and entered into the fitted model as features.

## Design choices (agreed with the study lead)

- **One model: Claude Haiku 5.5.** The aim is to show the mechanism, not breadth across models (study 3 covered that). Haiku was the best balance of cost and accuracy in study 3.
- **Charts written by a Gemini model** from structured specs, so the model that writes the charts is not the model tested. The Gemini model is never tested.
- **Clarity enters as features, not as a multiplier.** Each weighted answer is split by the clarity of its evidence into separate indicators (for example `Q4 = yes, clear` and `Q4 = yes, weak`), and the logistic regression learns a weight for each. The model stays a single convex logistic regression: unique solution, every weight still a log-odds contribution of one kind of evidence, no hand-set discounts.

## Labels: three kinds of chart

| Label | Meaning | What the method should do |
|---|---|---|
| Clearly supported | Any careful coder would report E11.22 | High score |
| Clearly not supported | Any careful coder would not | Low score |
| Disputed | Reasonable coders split; both readings written down in the spec | Middle score or review flag; never confidently wrong |

Who decides: the chart's spec sets the intended label. The study lead and two independent reviewer models from families not tested (for example GPT-5.4 and a Gemini Pro model) each read a sample; any split on a chart marked clear sends it back for revision. A certified coder checking 30–50 charts would strengthen this considerably (open question).

## The charts

About 400 notes, each from a short spec: the facts, the intended answer to each question, the label, and for disputed charts the two readings. A Gemini model writes the note from the spec. A code checker confirms the spec's key facts appear in the text and that the note does not signal its own difficulty (no "this is ambiguous"). The study lead reviews a sample.

Sources of genuine dispute in E11.22 coding, for example:

- "CKD, stable" with no status, data or plan (does it meet MEAT?)
- "Diabetic nephropathy" or "DM with renal complications" without the words CKD or chronic kidney disease
- "Likely CKD" or "CKD vs. AKI" in the plan
- Acute kidney injury on top of known CKD
- CKD after a kidney transplant
- eGFR values hovering around 60
- A resident's note with an attending's attestation; a scribe's note co-signed
- Audio-only or video telehealth visits
- An addendum by a different provider
- The problem list and the assessment disagreeing
- Diabetes named with another cause in hedged terms ("possibly also hypertensive")
- Copied-forward plan lines with partial updates

Mix: about one third clearly supported, one third clearly not supported, one third disputed. Each clarity category is oversampled so every split indicator has enough development examples (target at least 15–20 each).

Splits: **development 200, test 200.** Some scenario types appear **only in test**, so an improvement cannot come from tuning on the development cases.

## Clarity of the quoted evidence (computed by code)

For each weighted answer, code reads the quotes and marks the evidence **clear** or **weak**. Weak if any of:

- the quote comes from outside today's assessment and plan (problem list, history, a prior-visit section);
- it contains a hedge ("possible", "likely", "probable", "?", "vs.");
- it only points elsewhere ("see nephrology note", "per last visit", "as above");
- its date is not today's visit date;
- another quote in the note contradicts it.

The rules are written and frozen on development data. The model is never asked how sure it is.

## Methods compared (all from the same Haiku calls)

| ID | Method |
|---|---|
| B3 | The study-3 method, rubric v3, weights refitted on study-4 development charts by the frozen procedure |
| B4 | B3 plus the new questions |
| B4+C | B4 plus the clarity features (the full method) |
| A | Haiku's stated confidence, recalibrated |
| C | Rubric questions in the prompt, Haiku's own number |

B4 and B4+C come from one extraction call per chart with the new rubric; B3 is the same call scored with only the v3 questions. Each addition can therefore be switched on or off in the analysis without new calls.

## Hypotheses (test split; pass marks to agree before the freeze)

| ID | Claim | Proposed pass mark |
|---|---|---|
| H1 | The full method is never confidently wrong on disputed charts | At most 5% of disputed charts scored ≥ 0.9 or ≤ 0.1 |
| H2 | The additions improve ranking on clear charts | AUROC of B4+C > AUROC of B3, paired 95% interval above 0 |
| H3 | The additions improve calibration on clear charts | ECE of B4+C ≤ ECE of B3 |
| H4 | The full method beats Haiku's own confidence and the rubric prompt on clear charts | AUROC difference > 0, paired interval above 0, against A and against C |
| H5 | The clarity features add value beyond the new questions | AUROC or log-loss of B4+C better than B4, paired interval excluding 0 |

Also reported, without pass marks: results on the test-only scenario types; the fitted weights for clear vs weak evidence (does the data confirm that weak evidence is worth less?); the review-flag view (deciding answer weak and score near the threshold); confidently-wrong rates for A and C on disputed charts.

## Procedure (same safeguards as study 3)

1. Write the specs; generate the notes with Gemini; run the checker; study lead and reviewers check a sample.
2. **Stage 1, development:** run B3 on the development charts and record where it fails.
3. **Stage 2, development:** write the new questions and the clarity rules from those failures; fit B4 and B4+C on development charts; log every change in `CHANGELOG.md`.
4. Write the pre-registration; freeze with hashes.
5. Test once; report every hypothesis, passed or failed.

## Cost

Haiku: three calls per chart (one extraction, one stated confidence, one rubric prompt), about 1,200 calls for 400 charts, likely a few dollars. Gemini: about 400 note-writing calls, plus the reviewer models on a sample.

## Open decisions

1. The pass marks in the table, especially H1's 5%.
2. Keep method C (proposed: yes; it is cheap and the fair comparison).
3. Whether a certified coder can check 30–50 charts.
4. Which Gemini model writes the notes, and which models review.
