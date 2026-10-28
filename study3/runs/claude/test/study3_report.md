# Study 3 — claude-sonnet-5-5 (claude), test split

Generated 2026-10-28T12:59:55. Charts: 200. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 200 | 0.715 (0.627–0.794) | 0.143 (0.097–0.204) |
| A stated confidence (recalibrated) | 200 | 0.715 (0.627–0.794) | 0.067 (0.051–0.131) |
| B EWC (rubric v3) | 200 | 0.987 (0.967–0.999) | 0.021 (0.007–0.042) |
| C criteria-guided confidence | 200 | 0.995 (0.986–1.000) | 0.090 (0.075–0.111) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 200 | 0.272 | 0.193 to 0.360 |
| B minus C (M9) | 200 | -0.008 | -0.025 to 0.003 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 32 | 18 | 0.794 | 0.986 | 1.000 | 2 | 0 |
| B | 27 | 27 | n/a | n/a | n/a | 0 | 0 |
| C | 21 | 8 | 0.764 | 1.000 | 1.000 | 0 | 0 |
| D | 15 | 6 | 1.000 | 1.000 | 1.000 | 0 | 0 |
| E | 15 | 15 | n/a | n/a | n/a | 0 | 0 |
| F | 26 | 0 | n/a | n/a | n/a | 0 | 0 |
| G | 39 | 30 | 0.504 | 0.967 | 0.994 | 1 | 2 |
| H | 25 | 13 | 0.788 | 0.968 | 0.997 | 2 | 2 |

## Auto-accept view (thresholds chosen on dev for 95% precision, here applied unchanged)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | n/a | 0 | 0.00 | n/a | 0.000 |
| A stated confidence (recalibrated) | n/a | 0 | 0.00 | n/a | 0.000 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | 0.522 | 105 | 0.53 | 0.971 | 0.872 |
| B EWC (rubric v3) | 0.199 | 119 | 0.59 | 0.966 | 0.983 |
| M7 B without quote verification | 0.199 | 119 | 0.59 | 0.966 | 0.983 |
| M8 B with two-way answers (yes / not yes) | 0.862 | 120 | 0.60 | 0.958 | 0.983 |
| C criteria-guided confidence | 0.330 | 124 | 0.62 | 0.944 | 1.000 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.873 | 0.104 | 0.112 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.973 | 0.128 | 0.087 |
| M7 | B without quote verification | 0.987 | 0.021 | 0.024 |
| M8 | B with two-way answers (yes / not yes) | 0.983 | 0.027 | 0.036 |
