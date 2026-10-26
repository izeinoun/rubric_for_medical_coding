# EWC pilot — instructions for Claude Code

This repository runs a pre-registered pilot of evidence-weighted confidence (EWC): LLMs answer rubric questions about 200 synthetic outpatient charts (candidate code ICD-10-CM E11.22), code verifies their quotes and scores them, and a report compares the method with baselines.

## Read first

1. `README.md`: the data, labels and scenarios.
2. `PREREGISTRATION.md`: hypotheses, metrics, pass marks and kill criteria. This is the plan of record.
3. `harness/RUNNING.md`: setup, commands and order of work.
4. `CHANGELOG.md`: every change so far.

## Hard rules

- **Never open, collect, evaluate or summarize the test split** (`split = "test"` in `data/charts.jsonl`, or any `--split test` command) until `FREEZE.json` exists and the user explicitly says to run the test. The harness refuses anyway; do not work around it.
- **Do not change the pre-registered parts** without the user's explicit approval: metrics, pass marks, kill criteria, the weight-fitting procedure, the verification rule, the data split. If something looks wrong, explain it and ask.
- **Prompts and the rubric may change on dev only.** For every change: bump `PROMPT_VERSION` in `harness/prompts.py` (or `version` in the rubric file), add a `CHANGELOG.md` entry with the date, what changed, why, and the dev numbers that prompted it, and move the old `harness/runs/<model>/dev` folder to an archive folder before collecting again.
- **API keys come from environment variables only** (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`). Never print them, write them to files, or commit them.
- **Never commit `harness/runs/mock`.** Mock results are meaningless and must not appear in any report.
- **Do not regenerate the charts** (`generate_charts.py`) unless the user asks; the data is fixed for this pilot.
- Before running a full collection, run `python run_pilot.py estimate` and make one test call per model, and report the token usage to the user.

## Working style

- The user is learning the method while running it: explain what each step does and what the results mean, in plain language.
- After each `evaluate`, summarize the report: extraction quality per question (macro-F1, "no" recall), quote failures per question, calibration (ECE, reliability), AUROC, and the pre-registered checks. Point out which charts drive the errors.
- Commit after each meaningful step with a clear message.
