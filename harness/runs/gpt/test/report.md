# EWC pilot report — gpt-5.4-2026-03-05 (gpt), test split

Generated 2026-10-27T02:43:02. Charts: 60.

## Calibration and discrimination — All charts

| Method | n | ECE (95% CI) | Brier | AUROC (95% CI) | Coverage at precision ≥ 0.95 |
|---|---|---|---|---|---|
| M1 Verbalized confidence | 60 | 0.514 (0.393–0.639) | 0.509 | 0.571 (0.414–0.727) | 0.00 |
| M2 M1 + Platt scaling | 60 | 0.107 (0.032–0.224) | 0.245 | 0.571 (0.414–0.727) | 0.00 |
| M3 Self-consistency (5 samples) | 60 | 0.167 (0.083–0.267) | 0.167 | 0.812 (0.712–0.908) | 0.00 |
| M4 EWC, expert weights | 60 | 0.153 (0.116–0.221) | 0.080 | 0.967 (0.919–1.000) | 0.20 |
| M5 EWC, fitted weights | 60 | 0.009 (0.006–0.064) | 0.032 | 0.969 (0.904–1.000) | 0.37 |
| M6 Ablation: LLM computes score | 60 | 0.197 (0.115–0.282) | 0.150 | 0.974 (0.931–1.000) | 0.35 |
| M7 Ablation: no quote verification | 60 | 0.009 (0.006–0.064) | 0.032 | 0.969 (0.904–1.000) | 0.37 |
| M8 Ablation: two-way answers | 60 | 0.006 (0.006–0.091) | 0.080 | 0.956 (0.891–0.993) | 0.37 |

## Calibration and discrimination — Excluding charts flagged label_needs_review

| Method | n | ECE (95% CI) | Brier | AUROC (95% CI) | Coverage at precision ≥ 0.95 |
|---|---|---|---|---|---|
| M1 Verbalized confidence | 58 | 0.499 (0.380–0.629) | 0.496 | 0.570 (0.414–0.729) | 0.00 |
| M2 M1 + Platt scaling | 58 | 0.095 (0.028–0.217) | 0.246 | 0.570 (0.414–0.729) | 0.00 |
| M3 Self-consistency (5 samples) | 58 | 0.155 (0.069–0.259) | 0.155 | 0.827 (0.729–0.917) | 0.29 |
| M4 EWC, expert weights | 58 | 0.169 (0.122–0.218) | 0.063 | 0.989 (0.961–1.000) | 0.43 |
| M5 EWC, fitted weights | 58 | 0.031 (0.020–0.041) | 0.003 | 1.000 (1.000–1.000) | 0.47 |
| M6 Ablation: LLM computes score | 58 | 0.215 (0.135–0.301) | 0.150 | 0.996 (0.984–1.000) | 0.45 |
| M7 Ablation: no quote verification | 58 | 0.031 (0.020–0.041) | 0.003 | 1.000 (1.000–1.000) | 0.47 |
| M8 Ablation: two-way answers | 58 | 0.021 (0.014–0.088) | 0.062 | 0.982 (0.958–0.996) | 0.36 |

## Decisions at operating thresholds (all charts)

Auto-accept threshold: the lowest score giving precision ≥ 0.95 on dev, applied unchanged to test. F0.5 weights precision over recall. Charts flagged for review are never auto-accepted.

| Method | Threshold | Precision | Recall | F0.5 | Accepted | Precision at 0.5 | Recall at 0.5 | F0.5 at 0.5 |
|---|---|---|---|---|---|---|---|---|
| M1 | n/a | n/a | 0.000 | n/a | 0.00 | 0.433 | 1.000 | 0.489 |
| M2 | n/a | n/a | 0.000 | n/a | 0.00 | n/a | 0.000 | 0.000 |
| M3 | n/a | n/a | 0.000 | n/a | 0.00 | 0.944 | 0.654 | 0.867 |
| M4 | n/a | n/a | 0.000 | n/a | 0.00 | 0.926 | 0.962 | 0.933 |
| M5 | 0.988 | 0.900 | 0.346 | 0.682 | 0.17 | 0.929 | 1.000 | 0.942 |
| M6 | 0.567 | 0.923 | 0.462 | 0.769 | 0.22 | 0.944 | 0.654 | 0.867 |
| M7 | 0.988 | 0.900 | 0.346 | 0.682 | 0.17 | 0.929 | 1.000 | 0.942 |
| M8 | 0.913 | 0.944 | 0.654 | 0.867 | 0.30 | 0.765 | 1.000 | 0.802 |

