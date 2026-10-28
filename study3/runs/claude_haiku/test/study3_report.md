# Study 3 — claude-haiku-5-5 (claude_haiku), test split

Generated 2026-10-28T15:29:51. Charts: 200. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 200 | 0.772 (0.689–0.847) | 0.118 (0.091–0.176) |
| A stated confidence (recalibrated) | 200 | 0.772 (0.689–0.847) | 0.111 (0.081–0.165) |
| B EWC (rubric v3) | 200 | 0.994 (0.981–1.000) | 0.014 (0.007–0.035) |
| C criteria-guided confidence | 200 | 0.917 (0.859–0.964) | 0.234 (0.199–0.290) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 200 | 0.222 | 0.147 to 0.305 |
| B minus C (M9) | 200 | 0.077 | 0.031 to 0.131 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 32 | 18 | 0.857 | 1.000 | 0.855 | 1 | 11 |
| B | 27 | 27 | n/a | n/a | n/a | 1 | 10 |
| C | 21 | 8 | 0.716 | 1.000 | 0.846 | 0 | 4 |
| D | 15 | 6 | 1.000 | 1.000 | 0.944 | 0 | 5 |
| E | 15 | 15 | n/a | n/a | n/a | 0 | 4 |
| F | 26 | 0 | n/a | n/a | n/a | 0 | 0 |
| G | 39 | 30 | 0.528 | 1.000 | 0.883 | 0 | 19 |
| H | 25 | 13 | 0.673 | 0.974 | 0.878 | 2 | 7 |

## Auto-accept view (thresholds chosen on dev for 95% precision, here applied unchanged)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | n/a | 0 | 0.00 | n/a | 0.000 |
| A stated confidence (recalibrated) | n/a | 0 | 0.00 | n/a | 0.000 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | 0.332 | 110 | 0.55 | 0.964 | 0.906 |
| B EWC (rubric v3) | 0.182 | 120 | 0.60 | 0.967 | 0.991 |
| M7 B without quote verification | 0.182 | 121 | 0.60 | 0.967 | 1.000 |
| M8 B with two-way answers (yes / not yes) | 0.228 | 123 | 0.61 | 0.943 | 0.991 |
| C criteria-guided confidence | n/a | 0 | 0.00 | n/a | 0.000 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.879 | 0.111 | 0.108 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.982 | 0.117 | 0.075 |
| M7 | B without quote verification | 0.994 | 0.010 | 0.014 |
| M8 | B with two-way answers (yes / not yes) | 0.989 | 0.014 | 0.033 |
