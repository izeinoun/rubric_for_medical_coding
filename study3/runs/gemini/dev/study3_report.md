# Study 3 — gemini-3.8-flash (gemini), dev split

Generated 2026-10-28T01:16:02. Charts: 150. Dev numbers: B and recalibrated A are out-of-fold (fitted on dev), so mildly optimistic. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 150 | 0.695 (0.614–0.771) | 0.410 (0.332–0.487) |
| A stated confidence (recalibrated) | 150 | 0.676 (0.589–0.759) | 0.047 (0.039–0.134) |
| B EWC (rubric v3) | 150 | 0.987 (0.965–1.000) | 0.013 (0.001–0.033) |
| C criteria-guided confidence | 150 | 0.993 (0.981–1.000) | 0.029 (0.020–0.059) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 150 | 0.310 | 0.225 to 0.401 |
| B minus C (M9) | 150 | -0.006 | -0.024 to 0.008 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 28 | 12 | 0.536 | 0.979 | 0.984 | 2 | 1 |
| B | 18 | 18 | n/a | n/a | n/a | 0 | 0 |
| C | 15 | 7 | 0.402 | 1.000 | 1.000 | 0 | 0 |
| D | 11 | 2 | 1.000 | 1.000 | 0.972 | 0 | 2 |
| E | 9 | 9 | n/a | n/a | n/a | 0 | 0 |
| F | 19 | 0 | n/a | n/a | n/a | 0 | 0 |
| G | 25 | 19 | 0.456 | 1.000 | 1.000 | 0 | 1 |
| H | 25 | 14 | 0.886 | 1.000 | 1.000 | 0 | 0 |
