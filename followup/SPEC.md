# Follow-up study spec: harder charts (draft for review)

Status: **draft, not pre-registered.** Nothing here has been generated or run. The pilot's data, pre-registration and frozen pipeline are untouched.

## 1. Why a follow-up

The pilot (frozen 2026-10-27, test run once per model) showed that evidence-weighted confidence (EWC, M5) ranks and calibrates far better than the model's own confidence (M1, M2) on both GPT-5.4 and Gemini 3.8 Flash. It also left gaps that the follow-up should close:

| Gap in the pilot | Evidence | What the follow-up needs |
|---|---|---|
| Labels are a function of the rubric answers | Pre-registration section 3; M5 AUROC 1.000 on both models once the 2 flagged test charts are removed | Charts whose label depends on facts the rubric does **not** ask about, so EWC can be wrong for reasons other than extraction errors |
| Quote verification never tested | 0 quote failures on dev and test for both models; M7 identical to M5 | Notes where exact quoting is hard, so some quotes fail |
| Gates trivially easy | G1 and G2 macro-F1 1.000 everywhere | Ambiguous diabetes type, CKD stated in conflicting ways |
| Copy-forward drives every error | SYN-0182 (F1b) was the only wrongly accepted test chart for both models | More copy-forward variants, with labels clear enough that none need a review flag |
| Few charts in the middle of the probability range | Most M5 scores are near 0 or 1 | Borderline charts, so calibration is judged where it matters |
| Small test set | 60 charts; AUROC intervals about 0.1 wide | A larger test set |
| Weak confidence baseline | The verbal prompt asks a holistic question and gives no criteria | A stronger baseline that is given the same criteria as the rubric |

## 2. Design principles

1. **Rubric and prompts stay at the pilot's frozen versions** (prompt version 1, rubric version 2) for the first dev run, so that any drop in performance is attributable to the charts, not to new wording. Dev iteration is allowed afterwards under the same logging rules as the pilot.
2. **Ground truth is defined before the notes are written.** Each chart is generated from a fact sheet. The label comes from coding rules applied to those facts, including facts outside the rubric, not from the rubric answers.
3. **Labels are reviewed blind.** A coder who has not seen model outputs labels a stratified sample (at least 60 charts) from the note text alone. The pilot reviewed 20.
4. **Weights are refitted on the new dev split.** Pilot weights are reported only as a transfer check (section 6, H9), not as the main result.

## 3. Scenario families

Counts are proposals for a 400-chart set (section 4). Label 1 means the chart supports E11.22 for risk-adjustment submission.

### A. Carried over from the pilot (about 25% of charts)

The 13 pilot scenarios at reduced counts, regenerated with the new note template (section 3H), so that results on familiar scenarios can be compared with the pilot.

### B. Copy-forward (about 12%)

| ID | Label | What the note shows |
|---|---|---|
| B1 | 1 | Plan copied forward; the CKD line cites today's eGFR with today's date and a current action |
| B2 | 0 | Plan copied forward word for word from a dated prior visit; eGFR and action both carry the prior date; no CKD content elsewhere in today's note |
| B3 | 1 | Copied CKD line followed by a short new line from today ("eGFR today 41, stable; continue") |
| B4 | 0 | Copied CKD line marked "per last visit" or "unchanged from 3/2026"; today's labs are not mentioned |
| B5 | 1 | Interval history mentions today's renal labs; the plan's CKD line is copied but refers to them |

Rule for writing these: the label must be decidable from the text by a coder, with no review flag. If a draft chart needs a review flag, rewrite it or drop it.

### C. Gates made harder (about 12%)

| ID | Label | What the note shows |
|---|---|---|
| C1 | 1 | "DM" or "diabetes" with no type, on metformin; CKD due to diabetes (type 2 by ICD-10-CM default) |
| C2 | 1 | Type 2 diabetes on insulin (insulin use does not make it type 1) |
| C3 | 0 | Type 1 diabetes documented only in the HPI; the assessment says "diabetes" |
| C4 | 0 | CKD established in the problem list, but the assessment says "rule out CKD, repeat labs" (most specific current statement wins) |
| C5 | 1 | "History of CKD" in the HPI, and the plan gives a current CKD status and action |
| C6 | 0 | CKD in a kidney transplant recipient documented as "CKD resolved post-transplant" |

### D. Lab and date edge cases for Q2 (about 8%)

eGFR exactly 60; result gaps of 89, 90 and 91 days; a missing date; creatinine without eGFR; eGFR given as "> 60"; results in a sentence instead of a lab table. Labels follow the pilot rule (Q2 does not decide the label), so these test extraction only.

### E. Cause attribution for Q3 (about 8%)

| ID | Label | What the note shows |
|---|---|---|
| E1 | 1 | "CKD due to diabetes and hypertension" (diabetes is one stated cause) |
| E2 | 1 | "Likely diabetic nephropathy" (hedged, but attributed) |
| E3 | 0 | Cause stated as "hypertensive nephrosclerosis" in the assessment, while the HPI says "diabetic" (current assessment wins) |
| E4 | 1 | Cause stated only in a dated prior-visit section; no conflicting cause today ("with" convention applies) |

### F. Outside the rubric (about 15%)

