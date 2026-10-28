# Precision, recall and F0.5 on the study-3 test split (exploratory, post-test)

F0.5 weights precision twice as much as recall (a wrongly accepted chart costs more than a missed one). 'Frozen threshold' = chosen on dev for 95% precision and applied unchanged; n/a = no dev threshold reached 95%. C is not recalibrated, so its 0.5 cut-off is the model's own 50%.

## GPT-5.4 (n = 200, 117 supported)

| Method | At 0.5: precision | recall | F0.5 | At frozen threshold: threshold | accepted | precision | recall | F0.5 |
|---|---|---|---|---|---|---|---|---|
| A own confidence (recalibrated) | 0.613 | 0.650 | 0.620 | n/a | 0 | n/a | n/a | n/a |
| B our method | 0.866 | 0.991 | 0.888 | 0.907 | 46 | 0.935 | 0.368 | 0.714 |
| C given the questions | 0.594 | 1.000 | 0.646 | n/a | 0 | n/a | n/a | n/a |

## Claude Sonnet 5.5 (n = 200, 117 supported)

| Method | At 0.5: precision | recall | F0.5 | At frozen threshold: threshold | accepted | precision | recall | F0.5 |
|---|---|---|---|---|---|---|---|---|
| A own confidence (recalibrated) | 0.738 | 0.889 | 0.764 | n/a | 0 | n/a | n/a | n/a |
| B our method | 0.975 | 0.983 | 0.976 | 0.199 | 119 | 0.966 | 0.983 | 0.970 |
| C given the questions | 0.975 | 0.991 | 0.978 | 0.330 | 124 | 0.944 | 1.000 | 0.954 |

## Claude Haiku 5.5 (n = 200, 117 supported)

| Method | At 0.5: precision | recall | F0.5 | At frozen threshold: threshold | accepted | precision | recall | F0.5 |
|---|---|---|---|---|---|---|---|---|
| A own confidence (recalibrated) | 0.803 | 0.940 | 0.827 | n/a | 0 | n/a | n/a | n/a |
| B our method | 0.975 | 0.991 | 0.978 | 0.182 | 120 | 0.967 | 0.991 | 0.972 |
| C given the questions | 0.901 | 0.547 | 0.798 | n/a | 0 | n/a | n/a | n/a |

## Gemini 3.8 Flash (n = 200, 117 supported)

| Method | At 0.5: precision | recall | F0.5 | At frozen threshold: threshold | accepted | precision | recall | F0.5 |
|---|---|---|---|---|---|---|---|---|
| A own confidence (recalibrated) | 0.731 | 0.650 | 0.713 | 0.736 | 1 | 1.000 | 0.009 | 0.041 |
| B our method | 1.000 | 1.000 | 1.000 | 0.009 | 122 | 0.959 | 1.000 | 0.967 |
| C given the questions | 0.983 | 1.000 | 0.987 | 0.850 | 119 | 0.983 | 1.000 | 0.987 |

## Gemini 3.5 Flash-Lite (n = 200, 117 supported)

| Method | At 0.5: precision | recall | F0.5 | At frozen threshold: threshold | accepted | precision | recall | F0.5 |
|---|---|---|---|---|---|---|---|---|
| A own confidence (recalibrated) | 0.720 | 0.658 | 0.706 | n/a | 0 | n/a | n/a | n/a |
| B our method | 0.889 | 0.957 | 0.902 | n/a | 0 | n/a | n/a | n/a |
| C given the questions | 0.903 | 0.556 | 0.802 | n/a | 0 | n/a | n/a | n/a |