![Reliability diagrams](reliability.png)

## Extraction quality against intended answers

After verification. Plain agreement is shown for reference only; answer types are imbalanced.

| Question | Macro-F1 | Recall yes | Recall no | Recall not documented | Precision yes | Precision no | Agreement | Macro-F1 before verification | n |
|---|---|---|---|---|---|---|---|---|---|
| G1 | 1.000 | 1.000 (56) | 1.000 (4) | n/a (0) | 1.000 | 1.000 | 1.000 | 1.000 | 60 |
| G2 | 1.000 | 1.000 (47) | 1.000 (7) | n/a (0) | 1.000 | 1.000 | 1.000 | 1.000 | 54 |
| Q1 | 1.000 | 1.000 (38) | n/a (0) | 1.000 (22) | 1.000 | n/a | 1.000 | 1.000 | 60 |
| Q2 | 0.759 | 0.957 (46) | 1.000 (3) | 0.636 (11) | 1.000 | 0.429 | 0.900 | 0.759 | 60 |
| Q3 | 1.000 | 1.000 (19) | 1.000 (6) | 1.000 (35) | 1.000 | 1.000 | 1.000 | 1.000 | 60 |
| Q4 | 1.000 | 1.000 (36) | n/a (0) | 1.000 (11) | 1.000 | n/a | 1.000 | 1.000 | 47 |

Recall columns show the number of intended answers of that type in parentheses.

Confusion matrices (rows = intended answer, columns = model answer after verification):

**G1**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 56 | 0 | 0 |
| no | 0 | 4 | 0 |
| not_documented | 0 | 0 | 0 |

**G2**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 47 | 0 | 0 |
| no | 0 | 7 | 0 |
| not_documented | 0 | 0 | 0 |

**Q1**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 38 | 0 | 0 |
| no | 0 | 0 | 0 |
| not_documented | 0 | 0 | 22 |

**Q2**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 44 | 0 | 2 |
| no | 0 | 3 | 0 |
| not_documented | 0 | 4 | 7 |

**Q3**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 19 | 0 | 0 |
| no | 0 | 6 | 0 |
| not_documented | 0 | 0 | 35 |

**Q4**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 36 | 0 | 0 |
| no | 0 | 0 | 0 |
| not_documented | 0 | 0 | 11 |

Ambiguous fields (two answers defensible), reported separately:

- G2: agreement 1.000, macro-F1 1.000 (n = 6)
- Q4: agreement 0.615, macro-F1 0.762 (n = 13)

## Faithfulness, review flags and reproducibility

- Yes/no answers whose quote failed verification: 0.000
- By question: G1 0.000 (0 of 60); G2 0.000 (0 of 54); Q1 0.000 (0 of 38); Q2 0.000 (0 of 51); Q3 0.000 (0 of 25); Q4 0.000 (0 of 41)
- Charts flagged for human review by the verification rule: 0
- Unparseable responses: 0
- Median per-chart score SD across extraction runs, M5: 0.000 (n = 60)
- Median per-chart SD of verbalized confidence across runs, M1: 0.006 (n = 60)

## Fitted weights (M5, fitted on dev)

| Feature | Weight |
|---|---|
| intercept | -2.427 |
| Q1_yes | -2.276 |
| Q1_no | 0.000 |
| Q2_yes | -2.492 |
| Q2_no | 0.000 |
| Q3_yes | 0.370 |
| Q3_no | -8.679 |
| Q4_yes | 9.233 |
| Q4_no | 0.000 |

C = 100.0; grid extended: False; still at grid edge: False; training charts: 101 (62 positive).

## Pre-registered checks

| Check | Result |
|---|---|
| H1 macro-F1 >= 0.90 and 'no' recall >= 0.90 on every question | False |
| H2 quote failures <= 5% | True |
| H3 M5 median SD <= 0.05 and below M1 | True |
| H4 M5 AUROC >= M2 AUROC - 0.02 and M5 ECE <= M2 ECE | True |
| H5 M5 beats each of M6, M7, M8 on ECE or AUROC | {'M6': True, 'M7': False, 'M8': True} |
| Kill criterion: M5 worse than M2 on both AUROC and ECE | not triggered |
| Kill criterion: a gate question below 0.90 macro-F1 or 'no' recall | not triggered |

## Usage

600 extraction and verbal calls; 595,699 input tokens, 100,783 output tokens (M6 calls not included).
