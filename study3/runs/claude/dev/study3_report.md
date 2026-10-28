# Study 3 — claude-sonnet-5-5 (claude), dev split

Generated 2026-10-28T12:37:45. Charts: 150. Dev numbers: B and recalibrated A are out-of-fold (fitted on dev), so mildly optimistic. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 150 | 0.713 (0.622–0.807) | 0.149 (0.104–0.224) |
| A stated confidence (recalibrated) | 150 | 0.707 (0.614–0.801) | 0.100 (0.076–0.175) |
| B EWC (rubric v3) | 150 | 0.977 (0.944–1.000) | 0.029 (0.015–0.058) |
| C criteria-guided confidence | 150 | 0.995 (0.987–1.000) | 0.086 (0.066–0.111) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 150 | 0.270 | 0.172 to 0.369 |
| B minus C (M9) | 150 | -0.018 | -0.051 to 0.003 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 28 | 12 | 0.625 | 0.990 | 1.000 | 1 | 1 |
| B | 18 | 18 | n/a | n/a | n/a | 0 | 1 |
| C | 15 | 7 | 0.696 | 0.929 | 1.000 | 1 | 0 |
| D | 11 | 2 | 1.000 | 1.000 | 1.000 | 0 | 0 |
| E | 9 | 9 | n/a | n/a | n/a | 0 | 0 |
| F | 19 | 0 | n/a | n/a | n/a | 0 | 0 |
| G | 25 | 19 | 0.474 | 1.000 | 0.978 | 0 | 2 |
| H | 25 | 14 | 0.812 | 0.886 | 0.990 | 2 | 1 |

## Auto-accept view (thresholds chosen on dev for 95% precision; on dev they meet the target by construction)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | n/a | 0 | 0.00 | n/a | 0.000 |
| A stated confidence (recalibrated) | n/a | 0 | 0.00 | n/a | 0.000 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | 0.522 | 75 | 0.50 | 0.960 | 0.889 |
| B EWC (rubric v3) | 0.199 | 83 | 0.55 | 0.952 | 0.975 |
| M7 B without quote verification | 0.199 | 83 | 0.55 | 0.952 | 0.975 |
| M8 B with two-way answers (yes / not yes) | 0.862 | 81 | 0.54 | 0.951 | 0.951 |
| C criteria-guided confidence | 0.330 | 82 | 0.55 | 0.963 | 0.975 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.888 | 0.111 | 0.113 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.971 | 0.117 | 0.084 |
| M7 | B without quote verification | 0.977 | 0.029 | 0.027 |
| M8 | B with two-way answers (yes / not yes) | 0.958 | 0.019 | 0.039 |
