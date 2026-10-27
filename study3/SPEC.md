# Study 3: improved rubric (v3) on 350 charts — one-page plan

Status: plan for review (2026-10-27). Nothing built or run.

## The claim (unchanged since the pilot)
When a model judges whether a chart supports E11.22, our method (the model answers fixed questions with exact quotes; code checks the quotes and computes the score) gives a more trustworthy confidence than the model's own stated confidence.

## Why a new study
The follow-up (frozen pilot method on 300 harder charts) was stopped after stage 1, as its pre-registration allows, and is reported as directional. Stage 1 showed what to fix: the rubric cannot see provider, signature or encounter rules; two borderline phrasings need clear rules; the copy-forward rule was disputed. Study 3 fixes these on a dev split and tests once on charts no model has seen.

## Data: 350 charts
| Source | Charts | Split |
|---|---|---|
| Follow-up stage 1 (results seen) | 100 | dev |
| Follow-up stage 2 (never run) | 200 | 25 dev, 175 test |
| New hard cases | 50 | 25 dev, 25 test |
| **Total** | **350** | **150 dev, 200 test** |

Existing chart texts are reused unchanged; only labels change where the rules below change them.

**New hard cases (about 12 each):** conflicting statements within one note; CKD stage contradicted by the lab values; dialysis and end-stage kidney disease; incomplete or unclear statements that partly answer the questions.

## Label rules (study 3)
Supported (label 1) only if: type 2 diabetes documented (untyped defaults to type 2; secondary diabetes is not type 2); CKD an established diagnosis; CKD addressed at this visit; CKD not attributed to a different cause *instead of* diabetes (diabetes plus another cause still counts); face-to-face visit with an MD, DO, NP or PA; note signed with credentials.

"Addressed" follows the study lead's MEAT reading: a copied plan line with "continue regimen" or "stable" counts, as does CKD named in a list of chronic conditions reviewed. Proposed for the new cases (to confirm): the current assessment and plan governs when sections conflict; a documented stage counts even if the labs disagree (coders do not override the provider); ESRD on dialysis supports E11.22; "CKD?" or "possible CKD" is not established.

## Rubric v3 (changes from v2; prompts otherwise unchanged)
- New gates: R1 face-to-face with an acceptable provider; R2 signed with credentials. Secondary diabetes goes into G1's guidance.
- Q3 guidance: diabetes plus another cause is "yes".
- Q4 guidance: the MEAT reading above; "see nephrology note" alone is not addressed; a medication change made because of kidney function is addressed.
- Weights refitted on dev (same frozen fitting procedure).

## Methods compared (same three as the follow-up)
A, the model's stated confidence; B, our method with rubric v3; C, the model given the rubric's questions and told to base its confidence on them. Models: GPT-5.4 and Gemini 3.8 Flash.

## Order of work
1. Generate the 50 hard charts; relabel existing charts under the new rules; independent checks.
2. Study lead reviews a sample (the new hard cases plus relabeled charts).
3. Dev: collect, fit, iterate the rubric if needed (logged).
4. Write the study 3 pre-registration; freeze.
5. Test once on the 200 test charts. Report.

Cost: about 11 calls per chart per model; dev 150 charts (plus any re-runs after rubric changes), test 200.
