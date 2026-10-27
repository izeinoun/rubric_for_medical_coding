# Follow-up transfer test — gemini-3.8-flash (gemini), stage 1

Methods: A = the model's stated confidence (raw, and recalibrated with the frozen pilot map); B = EWC; C = the model's confidence when given the rubric's questions and told to use them. The frozen pilot report for the same charts (report.md) also lists the pilot's other variants.

Generated 2026-10-27T22:16:34. Primary analysis set: 73 main-set charts with uncontested labels (12 contested charts are reported separately below). The frozen pilot report for the same charts is in report.md (its 'excluding label_needs_review' table matches the primary set).

## Methods on the main set

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 73 | 0.731 (0.603–0.845) | 0.375 (0.266–0.484) |
| A stated confidence (recalibrated) | 73 | 0.731 (0.603–0.845) | 0.185 (0.108–0.287) |
| B EWC | 73 | 0.979 (0.948–1.000) | 0.031 (0.008–0.084) |
| C criteria-guided confidence | 73 | 0.961 (0.917–0.998) | 0.084 (0.037–0.150) |

Recalibration changes calibration, not ranking, so both rows of A share an AUROC. C is not recalibrated (there is no dev split to fit a map); compare it on AUROC.

## Paired AUROC differences (bootstrap, 95% CI)

| Comparison | n | Difference | 95% CI |
|---|---|---|---|
| B EWC minus A stated confidence (recalibrated) | 73 | 0.248 | 0.130 to 0.381 |
| B EWC minus C criteria-guided confidence | 73 | 0.018 | -0.018 to 0.058 |

## Contested charts (sensitivity analysis)

Copy-forward and list-only CKD lines (scenarios B2, B4, G4). The generator labels them 0 (the frozen rubric's rule: text carried forward that refers only to old results, or a bare list, does not count as addressed); the human review labeled them 1 (MEAT reading: 'continue regimen' or 'stable' counts).

Mean score on contested charts: A stated confidence (raw) 0.967; A stated confidence (recalibrated) 0.428; B EWC 0.132; C criteria-guided confidence 0.371.

| All main-set charts | n | AUROC A stated confidence (raw) | AUROC A stated confidence (recalibrated) | AUROC B EWC | AUROC C criteria-guided confidence | B minus A (95% CI) |
|---|---|---|---|---|---|---|
| contested labeled 0 (generator) | 85 | 0.692 | 0.692 | 0.966 | 0.959 | 0.273 (0.167 to 0.383) |
| contested labeled 1 (reviewer) | 85 | 0.718 | 0.718 | 0.924 | 0.927 | 0.205 (0.075 to 0.349) |

## Frozen auto-accept threshold (B)

Threshold 0.183: 42 charts accepted (coverage 0.58), precision 0.952.

## By family (main set)

| Family | n | Positives | AUROC B | AUROC A | Mean B, label 1 | Mean B, label 0 |
|---|---|---|---|---|---|---|
| A | 24 | 10 | 1.000 | 0.700 | 0.992 | 0.016 |
| B | 7 | 7 | n/a | n/a | 0.989 | n/a |
| C | 12 | 6 | 1.000 | 0.625 | 0.987 | 0.000 |
| D | 9 | 2 | 1.000 | 1.000 | 0.982 | 0.015 |
| E | 7 | 7 | n/a | n/a | 0.998 | n/a |
| G | 14 | 9 | 0.733 | 0.667 | 0.853 | 0.402 |

## Stress test: family F (all label 0, outside the rubric)

| Group | n | Mean A (raw) | Mean A (recalibrated) | Mean B | Mean C | B above frozen threshold |
|---|---|---|---|---|---|---|
| all | 15 | 0.954 | 0.315 | 0.987 | 0.723 | 1.00 |
| F1_non_acceptable_provider | 5 | 0.950 | 0.279 | 0.992 | 0.710 | 1.00 |
| F2_unsigned | 5 | 0.962 | 0.387 | 0.982 | 0.570 | 1.00 |
| F3_not_face_to_face | 5 | 0.950 | 0.279 | 0.988 | 0.890 | 1.00 |

## Technical checks (stage-1 go/no-go; results never count)

1100 calls, 0 errors, 0 unparseable; 1,674,021 input and 1,242,863 output tokens; 16740 input tokens per chart (estimate 14017); quote failure rate 0.000.

| Check | Pass |
|---|---|
| errors <= 2% | True |
| unparseable <= 2% | True |
| quote failures < 50% (not systematic) | True |
| input tokens per chart <= 1.5 x estimate | True |
