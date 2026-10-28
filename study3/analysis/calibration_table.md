# Does high confidence mean high accuracy? (study-3 test split, exploratory)

Each cell: how many of the 200 test charts the method put in that confidence range, the average confidence it gave, and the share of those charts actually supported. Calibrated = 'said' and 'actually' match. ECE is the weighted average gap over ten bins.

## GPT-5.4

| Method | under 10% | 10-50% | 50-90% | 90% and over | ECE |
|---|---|---|---|---|---|
| A own confidence, as stated | — | — | 51 charts: said 86%, actually 73% | 149 charts: said 95%, actually 54% | 0.346 |
| A own confidence, recalibrated | — | 76 charts: said 49%, actually 54% | 124 charts: said 57%, actually 61% | — | 0.046 |
| B our method | 58 charts: said 1%, actually 0% | 8 charts: said 29%, actually 12% | 88 charts: said 80%, actually 83% | 46 charts: said 93%, actually 93% | 0.037 |
| C given the questions | 2 charts: said 2%, actually 0% | 1 charts: said 22%, actually 0% | 6 charts: said 83%, actually 33% | 191 charts: said 97%, actually 60% | 0.368 |

## Claude Sonnet 5.5

| Method | under 10% | 10-50% | 50-90% | 90% and over | ECE |
|---|---|---|---|---|---|
| A own confidence, as stated | 24 charts: said 5%, actually 0% | 17 charts: said 24%, actually 6% | 120 charts: said 81%, actually 75% | 39 charts: said 93%, actually 67% | 0.143 |
| A own confidence, recalibrated | 29 charts: said 6%, actually 0% | 30 charts: said 33%, actually 43% | 141 charts: said 71%, actually 74% | — | 0.067 |
| B our method | 80 charts: said 1%, actually 2% | 2 charts: said 23%, actually 0% | 1 charts: said 84%, actually 0% | 117 charts: said 97%, actually 98% | 0.021 |
| C given the questions | 49 charts: said 3%, actually 0% | 32 charts: said 21%, actually 3% | 58 charts: said 84%, actually 95% | 61 charts: said 94%, actually 100% | 0.090 |

## Claude Haiku 5.5

| Method | under 10% | 10-50% | 50-90% | 90% and over | ECE |
|---|---|---|---|---|---|
| A own confidence, as stated | 27 charts: said 5%, actually 0% | 34 charts: said 22%, actually 18% | 108 charts: said 78%, actually 85% | 31 charts: said 93%, actually 61% | 0.118 |
| A own confidence, recalibrated | 44 charts: said 5%, actually 0% | 19 charts: said 19%, actually 37% | 131 charts: said 78%, actually 84% | 6 charts: said 90%, actually 0% | 0.111 |
| B our method | 78 charts: said 1%, actually 0% | 3 charts: said 26%, actually 33% | 1 charts: said 86%, actually 0% | 118 charts: said 98%, actually 98% | 0.014 |
| C given the questions | 53 charts: said 4%, actually 0% | 76 charts: said 24%, actually 70% | 35 charts: said 70%, actually 91% | 36 charts: said 94%, actually 89% | 0.234 |

## Gemini 3.8 Flash

| Method | under 10% | 10-50% | 50-90% | 90% and over | ECE |
|---|---|---|---|---|---|
| A own confidence, as stated | — | 3 charts: said 28%, actually 0% | 14 charts: said 84%, actually 14% | 183 charts: said 97%, actually 63% | 0.363 |
| A own confidence, recalibrated | 17 charts: said 7%, actually 12% | 79 charts: said 47%, actually 49% | 104 charts: said 67%, actually 73% | — | 0.108 |
| B our method | 83 charts: said 0%, actually 0% | — | — | 117 charts: said 100%, actually 100% | 0.002 |
| C given the questions | 51 charts: said 0%, actually 0% | 30 charts: said 16%, actually 0% | — | 119 charts: said 96%, actually 98% | 0.036 |

## Gemini 3.5 Flash-Lite

| Method | under 10% | 10-50% | 50-90% | 90% and over | ECE |
|---|---|---|---|---|---|
| A own confidence, as stated | 21 charts: said 0%, actually 5% | 72 charts: said 27%, actually 54% | — | 107 charts: said 99%, actually 72% | 0.248 |
| A own confidence, recalibrated | — | 93 charts: said 35%, actually 43% | 107 charts: said 75%, actually 72% | — | 0.076 |
| B our method | 66 charts: said 1%, actually 6% | 8 charts: said 26%, actually 12% | 82 charts: said 81%, actually 87% | 44 charts: said 93%, actually 93% | 0.050 |
| C given the questions | 95 charts: said 0%, actually 34% | 33 charts: said 37%, actually 61% | 6 charts: said 67%, actually 100% | 66 charts: said 100%, actually 89% | 0.246 |

## Summary: charts given 90% or more

| Model | Method | Charts | Average confidence | Actually supported |
|---|---|---|---|---|
| GPT-5.4 | A own confidence, as stated | 149 | 95% | 54% |
| GPT-5.4 | A own confidence, recalibrated | 0 | — | — |
| GPT-5.4 | B our method | 46 | 93% | 93% |
| GPT-5.4 | C given the questions | 191 | 97% | 60% |
| Claude Sonnet 5.5 | A own confidence, as stated | 39 | 93% | 67% |
| Claude Sonnet 5.5 | A own confidence, recalibrated | 0 | — | — |
| Claude Sonnet 5.5 | B our method | 117 | 97% | 98% |
| Claude Sonnet 5.5 | C given the questions | 61 | 94% | 100% |
| Claude Haiku 5.5 | A own confidence, as stated | 31 | 93% | 61% |
| Claude Haiku 5.5 | A own confidence, recalibrated | 6 | 90% | 0% |
| Claude Haiku 5.5 | B our method | 118 | 98% | 98% |
| Claude Haiku 5.5 | C given the questions | 36 | 94% | 89% |
| Gemini 3.8 Flash | A own confidence, as stated | 183 | 97% | 63% |
| Gemini 3.8 Flash | A own confidence, recalibrated | 0 | — | — |
| Gemini 3.8 Flash | B our method | 117 | 100% | 100% |
| Gemini 3.8 Flash | C given the questions | 119 | 96% | 98% |
| Gemini 3.5 Flash-Lite | A own confidence, as stated | 107 | 99% | 72% |
| Gemini 3.5 Flash-Lite | A own confidence, recalibrated | 0 | — | — |
| Gemini 3.5 Flash-Lite | B our method | 44 | 93% | 93% |
| Gemini 3.5 Flash-Lite | C given the questions | 66 | 100% | 89% |
