# Zenodo upload: Evidence-Weighted Confidence (version 3)

Publish as a **new version** of the existing record (all versions: 10.5281/zenodo.23651100; current version 2: 10.5281/zenodo.23745059):
open the record on Zenodo → **New version** → remove the old files, upload the three below, edit the fields → **Publish**.
Versions 1 and 2 keep their own DOIs and dates; the all-versions DOI then resolves to version 3.

## Files

| Upload as | Source in the repository | What it is |
|---|---|---|
| `Evidence-Weighted-Confidence.pdf` (set as the main / preview file) | `paper/paper.pdf` | The paper, 11 pages |
| `Evidence-Weighted-Confidence-extended.pdf` | `paper/main.pdf` | Extended version, 25 pages: full method explanation, algorithm specification, transparency notes |
| `Evidence-Weighted-Confidence-summary.pdf` | `paper/short.pdf` | 3-page summary |

## Fields

- **Resource type:** Publication → Preprint
- **Title:** Evidence-Weighted Confidence: Auditable, Calibrated Scoring of LLM Outputs
- **Version:** 3
- **Publication date:** the day you publish
- **Creator:** Zeinoun, Issam — ORCID 0009-0007-4874-880X — Independent Researcher
- **Language:** English
- **License:** keep the license of versions 1 and 2

### Description

> Organizations that automate decisions with large language models (LLMs) face a basic problem: the confidence a model reports is not a probability. In our tests, when five current models said they were 93–99% sure that a medical record supported a diagnosis code, they were right only 54–72% of the time. Evidence-weighted confidence (EWC) fixes this by taking the judgment away from the model. The LLM only reads: it answers a short list of questions derived from the governing rules and quotes the text behind each answer. Code verifies the quotes, and a small logistic regression fitted on about 100 labeled cases turns the answers into a probability that comes with an audit trail.
>
> In three pre-registered studies of ICD-10-CM coding on synthetic charts, ending with 200 held-out cases and five models, EWC's scores of 90% or more were right 93–100% of the time on every model, and EWC ranked cases far better than the models' own confidence (AUROC 0.90–1.00 against 0.59–0.77). It also let an inexpensive model match the best frontier result at about one fifteenth of the cost. The charts are synthetic; validation on real records is the next step.
>
> **Files:** the paper (11 pages); an extended version with the full method explanation, algorithm specification and transparency notes (25 pages); and a 3-page summary.
>
> **Changes from version 2:** a shorter main paper with a detailed method diagram; the extended version kept alongside it; the Table 7 caption corrected (recalibration reversed GPT-5.4's confidence, whose fitted Platt slope was negative); and wording that could suggest Bayesian inference removed (the method fits an ordinary logistic regression).
>
> **Code, data, pre-registrations, freeze records and a change log of every decision:** https://github.com/izeinoun/rubric_for_medical_coding

### Keywords

LLM evaluation; calibration; uncertainty quantification; auditability; logistic regression; medical coding; ICD-10-CM; risk adjustment; pre-registration

### Related works

| Relation | Identifier | Type |
|---|---|---|
| Is supplemented by | https://github.com/izeinoun/rubric_for_medical_coding | Software |
| Cites | 10.5281/zenodo.23628695 (Beyond accuracy: monitoring AI in prior authorization) | Publication |

These are the two rows already on the record; nothing to change.

### References

Paste one per box, as for version 2. The main paper cites references 1–11 of `paper/paper.tex`; the extended version adds Rashkin et al. 2023, Gao et al. 2023 and Yue et al. 2023, which can stay.
