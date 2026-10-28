# Handoff: running the Claude Sonnet 5.5 addendum in a new session

This session could not see an Anthropic API key (a test request to api.anthropic.com got 401), most likely because the key was added to the environment after the session started. Environment settings apply to new sessions.

## For the study lead
1. In the environment's settings, add the key as an **environment variable named `ANTHROPIC_API_KEY`** (the harness checks for this variable before any Claude call). Never paste it into a chat.
2. Start a new session in the same environment on branch `claude/amazing-hamilton-egd4ds`, and ask it to "run the Claude Sonnet addendum in study3/HANDOFF_SONNET.md".

## For the new session (Claude Code)
- Read `CLAUDE.md`, `study3/PREREGISTRATION.md`, `study3/ADDENDUM_CLAUDE_SONNET.md` and the last entries of `CHANGELOG.md` first.
- Check the key without printing it: `python -c "import os; print(bool(os.environ.get('ANTHROPIC_API_KEY')))"`.
- **Base URL:** this environment sets `ANTHROPIC_BASE_URL` for Claude Code itself. The harness's Anthropic provider (`harness/providers.py`, frozen) builds `anthropic.Anthropic()`, which would pick that up. Run Sonnet with `ANTHROPIC_BASE_URL=https://api.anthropic.com` set for the runner's process only, and log this in `CHANGELOG.md`.
- **Model:** the frozen `harness/config.json` names `claude-opus-5-5`; the addendum overrides it in memory to `claude-sonnet-5-5` (do not edit the frozen file). This needs a small addendum runner (or an option in a new script) that loads the study-3 setup and sets `cfg["models"]["claude"]["model"] = "claude-sonnet-5-5"`.
- Steps: one test call per call type, report tokens and cost to the study lead; dev collect (150 charts) and evaluate (fits Sonnet's weights, Platt map and thresholds under `study3/runs/claude/weights/`); addendum freeze that hashes those files plus the unchanged study-3 freeze; test collect and evaluate once; report with the same-model caveat.
