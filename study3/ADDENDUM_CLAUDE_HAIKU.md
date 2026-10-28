# Study 3 addendum: Claude Haiku 5.5 (written before any Haiku call)

Written 2026-10-28 at the study lead's request. Extends `study3/PREREGISTRATION.md` to a fourth model, exactly as the Sonnet addendum (`study3/ADDENDUM_CLAUDE_SONNET.md`) did, and changes nothing else.

## Why
To test whether the structure (fixed questions, verified quotes, code scoring) lets a much cheaper model do the job: Claude Haiku 5.5 costs $0.10 / $0.50 per million input / output tokens, about 1/20 of Sonnet 5.5.

## Procedure
Same charts, split, rubric v3, prompts, runner and analysis. Model `claude-haiku-5-5` through the unchanged Anthropic provider, under its own model key (`claude_haiku`, runs in `study3/runs/claude_haiku/`), with API defaults (adaptive thinking, effort `medium`). Dev run (150 charts) to fit weights, Platt map and thresholds; addendum freeze (`study3/FREEZE_CLAUDE_HAIKU.json`); test run (200 charts), evaluated once. Hypotheses H1–H4 and pass marks as in the pre-registration.

## Stated in advance
- Same-model risk: the charts were written with Claude.
- Expected cost: about $2–4 for dev and test together.

## Declared deviation (after the test calls, before any dev call)
In test calls, Haiku sometimes copied a raw tab or line break from the note into a JSON string, which the frozen parser rejects ("Invalid control character"); this happened on 1 of 3 extraction attempts on the same chart. For the Haiku runs only, `run_addendum_haiku.py` wraps the parser: a response that fails only with "Invalid control character" is parsed again with `json.loads(..., strict=False)`. Answers and quotes are unchanged; quote verification already normalizes whitespace. Frozen files and the other models are unaffected.
