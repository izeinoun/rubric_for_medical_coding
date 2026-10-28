# Study 3 — gpt-5.4-2026-03-05 (gpt), dev split

Generated 2026-10-28T02:58:05. Charts: 150. Dev numbers: B and recalibrated A are out-of-fold (fitted on dev), so mildly optimistic. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 150 | 0.451 (0.358–0.541) | 0.394 (0.318–0.476) |
| A stated confidence (recalibrated) | 150 | 0.542 (0.453–0.638) | 0.061 (0.025–0.141) |
| B EWC (rubric v3) | 150 | 0.919 (0.865–0.962) | 0.051 (0.037–0.108) |
| C criteria-guided confidence | 150 | 0.463 (0.374–0.553) | 0.422 (0.343–0.501) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 150 | 0.377 | 0.266 to 0.479 |
| B minus C (M9) | 150 | 0.457 | 0.358 to 0.561 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 28 | 12 | 0.615 | 0.974 | 0.419 | 1 | 15 |
| B | 18 | 18 | n/a | n/a | n/a | 0 | 0 |
| C | 15 | 7 | 0.750 | 0.929 | 0.170 | 1 | 8 |
| D | 11 | 2 | 0.611 | 0.917 | 0.667 | 3 | 9 |
| E | 9 | 9 | n/a | n/a | n/a | 0 | 0 |
| F | 19 | 0 | n/a | n/a | n/a | 0 | 19 |
| G | 25 | 19 | 0.636 | 0.518 | 0.732 | 7 | 6 |
| H | 25 | 14 | 0.347 | 0.851 | 0.607 | 4 | 11 |

## Auto-accept view (thresholds chosen on dev for 95% precision; on dev they meet the target by construction)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | n/a | 0 | 0.00 | n/a | 0.000 |
| A stated confidence (recalibrated) | n/a | 0 | 0.00 | n/a | 0.000 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | 0.916 | 24 | 0.16 | 0.958 | 0.284 |
| B EWC (rubric v3) | 0.907 | 31 | 0.21 | 0.968 | 0.370 |
| M7 B without quote verification | 0.907 | 31 | 0.21 | 0.968 | 0.370 |
| M8 B with two-way answers (yes / not yes) | 0.894 | 31 | 0.21 | 0.968 | 0.370 |
| C criteria-guided confidence | n/a | 0 | 0.00 | n/a | 0.000 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.628 | 0.392 | 0.391 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.914 | 0.077 | 0.115 |
| M7 | B without quote verification | 0.919 | 0.051 | 0.096 |
| M8 | B with two-way answers (yes / not yes) | 0.910 | 0.056 | 0.100 |
