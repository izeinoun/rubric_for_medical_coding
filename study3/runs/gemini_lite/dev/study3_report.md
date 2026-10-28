# Study 3 — gemini-3.5-flash-lite (gemini_lite), dev split

Generated 2026-10-28T18:11:12. Charts: 150. Dev numbers: B and recalibrated A are out-of-fold (fitted on dev), so mildly optimistic. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 150 | 0.742 (0.661–0.820) | 0.215 (0.152–0.291) |
| A stated confidence (recalibrated) | 150 | 0.711 (0.616–0.798) | 0.085 (0.051–0.161) |
| B EWC (rubric v3) | 150 | 0.911 (0.854–0.959) | 0.025 (0.021–0.081) |
| C criteria-guided confidence | 150 | 0.773 (0.702–0.843) | 0.212 (0.151–0.285) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 150 | 0.200 | 0.106 to 0.304 |
| B minus C (M9) | 150 | 0.138 | 0.068 to 0.206 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 28 | 12 | 0.945 | 0.919 | 0.909 | 3 | 3 |
| B | 18 | 18 | n/a | n/a | n/a | 0 | 8 |
| C | 15 | 7 | 0.848 | 1.000 | 0.857 | 0 | 4 |
| D | 11 | 2 | 0.278 | 1.000 | 1.000 | 0 | 0 |
| E | 9 | 9 | n/a | n/a | n/a | 0 | 2 |
| F | 19 | 0 | n/a | n/a | n/a | 2 | 1 |
| G | 25 | 19 | 0.724 | 0.456 | 0.579 | 5 | 12 |
| H | 25 | 14 | 0.711 | 0.812 | 0.640 | 3 | 9 |

## Auto-accept view (thresholds chosen on dev for 95% precision; on dev they meet the target by construction)

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
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.692 | 0.281 | 0.295 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.921 | 0.096 | 0.110 |
| M7 | B without quote verification | 0.905 | 0.061 | 0.077 |
| M8 | B with two-way answers (yes / not yes) | 0.909 | 0.039 | 0.078 |
