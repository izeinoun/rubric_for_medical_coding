# Study 3 — gpt-5.4-2026-03-05 (gpt), test split

Generated 2026-10-28T03:22:54. Charts: 200. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 200 | 0.407 (0.329–0.482) | 0.346 (0.275–0.416) |
| A stated confidence (recalibrated) | 200 | 0.593 (0.518–0.671) | 0.046 (0.017–0.118) |
| B EWC (rubric v3) | 200 | 0.926 (0.881–0.962) | 0.037 (0.027–0.081) |
| C criteria-guided confidence | 200 | 0.483 (0.404–0.564) | 0.368 (0.301–0.438) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 200 | 0.333 | 0.243 to 0.417 |
| B minus C (M9) | 200 | 0.443 | 0.352 to 0.530 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 32 | 18 | 0.685 | 0.956 | 0.391 | 3 | 14 |
| B | 27 | 27 | n/a | n/a | n/a | 0 | 0 |
| C | 21 | 8 | 0.639 | 1.000 | 0.500 | 0 | 12 |
| D | 15 | 6 | 0.778 | 0.852 | 0.602 | 2 | 9 |
| E | 15 | 15 | n/a | n/a | n/a | 0 | 0 |
| F | 26 | 0 | n/a | n/a | n/a | 0 | 25 |
| G | 39 | 30 | 0.454 | 0.552 | 0.502 | 9 | 9 |
| H | 25 | 13 | 0.244 | 0.853 | 0.689 | 5 | 11 |

## Auto-accept view (thresholds chosen on dev for 95% precision, here applied unchanged)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | n/a | 0 | 0.00 | n/a | 0.000 |
| A stated confidence (recalibrated) | n/a | 0 | 0.00 | n/a | 0.000 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | 0.916 | 34 | 0.17 | 0.941 | 0.274 |
| B EWC (rubric v3) | 0.907 | 46 | 0.23 | 0.935 | 0.368 |
| M7 B without quote verification | 0.907 | 46 | 0.23 | 0.935 | 0.368 |
| M8 B with two-way answers (yes / not yes) | 0.894 | 46 | 0.23 | 0.935 | 0.368 |
| C criteria-guided confidence | n/a | 0 | 0.00 | n/a | 0.000 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.588 | 0.445 | 0.445 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.900 | 0.093 | 0.118 |
| M7 | B without quote verification | 0.926 | 0.037 | 0.078 |
| M8 | B with two-way answers (yes / not yes) | 0.921 | 0.033 | 0.084 |
