# EWC pilot report — gemini-3.8-flash (gemini), dev split

Generated 2026-10-28T01:16:01. Charts: 150.

**Development split.** Fitted methods (M2, M5, M7, M8) are scored out-of-fold with C chosen on all of dev, so these numbers are mildly optimistic. They are for iteration, not for the paper.

## Calibration and discrimination — All charts

| Method | n | ECE (95% CI) | Brier | AUROC (95% CI) | Coverage at precision ≥ 0.95 |
|---|---|---|---|---|---|
| M1 Verbalized confidence | 150 | 0.410 (0.332–0.487) | 0.404 | 0.695 (0.614–0.771) | 0.01 |
| M2 M1 + Platt scaling | 150 | 0.047 (0.039–0.134) | 0.216 | 0.676 (0.588–0.761) | 0.01 |
| M3 Self-consistency (5 samples) | 150 | 0.101 (0.057–0.153) | 0.100 | 0.896 (0.847–0.943) | 0.00 |
| M4 EWC, expert weights | 150 | 0.106 (0.092–0.149) | 0.061 | 0.993 (0.984–0.999) | 0.55 |
| M5 EWC, fitted weights | 150 | 0.013 (0.001–0.033) | 0.013 | 0.987 (0.965–1.000) | 0.57 |
| M7 Ablation: no quote verification | 150 | 0.013 (0.001–0.033) | 0.013 | 0.987 (0.965–1.000) | 0.57 |
| M8 Ablation: two-way answers | 150 | 0.002 (0.001–0.023) | 0.014 | 0.979 (0.945–1.000) | 0.57 |

## Calibration and discrimination — Excluding charts flagged label_needs_review

| Method | n | ECE (95% CI) | Brier | AUROC (95% CI) | Coverage at precision ≥ 0.95 |
|---|---|---|---|---|---|
| M1 Verbalized confidence | 150 | 0.410 (0.332–0.487) | 0.404 | 0.695 (0.614–0.771) | 0.01 |
| M2 M1 + Platt scaling | 150 | 0.047 (0.039–0.134) | 0.216 | 0.676 (0.588–0.761) | 0.01 |
| M3 Self-consistency (5 samples) | 150 | 0.101 (0.057–0.153) | 0.100 | 0.896 (0.847–0.943) | 0.00 |
| M4 EWC, expert weights | 150 | 0.106 (0.092–0.149) | 0.061 | 0.993 (0.984–0.999) | 0.55 |
| M5 EWC, fitted weights | 150 | 0.013 (0.001–0.033) | 0.013 | 0.987 (0.965–1.000) | 0.57 |
| M7 Ablation: no quote verification | 150 | 0.013 (0.001–0.033) | 0.013 | 0.987 (0.965–1.000) | 0.57 |
| M8 Ablation: two-way answers | 150 | 0.002 (0.001–0.023) | 0.014 | 0.979 (0.945–1.000) | 0.57 |

## Decisions at operating thresholds (all charts)

Auto-accept threshold: the lowest score giving precision ≥ 0.95 on dev, applied unchanged to test. F0.5 weights precision over recall. Charts flagged for review are never auto-accepted. On dev the threshold is chosen on these same charts, so dev precision meets the target by construction.

| Method | Threshold | Precision | Recall | F0.5 | Accepted | Precision at 0.5 | Recall at 0.5 | F0.5 at 0.5 |
|---|---|---|---|---|---|---|---|---|
| M1 | 1.000 | 1.000 | 0.012 | 0.059 | 0.01 | 0.544 | 1.000 | 0.598 |
| M2 | 0.736 | 1.000 | 0.025 | 0.112 | 0.01 | 0.640 | 0.704 | 0.652 |
| M3 | n/a | n/a | 0.000 | n/a | 0.00 | 0.849 | 0.975 | 0.872 |
| M4 | 0.332 | 0.964 | 0.988 | 0.969 | 0.55 | 0.987 | 0.926 | 0.974 |
| M5 | 0.009 | 0.953 | 1.000 | 0.962 | 0.57 | 0.976 | 1.000 | 0.981 |
| M7 | 0.009 | 0.953 | 1.000 | 0.962 | 0.57 | 0.976 | 1.000 | 0.981 |
| M8 | 0.013 | 0.953 | 1.000 | 0.962 | 0.57 | 0.976 | 1.000 | 0.981 |

![Reliability diagrams](reliability.png)

## Extraction quality against intended answers

After verification. Plain agreement is shown for reference only; answer types are imbalanced.

