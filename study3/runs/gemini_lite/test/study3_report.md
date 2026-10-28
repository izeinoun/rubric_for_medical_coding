# Study 3 — gemini-3.5-flash-lite (gemini_lite), test split

Generated 2026-10-28T18:24:27. Charts: 200. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 200 | 0.692 (0.621–0.767) | 0.248 (0.188–0.310) |
| A stated confidence (recalibrated) | 200 | 0.692 (0.621–0.767) | 0.076 (0.039–0.143) |
| B EWC (rubric v3) | 200 | 0.897 (0.843–0.944) | 0.050 (0.033–0.094) |
| C criteria-guided confidence | 200 | 0.779 (0.720–0.835) | 0.246 (0.190–0.305) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 200 | 0.205 | 0.126 to 0.282 |
| B minus C (M9) | 200 | 0.119 | 0.055 to 0.185 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 32 | 18 | 0.909 | 0.982 | 0.851 | 1 | 8 |
| B | 27 | 27 | n/a | n/a | n/a | 1 | 12 |
| C | 21 | 8 | 0.870 | 0.938 | 0.938 | 1 | 2 |
| D | 15 | 6 | 1.000 | 1.000 | 0.843 | 0 | 2 |
| E | 15 | 15 | n/a | n/a | n/a | 0 | 5 |
| F | 26 | 0 | n/a | n/a | n/a | 0 | 4 |
| G | 39 | 30 | 0.702 | 0.456 | 0.641 | 11 | 19 |
| H | 25 | 13 | 0.696 | 0.718 | 0.683 | 5 | 7 |

## Auto-accept view (thresholds chosen on dev for 95% precision, here applied unchanged)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | n/a | 0 | 0.00 | n/a | 0.000 |
| A stated confidence (recalibrated) | n/a | 0 | 0.00 | n/a | 0.000 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | n/a | 0 | 0.00 | n/a | 0.000 |
| B EWC (rubric v3) | n/a | 0 | 0.00 | n/a | 0.000 |
| M7 B without quote verification | n/a | 0 | 0.00 | n/a | 0.000 |
| M8 B with two-way answers (yes / not yes) | n/a | 0 | 0.00 | n/a | 0.000 |
| C criteria-guided confidence | n/a | 0 | 0.00 | n/a | 0.000 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.650 | 0.326 | 0.327 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.879 | 0.149 | 0.155 |
| M7 | B without quote verification | 0.919 | 0.041 | 0.069 |
| M8 | B with two-way answers (yes / not yes) | 0.894 | 0.029 | 0.097 |
