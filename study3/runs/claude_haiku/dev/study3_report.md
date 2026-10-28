# Study 3 — claude-haiku-5-5 (claude_haiku), dev split

Generated 2026-10-28T15:07:32. Charts: 150. Dev numbers: B and recalibrated A are out-of-fold (fitted on dev), so mildly optimistic. The harness report for the same charts is report.md.

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 150 | 0.839 (0.763–0.910) | 0.127 (0.086–0.183) |
| A stated confidence (recalibrated) | 150 | 0.836 (0.759–0.908) | 0.072 (0.056–0.139) |
| B EWC (rubric v3) | 150 | 0.992 (0.974–1.000) | 0.019 (0.010–0.044) |
| C criteria-guided confidence | 150 | 0.940 (0.888–0.980) | 0.233 (0.189–0.298) |

C is not recalibrated; compare it on AUROC.

| Paired AUROC difference | n | Difference | 95% CI |
|---|---|---|---|
| B minus A (M2) | 150 | 0.155 | 0.085 to 0.232 |
| B minus C (M9) | 150 | 0.052 | 0.014 to 0.100 |

| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |
|---|---|---|---|---|---|---|---|
| A | 28 | 12 | 0.812 | 0.984 | 0.938 | 2 | 7 |
| B | 18 | 18 | n/a | n/a | n/a | 0 | 9 |
| C | 15 | 7 | 0.893 | 1.000 | 0.875 | 0 | 6 |
| D | 11 | 2 | 1.000 | 1.000 | 1.000 | 0 | 2 |
| E | 9 | 9 | n/a | n/a | n/a | 0 | 1 |
| F | 19 | 0 | n/a | n/a | n/a | 0 | 0 |
| G | 25 | 19 | 0.689 | 1.000 | 0.921 | 0 | 13 |
| H | 25 | 14 | 0.838 | 0.951 | 0.847 | 1 | 9 |

## Auto-accept view (thresholds chosen on dev for 95% precision; on dev they meet the target by construction)

| Method | Threshold | Accepted | Coverage | Precision | Recall |
|---|---|---|---|---|---|
| A stated confidence (raw) | n/a | 0 | 0.00 | n/a | 0.000 |
| A stated confidence (recalibrated) | n/a | 0 | 0.00 | n/a | 0.000 |
| M3 Self-consistency | n/a | 0 | 0.00 | n/a | 0.000 |
| M4 B with hand-set expert weights instead of fitted weights | 0.332 | 78 | 0.52 | 0.949 | 0.914 |
| B EWC (rubric v3) | 0.182 | 83 | 0.55 | 0.964 | 0.988 |
| M7 B without quote verification | 0.182 | 83 | 0.55 | 0.964 | 0.988 |
| M8 B with two-way answers (yes / not yes) | 0.228 | 83 | 0.55 | 0.964 | 0.988 |
| C criteria-guided confidence | n/a | 0 | 0.00 | n/a | 0.000 |

## Secondary views (exploratory, same calls, no pass marks)

| View | What it is | AUROC | ECE | Brier |
|---|---|---|---|---|
| M3 | Self-consistency: share of the 5 stated-confidence runs answering 'supported' | 0.893 | 0.113 | 0.112 |
| M4 | B with hand-set expert weights instead of fitted weights | 0.987 | 0.115 | 0.069 |
| M7 | B without quote verification | 0.992 | 0.014 | 0.014 |
| M8 | B with two-way answers (yes / not yes) | 0.980 | 0.022 | 0.030 |
