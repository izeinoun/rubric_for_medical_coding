# Zenodo upload: Evidence-Weighted Confidence (version with experiments)

Publish as a **new version** of the existing record (concept DOI 10.5281/zenodo.23651100):
open the record on Zenodo → **New version** → replace the file and edit the fields below → **Publish**.
The earlier version keeps its own DOI and date; the concept DOI then resolves to this version.

## Files

| File | Source in the repository |
|---|---|
| `Evidence-Weighted-Confidence.pdf` (main file) | `paper/main.pdf` |
| `Evidence-Weighted-Confidence-short.pdf` | `paper/short.pdf` |

## Fields

- **Resource type:** Publication → Preprint
- **Title:** Evidence-Weighted Confidence: Auditable, Calibrated Scoring of LLM Outputs
- **Version:** 2 (method, protocol and pre-registered experiments)
- **Publication date:** the day you publish
- **Creator:** Zeinoun, Issam — ORCID 0009-0007-4874-880X — Independent Researcher
- **Language:** English
- **License:** keep the license of version 1 (CC BY 4.0 is the usual choice for preprints)

### Description

> A confidence number reported by a large language model (LLM) has no defined meaning. Evidence-weighted confidence (EWC) replaces it with a score computed from verifiable evidence: the LLM answers rule-derived questions with exact quotes, code verifies the quotes, and a logistic regression fitted on labeled data turns the answers into a calibrated probability, with an audit trail behind every score.
>
> This version adds three pre-registered studies on synthetic outpatient charts for ICD-10-CM E11.22, ending with a 350-chart study (200 held-out test charts) on five models: GPT-5.4, Claude Sonnet 5.5, Claude Haiku 5.5, Gemini 3.8 Flash and Gemini 3.5 Flash-Lite. When EWC gave 90% or more, the chart was supported 93–100% of the time on every model; when the models stated 93–99% themselves, they were right 54–72% of the time. EWC ranked charts better than the models' own confidence on every model (AUROC 0.897–1.000 against 0.593–0.772) and was the best-calibrated method on every model. On frontier models given the same questions, EWC matched their ranking and added calibration, verified quotes and a reproducible score; with EWC, the inexpensive Claude Haiku 5.5 matched the best result at about one fifteenth of the cost. The data are synthetic and their labels favor the method; the paper states these limits.
>
> Files: the full paper and a 3-page short version. Code, data, pre-registrations, freeze records and a change log of every decision: https://github.com/izeinoun/rubric_for_medical_coding

### Keywords

LLM evaluation; calibration; uncertainty quantification; auditability; weight of evidence; logistic regression; medical coding; ICD-10-CM; risk adjustment; pre-registration

### Related works

| Relation | Identifier | Type |
|---|---|---|
| Is supplemented by | https://github.com/izeinoun/rubric_for_medical_coding | Software |
| References | 10.5281/zenodo.23628695 (Beyond accuracy: monitoring AI in prior authorization) | Publication |

Optional: connect Zenodo to GitHub and make a release of the repository; it then gets its own DOI, which can replace the GitHub URL above as "Is supplemented by".