The rubric answers look like a positive chart, but the label is 0 for a reason the rubric does not ask about. These test whether EWC is overconfident when its criteria are incomplete. That is the main limit the pilot could not measure.

| ID | Label | Reason, not covered by any rubric question |
|---|---|---|
| F1 | 0 | Audio-only telephone visit (not acceptable for risk adjustment) |
| F2 | 0 | Note unsigned or signed by a non-acceptable provider type |
| F3 | 0 | The document is a stand-alone diagnostic or lab report, not a provider encounter note (not an acceptable risk-adjustment source) |
| F4 | 0 | Encounter date outside the collection year |

Analysis: report EWC's scores on family F separately. A well-behaved method should not give these charts high confidence. EWC is expected to fail here unless the rubric is extended, and the follow-up should show how badly.

### G. Borderline and mid-probability (about 10%)

| ID | Label | What the note shows |
|---|---|---|
| G1 | 1 | CKD addressed only by "renal function reviewed, stable"; no stage, no cause |
| G2 | 0 | CKD mentioned in the plan with "see nephrology note"; no status or action today |
| G3 | 1 | CKD addressed by medication adjustment only (for example, metformin dose reduced for eGFR) without naming CKD in that line |
| G4 | 0 | "CKD 3a, stable" as a one-line list entry that also contains a status word (tests where "status" starts) |

G3 generalizes pilot chart SYN-0055, the borderline case Gemini missed on dev.

### H. Note format stress for quote verification (applied across families)

About half of all charts, spread across families A–G, get one or more of:

- Notes 3 to 5 times longer than the pilot (median about 2,000 characters now): prior-visit sections, medication reconciliation, review of systems.
- Lab tables with irregular spacing and tab characters.
- OCR-style noise: l/1 and O/0 swaps, broken hyphenation across lines, stray page headers in the middle of a section.
- Repeated, nearly identical lines from earlier visits, differing only by date or value.
- Non-ASCII punctuation (curly quotes, en dashes, non-breaking spaces).

Target: a quote failure rate of at least 3% on dev for at least one model, so that M7 (no verification) can differ from M5. If dev shows fewer failures, record that rather than adding more noise.

## 4. Size and splits

- 400 charts: 200 dev, 200 test, stratified by scenario. 200 test charts give AUROC intervals roughly half as wide as the pilot's 60.
- Positive rate about 40%, close to the pilot, so results can be compared. Prevalence is still far above real populations; state this as a limitation again.
- Cost per model, rough: longer notes multiply input tokens by about 3. Expect about 6M input tokens per model for dev and the same for test, plus Gemini thinking tokens. Run `estimate` once the data exists.

## 5. Methods

Same as the pilot (M1–M8, same fitting procedure, same verification rule), plus one stronger baseline:

- **M9, criteria-informed verbal confidence.** The verbal prompt also lists the rubric's questions and guidance, and asks for a probability. This tests whether EWC's advantage comes from the structure (code does the weighing) or only from giving the model the criteria. Platt-scaled like M2.

Models: GPT-5.4 (`gpt-5.4-2026-03-05`) and Gemini 3.8 Flash, as in the pilot. Optional additions, decided before pre-registration: Claude (needs an Anthropic key), and GPT-5.4 with reasoning turned on, to test whether thinking fixes the Q2 date arithmetic.

## 6. Draft hypotheses (to be finalized in the pre-registration)

H1–H5 as in the pilot, with the same pass marks. New:

| ID | Claim | Pass mark (draft) |
|---|---|---|
| H6 | EWC beats self-reported confidence on ranking | M5 AUROC − M2 AUROC ≥ 0.10, with the paired bootstrap 95% interval above 0, on each model |
| H7 | EWC beats criteria-informed confidence | M5 AUROC ≥ M9 AUROC and M5 ECE ≤ M9 ECE |
| H8 | Quote verification helps | M5 beats M7 on ECE or AUROC, given at least 3% quote failures |
| H9 | Weights transfer | Pilot-fitted weights applied to the new test split: ECE reported against refitted M5 (descriptive, no pass mark) |
| H10 | Out-of-rubric failure is visible | Mean M5 score on family F reported with its interval (descriptive; expected to be high) |

The pilot compared overlapping intervals; H6 adds a proper paired test, so the claim "significantly better" can be made directly.

## 7. Order of work

1. Review this spec, and decide the open questions below.
2. Write generator v3 as a new script (`followup/generate_charts_v3.py`). The pilot's `generate_charts.py` and `data/charts.jsonl` stay unchanged.
3. Blind label review of at least 60 charts by a coder; fix the generator until labels agree.
4. Write and freeze the follow-up pre-registration (`followup/PREREGISTRATION.md`) before any model call.
5. Dev collection, evaluation and allowed iteration, all logged; then freeze and run test once, as in the pilot.

## 8. Open questions for the user

1. Should family F (outside the rubric) be in the main analysis, or reported separately as a stress test? It will lower EWC's headline numbers by design.
2. Who does the blind label review, and is 60 charts enough?
3. Add Claude, and/or GPT-5.4 with reasoning turned on?
4. Is 400 charts (200 test) affordable, given longer notes?
5. Confirm the coding rules behind F1–F4 and C4 (risk-adjustment acceptability of telephone visits, provider types, stand-alone diagnostic reports and dates of service, and "most specific current statement wins").
