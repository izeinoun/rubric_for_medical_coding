"""
Study 3 addendum: Claude Sonnet 5.5 (see study3/ADDENDUM_CLAUDE_SONNET.md).

Runs the frozen study-3 pipeline (study3/run_study3.py, unchanged) for model key "claude", with the model name
overridden in memory from the frozen config's claude-opus-5-5 to claude-sonnet-5-5. Weights, Platt map and
thresholds are fitted on dev into study3/runs/claude/weights/; an addendum freeze (study3/FREEZE_CLAUDE.json)
hashes them together with the study-3 freeze; the test split is then evaluated once.

The Anthropic key comes from the environment only. ANTHROPIC_BASE_URL must point to https://api.anthropic.com
for this process (the session environment sets it for Claude Code itself).

  python study3/run_addendum_sonnet.py collect  --split dev
  python study3/run_addendum_sonnet.py evaluate --split dev
  python study3/run_addendum_sonnet.py freeze
  python study3/run_addendum_sonnet.py collect  --split test
  python study3/run_addendum_sonnet.py evaluate --split test
"""

import argparse
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import run_study3 as S  # noqa: E402  frozen, unchanged

MODEL_KEY, MODEL_NAME = "claude", "claude-sonnet-5-5"
FREEZE_CLAUDE = os.path.join(HERE, "FREEZE_CLAUDE.json")
ADDENDUM_FILES = ["study3/ADDENDUM_CLAUDE_SONNET.md", "study3/run_addendum_sonnet.py", "study3/FREEZE.json"]


def setup():
    cfg, rubric, charts = S.setup(os.path.join(HERE, "runs"))
    cfg["models"] = dict(cfg["models"])
    cfg["models"][MODEL_KEY] = dict(cfg["models"][MODEL_KEY], model=MODEL_NAME)
    return cfg, rubric, charts


def addendum_hashes():
    wdir = os.path.join(HERE, "runs", MODEL_KEY, "weights")
    h = {f: S.sha256(os.path.join(ROOT, f)) for f in ADDENDUM_FILES}
    for w in sorted(os.listdir(wdir)):
        h[os.path.relpath(os.path.join(wdir, w), ROOT)] = S.sha256(os.path.join(wdir, w))
    return h


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["collect", "evaluate", "freeze"])
    ap.add_argument("--split", choices=["dev", "test"], default="dev")
    a = ap.parse_args()
    if os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/") != "https://api.anthropic.com":
        sys.exit("Set ANTHROPIC_BASE_URL=https://api.anthropic.com for this process.")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("No ANTHROPIC_API_KEY in the environment.")
    S.require_frozen()  # the study-3 freeze must be unchanged for the addendum, dev included
    cfg, rubric, charts = setup()
    if a.command == "freeze":
        if os.path.exists(FREEZE_CLAUDE):
            sys.exit("Already frozen.")
        with open(FREEZE_CLAUDE, "w") as f:
            json.dump({"frozen_at": dt.datetime.now().isoformat(timespec="seconds"), "model": MODEL_NAME,
                       "hashes": addendum_hashes()}, f, indent=2)
        print("Sonnet addendum frozen. SHA-256:", S.sha256(FREEZE_CLAUDE))
        return
    if a.split == "test":
        if not os.path.exists(FREEZE_CLAUDE):
            sys.exit("Refusing: freeze the Sonnet addendum first.")
        frozen = json.load(open(FREEZE_CLAUDE))["hashes"]
        changed = [k for k, v in frozen.items() if addendum_hashes().get(k) != v]
        if changed:
            sys.exit("Refusing: changed after the addendum freeze:\n  " + "\n  ".join(changed))
        if a.command == "evaluate" and os.path.exists(os.path.join(HERE, f"TEST_DONE_{MODEL_KEY}.json")):
            sys.exit("Refusing: the Sonnet test split was already evaluated.")
    if a.command == "collect":
        for kind in ("extract", "verbal"):
            S.rp.collect_kind(cfg, rubric, charts, MODEL_KEY, a.split, kind)
        S.fu.collect_m9(cfg, rubric, charts, MODEL_KEY, a.split)
    else:
        S.rp.evaluate(cfg, rubric, charts, MODEL_KEY, a.split)
        S.report(cfg, rubric, charts, MODEL_KEY, a.split)


if __name__ == "__main__":
    main()