| Question | Macro-F1 | Recall yes | Recall no | Recall not documented | Precision yes | Precision no | Agreement | Macro-F1 before verification | n |
|---|---|---|---|---|---|---|---|---|---|
| G1 | 1.000 | 1.000 (141) | 1.000 (8) | n/a (0) | 1.000 | 1.000 | 1.000 | 1.000 | 149 |
| G2 | 1.000 | 1.000 (129) | 1.000 (7) | n/a (0) | 1.000 | 1.000 | 1.000 | 1.000 | 136 |
| R1 | 0.998 | 0.993 (137) | 1.000 (13) | n/a (0) | 1.000 | 1.000 | 0.993 | 0.998 | 150 |
| R2 | 1.000 | 1.000 (144) | 1.000 (6) | n/a (0) | 1.000 | 1.000 | 1.000 | 1.000 | 150 |
| Q1 | 1.000 | 1.000 (117) | n/a (0) | 1.000 (25) | 1.000 | n/a | 1.000 | 1.000 | 142 |
| Q2 | 1.000 | 1.000 (99) | 1.000 (7) | 1.000 (43) | 1.000 | 1.000 | 1.000 | 1.000 | 149 |
| Q3 | 1.000 | 1.000 (42) | 1.000 (2) | 1.000 (99) | 1.000 | 1.000 | 1.000 | 1.000 | 143 |
| Q4 | 1.000 | 1.000 (100) | n/a (0) | 1.000 (20) | 1.000 | n/a | 1.000 | 1.000 | 120 |

Recall columns show the number of intended answers of that type in parentheses.

Confusion matrices (rows = intended answer, columns = model answer after verification):

**G1**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 141 | 0 | 0 |
| no | 0 | 8 | 0 |
| not_documented | 0 | 0 | 0 |

**G2**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 129 | 0 | 0 |
| no | 0 | 7 | 0 |
| not_documented | 0 | 0 | 0 |

**R1**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 136 | 0 | 1 |
| no | 0 | 13 | 0 |
| not_documented | 0 | 0 | 0 |

**R2**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 144 | 0 | 0 |
| no | 0 | 6 | 0 |
| not_documented | 0 | 0 | 0 |

**Q1**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 117 | 0 | 0 |
| no | 0 | 0 | 0 |
| not_documented | 0 | 0 | 25 |

**Q2**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 99 | 0 | 0 |
| no | 0 | 7 | 0 |
| not_documented | 0 | 0 | 43 |

**Q3**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 42 | 0 | 0 |
| no | 0 | 2 | 0 |
| not_documented | 0 | 0 | 99 |

**Q4**

| intended \ model | yes | no | not documented |
|---|---|---|---|
| yes | 100 | 0 | 0 |
| no | 0 | 0 | 0 |
| not_documented | 0 | 0 | 20 |

Ambiguous fields (two answers defensible), reported separately:

- G1: agreement 1.000, macro-F1 1.000 (n = 1)
- G2: agreement 1.000, macro-F1 1.000 (n = 14)
- Q1: agreement 1.000, macro-F1 1.000 (n = 8)
- Q2: agreement 1.000, macro-F1 1.000 (n = 1)
- Q3: agreement 1.000, macro-F1 1.000 (n = 7)
- Q4: agreement 0.633, macro-F1 0.612 (n = 30)

## Faithfulness, review flags and reproducibility

- Yes/no answers whose quote failed verification: 0.000
- By question: G1 0.000 (0 of 150); G2 0.000 (0 of 142); R1 0.000 (0 of 149); R2 0.000 (0 of 150); Q1 0.000 (0 of 125); Q2 0.000 (0 of 106); Q3 0.000 (0 of 51); Q4 0.000 (0 of 124)
- Charts flagged for human review by the verification rule: 0
- Unparseable responses: 0
- Median per-chart score SD across extraction runs, M5: 0.000 (n = 150)
- Median per-chart SD of verbalized confidence across runs, M1: 0.005 (n = 150)

## Fitted weights (M5, fitted on dev)

| Feature | Weight |
|---|---|
| intercept | -3.084 |
| Q1_yes | -2.840 |
| Q1_no | 0.000 |
| Q2_yes | -0.143 |
| Q2_no | -1.472 |
| Q3_yes | 0.801 |
| Q3_no | -10.431 |
| Q4_yes | 12.538 |
| Q4_no | 0.000 |

C = 316.2277660168379; grid extended: False; still at grid edge: False; training charts: 101 (81 positive).

## Pre-registered checks

| Check | Result |
|---|---|
| H1 macro-F1 >= 0.90 and 'no' recall >= 0.90 on every question | True |
| H2 quote failures <= 5% | True |
| H3 M5 median SD <= 0.05 and below M1 | True |
| H4 M5 AUROC >= M2 AUROC - 0.02 and M5 ECE <= M2 ECE | True |
| H5 M5 beats each of M6, M7, M8 on ECE or AUROC | {'M6': False, 'M7': False, 'M8': True} |
| Kill criterion: M5 worse than M2 on both AUROC and ECE | not triggered |
| Kill criterion: a gate question below 0.90 macro-F1 or 'no' recall | not triggered |

## Usage

1500 extraction and verbal calls; 2,568,489 input tokens, 1,642,063 output tokens (M6 calls not included).
