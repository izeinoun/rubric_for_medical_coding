# Study 3 — gpt-5.4-2026-03-05 (gpt), dev split

Generated 2026-10-28T00:42:43. Charts: 150. Dev numbers: B and recalibrated A are out-of-fold (fitted on dev), so mildly optimistic. The harness report for the same charts is report.md.

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
