# Study 3 addendum: Gemini 3.5 Flash-Lite (written before any Flash-Lite call)

Written 2026-10-28 at the study lead's request. Extends `study3/PREREGISTRATION.md` to a cheap Gemini model, as the Haiku addendum did for Claude, and changes nothing else.

## Why
To test, within the Gemini family, whether the structure lets a much cheaper model do the job (the Haiku result: B AUROC 0.994 at about 1/15 of Sonnet's cost).

## Procedure
Same charts, split, rubric v3, prompts, runner and analysis. Model `gemini-3.5-flash-lite` (no dated name is offered, so the version cannot be pinned) through the unchanged Gemini provider (JSON response mode, API-default thinking), under its own model key `gemini_lite` (runs in `study3/runs/gemini_lite/`). Dev run (150 charts) to fit weights, Platt map and thresholds; addendum freeze (`study3/FREEZE_GEMINI_LITE.json`); test run (200 charts), evaluated once. Hypotheses H1–H4 and pass marks as in the pre-registration.

## Declared in advance
- The tolerant JSON parse declared for Haiku (a response failing only with "Invalid control character" is parsed again with `strict=False`) also applies to this model, decided before any call.
- Cost is measured with test calls before the dev run.
