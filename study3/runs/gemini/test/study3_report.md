# Study 3 — gemini-3.8-flash (gemini), test split

Generated 2026-10-28T18:09:20. Charts: 200. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 200 | 0.647 (0.566–0.720) | 0.363 (0.296–0.430) |
| A stated confidence (recalibrated) | 200 | 0.647 (0.566–0.720) | 0.108 (0.064–0.173) |
| B EWC (rubric v3) | 200 | 1.000 (1.000–1.000) | 0.002 (0.001–0.002) |
| C criteria-guided confidence | 200 | 1.000 (1.000–1.000) | 0.036 (0.024–0.050) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 200 | 0.353 | 0.280 to 0.434 |
| B minus C (M9) | 200 | 0.000 | 0.000 to 0.000 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 32 | 18 | 0.536 | 1.000 | 1.000 | 0 | 0 |
| B | 27 | 27 | n/a | n/a | n/a | 0 | 0 |
| C | 21 | 8 | 0.649 | 1.000 | 1.000 | 0 | 0 |
| D | 15 | 6 | 1.000 | 1.000 | 1.000 | 0 | 1 |
| E | 15 | 15 | n/a | n/a | n/a | 0 | 0 |
| F | 26 | 0 | n/a | n/a | n/a | 0 | 0 |
| G | 39 | 30 | 0.470 | 1.000 | 1.000 | 0 | 1 |
| H | 25 | 13 | 0.657 | 1.000 | 1.000 | 0 | 0 |

## Auto-accept view (thresholds chosen on dev for 95% precision, here applied unchanged)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | 1.000 | 1 | 0.01 | 1.000 | 0.009 |
| A stated confidence (recalibrated) | 0.736 | 1 | 0.01 | 1.000 | 0.009 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | 0.332 | 108 | 0.54 | 0.981 | 0.906 |
| B EWC (rubric v3) | 0.009 | 122 | 0.61 | 0.959 | 1.000 |
| M7 B without quote verification | 0.009 | 122 | 0.61 | 0.959 | 1.000 |
| M8 B with two-way answers (yes / not yes) | 0.013 | 121 | 0.60 | 0.967 | 1.000 |
| C criteria-guided confidence | 0.850 | 119 | 0.59 | 0.983 | 1.000 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.890 | 0.095 | 0.094 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.990 | 0.123 | 0.071 |
| M7 | B without quote verification | 1.000 | 0.002 | 0.000 |
| M8 | B with two-way answers (yes / not yes) | 0.988 | 0.002 | 0.015 |
