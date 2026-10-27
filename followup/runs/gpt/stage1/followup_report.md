# Follow-up transfer test — gpt-5.4-2026-03-05 (gpt), stage 1

Methods: A = the model's stated confidence (raw, and recalibrated with the frozen pilot map); B = EWC; C = the model's confidence when given the rubric's questions and told to use them. The frozen pilot report for the same charts (report.md) also lists the pilot's other variants.

Generated 2026-10-27T22:13:53. Primary analysis set: 73 main-set charts with uncontested labels (12 contested charts are reported separately below). The frozen pilot report for the same charts is in report.md (its 'excluding label_needs_review' table matches the primary set).

## Methods on the main set

| Method | n | AUROC (95% CI) | ECE (95% CI) |
|---|---|---|---|
| A stated confidence (raw) | 73 | 0.470 (0.334–0.603) | 0.381 (0.266–0.497) |
| A stated confidence (recalibrated) | 73 | 0.470 (0.334–0.603) | 0.133 (0.036–0.254) |
| B EWC | 73 | 0.932 (0.869–0.982) | 0.068 (0.022–0.144) |
| C criteria-guided confidence | 73 | 0.441 (0.303–0.575) | 0.406 (0.285–0.527) |

Recalibration changes calibration, not ranking, so both rows of A share an AUROC. C is not recalibrated (there is no dev split to fit a map); compare it on AUROC.

## Paired AUROC differences (bootstrap, 95% CI)

| Comparison | n | Difference | 95% CI |
|---|---|---|---|
| B EWC minus A stated confidence (recalibrated) | 73 | 0.462 | 0.317 to 0.608 |
| B EWC minus C criteria-guided confidence | 73 | 0.491 | 0.348 to 0.645 |

## Contested charts (sensitivity analysis)

Copy-forward and list-only CKD lines (scenarios B2, B4, G4). The generator labels them 0 (the frozen rubric's rule: text carried forward that refers only to old results, or a bare list, does not count as addressed); the human review labeled them 1 (MEAT reading: 'continue regimen' or 'stable' counts).

Mean score on contested charts: A stated confidence (raw) 0.939; A stated confidence (recalibrated) 0.436; B EWC 0.602; C criteria-guided confidence 0.950.

| All main-set charts | n | AUROC A stated confidence (raw) | AUROC A stated confidence (recalibrated) | AUROC B EWC | AUROC C criteria-guided confidence | B minus A (95% CI) |
|---|---|---|---|---|---|---|
| contested labeled 0 (generator) | 85 | 0.471 | 0.471 | 0.883 | 0.504 | 0.412 (0.281 to 0.544) |
| contested labeled 1 (reviewer) | 85 | 0.479 | 0.479 | 0.905 | 0.405 | 0.426 (0.270 to 0.575) |

## Frozen auto-accept threshold (B)

Threshold 0.988: 13 charts accepted (coverage 0.18), precision 0.923.

## By family (main set)

| Family | n | Positives | AUROC B | AUROC A | Mean B, label 1 | Mean B, label 0 |
|---|---|---|---|---|---|---|
| A | 24 | 10 | 1.000 | 0.529 | 0.948 | 0.002 |
| B | 7 | 7 | n/a | n/a | 0.914 | n/a |
| C | 12 | 6 | 0.889 | 0.236 | 0.943 | 0.165 |
| D | 9 | 2 | 1.000 | 0.429 | 0.885 | 0.007 |
| E | 7 | 7 | n/a | n/a | 0.923 | n/a |
| G | 14 | 9 | 0.611 | 0.378 | 0.736 | 0.885 |

## Stress test: family F (all label 0, outside the rubric)

| Group | n | Mean A (raw) | Mean A (recalibrated) | Mean B | Mean C | B above frozen threshold |
|---|---|---|---|---|---|---|
| all | 15 | 0.927 | 0.426 | 0.936 | 0.961 | 0.40 |
| F1_non_acceptable_provider | 5 | 0.950 | 0.445 | 0.940 | 0.968 | 0.40 |
| F2_unsigned | 5 | 0.884 | 0.391 | 0.947 | 0.946 | 0.60 |
| F3_not_face_to_face | 5 | 0.946 | 0.441 | 0.919 | 0.970 | 0.20 |

## Technical checks (stage-1 go/no-go; results never count)

1100 calls, 0 errors, 0 unparseable; 1,554,855 input and 170,916 output tokens; 15549 input tokens per chart (estimate 14017); quote failure rate 0.000.

| Check | Pass |
|---|---|
| errors <= 2% | True |
| unparseable <= 2% | True |
| quote failures < 50% (not systematic) | True |
| input tokens per chart <= 1.5 x estimate | True |
