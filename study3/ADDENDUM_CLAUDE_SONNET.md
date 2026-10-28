# Study 3 addendum: Claude Sonnet 5.5 (planned; not started)

Written 2026-10-28, before any Claude Sonnet 5.5 call on study-3 charts. It extends `study3/PREREGISTRATION.md` to a third model and changes nothing else.

## Why
Many users run Claude models; the pre-registration tested GPT-5.4 and Gemini 3.8 Flash only. Sonnet 5.5 was chosen over Opus 5.5 by the study lead: widely used in production and about half the price ($2 / $10 per million input / output tokens).

## What stays the same
The 350 charts, the dev/test split, rubric v3, prompts, the runner, the fitting procedure, metrics, hypotheses H1–H4 and their pass marks, and the secondary views. All files hashed in `study3/FREEZE.json` stay unchanged.

## What is added
- Model `claude-sonnet-5-5` through the harness's Anthropic provider (unchanged). The frozen `config.json` lists `claude-opus-5-5`, so the model name is overridden in memory for this addendum only, as with concurrency. Sonnet 5.5 thinks adaptively by default; the provider sends no thinking or effort settings, so the API defaults apply (effort `high`).
- A dev run (150 charts) to fit Sonnet's weights, Platt map and thresholds, exactly as for the other two models; then an addendum freeze hashing those files; then the test run (200 charts), evaluated once.

## Stated in advance
- **Same-model risk:** the charts and phrase banks were written with Claude. Sonnet's results are reported with this caveat; GPT-5.4 and Gemini 3.8 Flash remain the independent tests.
- **Cost estimate:** roughly $35–65 for dev and test together (thinking tokens are billed as output).
- **Prerequisite:** an Anthropic API key in the environment (`ANTHROPIC_API_KEY`), billed through the Anthropic Console.
