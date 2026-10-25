# Running the EWC pilot

The harness runs the experiment in `PREREGISTRATION.md`: models read the synthetic charts, code verifies quotes and scores, and a report compares the method with the baselines. Everything except the model calls runs locally.

## 1. One-time setup

1. Python 3.10 or newer. From the `harness` folder: `pip install -r requirements.txt`
2. API keys go in environment variables, never in files or chat:
   ```
   export ANTHROPIC_API_KEY=...
   export OPENAI_API_KEY=...
   export GEMINI_API_KEY=...
   ```
3. In `config.json`, replace the placeholder model names for `gpt` and `gemini` with models available on your accounts. Prefer a dated or pinned version name when the provider offers one, so the run can be reproduced. Check the Claude model name too.
4. `python run_pilot.py check` confirms the data, model names and keys.
5. Smoke test with the offline fake model: `python run_pilot.py collect --model mock --split dev`, then `python run_pilot.py evaluate --model mock --split dev`. The report in `runs/mock/dev/` shows the pipeline works. **Its numbers are meaningless**; delete `runs/mock` afterwards.

## 2. Order of work

| Step | Command | Notes |
|---|---|---|
| Freeze the plan | — | Review `PREREGISTRATION.md`, fill in the date, record its SHA-256 somewhere dated |
| Collect on dev | `python run_pilot.py collect --model gpt --split dev` | 5 extraction runs and 5 verbal-confidence runs per chart. Resumable: rerun to retry errors |
| Evaluate on dev | `python run_pilot.py evaluate --model gpt --split dev` | Verifies quotes, fits weights on dev, writes `runs/gpt/dev/report.md` |
| Ablation M6 | `python run_pilot.py collect-m6 --model gpt --split dev`, then evaluate again | Needs the dev-fitted weights |
| Iterate | — | See section 3 |
| Freeze the pipeline | `python run_pilot.py freeze` | Hashes the plan, prompts, code, rubric, data and weights into `FREEZE.json` |
| Test, once | `collect` and `evaluate` with `--split test` | Refused unless frozen and unchanged; evaluate runs once per model |

Run the same steps for each model. The pre-registration requires at least one non-Claude model; running Claude as well shows whether results depend on the model.

## 3. Iterating on dev

- Read `runs/<model>/dev/report.md`, then look at the charts behind the errors: `predictions.csv` lists every chart's scores, and `extract.jsonl` holds the raw model responses.
- Prompt and rubric changes are allowed on dev. For each change: describe it in `CHANGELOG.md` with the dev numbers that prompted it, bump `PROMPT_VERSION` in `prompts.py` (or `version` in the rubric file), move the old `runs/<model>/dev` folder to an archive, and collect again.
- Do not change the fitting procedure, metrics or pass marks; those are fixed by the pre-registration.
- Never open, collect or evaluate the test split before freezing.

## 4. What the outputs mean

| File | Contents |
|---|---|
| `report.md` | Calibration (ECE, Brier), discrimination (AUROC), coverage at 95% precision, extraction accuracy, quote failures, reproducibility, fitted weights, pre-registered checks |
| `reliability.png` | Predicted probability against observed share supported; a calibrated method follows the diagonal |
| `results.json` | Everything in the report, machine-readable |
| `predictions.csv` | Every method's probability for every chart |
| `runs/<model>/weights/` | Dev-fitted weights (M5, M7, M8) and the Platt map (M2) |

Dev numbers for fitted methods are scored out-of-fold and are mildly optimistic. Only test numbers go in the paper.

## 5. Cost

`python run_pilot.py estimate` prints calls and tokens. With the default settings, each model needs about 1,500 calls and 1.4M input plus 0.4M output tokens on dev, and about 660 calls on test. Reasoning models add hidden reasoning tokens on top of that, sometimes many times the visible output, so check a few calls' usage in `extract.jsonl` before running everything. Iteration multiplies the dev cost: each prompt revision is another full dev collection. To keep early iterations cheap, set `extraction_runs` and `verbal_runs` to 1 in `config.json` while drafting prompts, then restore 5 for the final dev run (log both in `CHANGELOG.md`).

## 6. Using Claude Code

Open the `ewc-pilot` folder in Claude Code, make sure your keys are set in the shell it uses, and ask it to run the commands above, read the reports, and help diagnose extraction errors. Keep the rules in section 3: changes on dev only, logged, and no test-split access before freezing.
