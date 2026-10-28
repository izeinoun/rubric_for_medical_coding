"""
Study 3 runner: methods A (stated confidence), B (EWC with rubric v3) and C (criteria-guided confidence) on the
350 study-3 charts, dev 150 / test 200. See study3/SPEC.md.

Uses the pilot harness (harness/*.py) unchanged, pointed at study3/data/charts.jsonl, study3/rubric_e1122_v3.json
and study3/runs/. Method C reuses the follow-up's prompt code (followup/run_transfer.py), so its criteria are the
same rubric-v3 questions and guidance that method B uses.

Commands (from the repository root):
  python study3/run_study3.py estimate --split dev
  python study3/run_study3.py collect  --model gpt --split dev      extraction, verbal and C calls (resumable)
  python study3/run_study3.py evaluate --model gpt --split dev      fits weights, Platt map and thresholds on dev
  python study3/run_study3.py freeze                               after dev work: hashes into study3/FREEZE.json
  python study3/run_study3.py collect/evaluate ... --split test    only when frozen; evaluate runs once per model
Mock testing: add --model mock --runs-dir <scratch> (never inside the repository).
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))
sys.path.insert(0, os.path.join(ROOT, "followup"))
import pipeline as P       # noqa: E402  unchanged
import prompts             # noqa: E402  unchanged
import run_pilot as rp     # noqa: E402  unchanged
import run_transfer as fu  # noqa: E402  method C prompt and collector (unchanged)

DATA = os.path.join(HERE, "data", "charts.jsonl")
RUBRIC = os.path.join(HERE, "rubric_e1122_v3.json")
FREEZE = os.path.join(HERE, "FREEZE.json")
FROZEN_FILES = ["study3/data/charts.jsonl", "study3/rubric_e1122_v3.json", "study3/run_study3.py",
                "study3/build_data.py", "study3/check_data.py", "study3/PREREGISTRATION.md",
                "harness/pipeline.py", "harness/prompts.py", "harness/providers.py", "harness/run_pilot.py",
                "harness/config.json", "followup/run_transfer.py"]
NAMES = {"M1": "A stated confidence (raw)", "M2": "A stated confidence (recalibrated)", "M5": "B EWC (rubric v3)",
         "M9": "C criteria-guided confidence"}
HEADLINE = ["M1", "M2", "M5", "M9"]


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def setup(runs_dir):
    cfg, _ = rp.load_cfg()
    cfg = dict(cfg, runs_dir=os.path.abspath(runs_dir), concurrency=fu.CONCURRENCY)
    with open(RUBRIC) as f:
        rubric = json.load(f)
    with open(DATA) as f:
        charts = {c["chart_id"]: c for c in map(json.loads, f)}
    rp.ROOT = HERE  # keeps the harness's one-evaluation marker for test inside study3/, apart from the pilot's
    return cfg, rubric, charts


def frozen_hashes():
    return {f: sha256(os.path.join(ROOT, f)) for f in FROZEN_FILES} | {
        os.path.relpath(os.path.join(HERE, "runs", m, "weights", w), ROOT): sha256(os.path.join(HERE, "runs", m, "weights", w))
        for m in ("gpt", "gemini") if os.path.isdir(os.path.join(HERE, "runs", m, "weights"))
        for w in sorted(os.listdir(os.path.join(HERE, "runs", m, "weights")))}


def require_frozen():
    if not os.path.exists(FREEZE):
        sys.exit("Refusing: the test split needs study 3 to be frozen (python study3/run_study3.py freeze).")
    with open(FREEZE) as f:
        frozen = json.load(f)["hashes"]
    now = frozen_hashes()
    changed = [k for k, v in frozen.items() if now.get(k) != v]
    if changed:
        sys.exit("Refusing: these files changed after the study-3 freeze:\n  " + "\n  ".join(changed))


def cmd_estimate(cfg, rubric, charts, split):
    ids = [c for c, v in charts.items() if v["split"] == split]
    ex = np.mean([len(prompts.EXTRACT_SYSTEM) + len(prompts.extract_user(rubric, charts[c]["text"])) for c in ids])
    vb = np.mean([len(prompts.VERBAL_SYSTEM) + len(prompts.verbal_user(rubric, charts[c]["text"])) for c in ids])
    m9 = np.mean([len(fu.M9_SYSTEM) + len(fu.m9_user(rubric, charts[c]["text"])) for c in ids])
    per = (ex * cfg["extraction_runs"] + vb * cfg["verbal_runs"] + m9 * fu.M9_RUNS) / 4
    calls = len(ids) * (cfg["extraction_runs"] + cfg["verbal_runs"] + fu.M9_RUNS)
    print(f"{split}: {len(ids)} charts, about {calls} calls and {per * len(ids) / 1e6:.2f}M input tokens per model "
          f"(plus output, and Gemini's thinking tokens)")


def report(cfg, rubric, charts, model, split):
    """Study-3 summary from the harness's predictions (dev: out-of-fold B and A recalibrated) plus method C."""
    out = rp.run_dir(cfg, model, split)
    import csv
    rows = list(csv.DictReader(open(os.path.join(out, "predictions.csv"))))
    m9 = fu.m9_view(cfg, model, split)
    probs = {m: {r["chart_id"]: float(r[m]) for r in rows if r.get(m)} for m in ("M1", "M2", "M5")}
    probs["M9"] = m9
    ids = [r["chart_id"] for r in rows]
    y = {c: charts[c]["label"] for c in ids}
    res = {"model": model, "model_name": cfg["models"][model]["model"], "split": split,
           "ts": dt.datetime.now().isoformat(timespec="seconds"), "n": len(ids), "methods": {}, "paired": {}, "families": {}}
    for m in HEADLINE:
        c = [x for x in ids if x in probs[m]]
        p, yy = [probs[m][x] for x in c], [y[x] for x in c]
        res["methods"][m] = {"n": len(c), "AUROC": P.auroc(p, yy), "AUROC_CI": P.bootstrap_ci(P.auroc, p, yy, cfg["bootstrap"], cfg["seed"]),
                             "ECE": P.ece(p, yy), "ECE_CI": P.bootstrap_ci(P.ece, p, yy, cfg["bootstrap"], cfg["seed"])}
    for other in ("M2", "M9"):
        c = [x for x in ids if x in probs["M5"] and x in probs[other]]
        d, lo, hi = fu.paired_auroc_diff([probs["M5"][x] for x in c], [probs[other][x] for x in c], [y[x] for x in c],
                                         cfg["bootstrap"], cfg["seed"])
        res["paired"][f"B minus {NAMES[other].split(' ')[0]} ({other})"] = {"n": len(c), "AUROC_diff": d, "CI": [lo, hi]}
    for fam in sorted({charts[c]["family"] for c in ids}):
        c = [x for x in ids if charts[x]["family"] == fam]
        yy = [y[x] for x in c]
        both = 0 < sum(yy) < len(yy)
        res["families"][fam] = {"n": len(c), "positives": sum(yy),
                                **{f"AUROC_{m}": (P.auroc([probs[m].get(x, 0.5) for x in c], yy) if both else None) for m in ("M2", "M5", "M9")},
                                **{f"wrong_{m}": sum((probs[m].get(x, 0.5) >= 0.5) != (y[x] == 1) for x in c) for m in ("M5", "M9")}}
    with open(os.path.join(out, "study3_results.json"), "w") as f:
        json.dump(res, f, indent=2, default=str)
    fmt = fu.fmt
    L = [f"# Study 3 — {res['model_name']} ({model}), {split} split", "",
         f"Generated {res['ts']}. Charts: {res['n']}. "
         + ("Dev numbers: B and recalibrated A are out-of-fold (fitted on dev), so mildly optimistic. " if split == "dev" else "")
         + "The harness report for the same charts is report.md.", "",
         "| Method | n | AUROC (95% CI) | ECE (95% CI) |", "|---|---|---|---|"]
    for m, r in res["methods"].items():
        L.append(f"| {NAMES[m]} | {r['n']} | {fmt(r['AUROC'])} ({fmt(r['AUROC_CI'][0])}–{fmt(r['AUROC_CI'][1])}) | "
                 f"{fmt(r['ECE'])} ({fmt(r['ECE_CI'][0])}–{fmt(r['ECE_CI'][1])}) |")
    L += ["", "C is not recalibrated; compare it on AUROC.", "", "| Paired AUROC difference | n | Difference | 95% CI |", "|---|---|---|---|"]
    for k, r in res["paired"].items():
        L.append(f"| {k} | {r['n']} | {fmt(r['AUROC_diff'])} | {fmt(r['CI'][0])} to {fmt(r['CI'][1])} |")
    L += ["", "| Family | n | Positives | AUROC A | AUROC B | AUROC C | Wrong at 0.5, B | Wrong at 0.5, C |", "|---|---|---|---|---|---|---|---|"]
    for fam, r in res["families"].items():
        L.append(f"| {fam} | {r['n']} | {r['positives']} | {fmt(r['AUROC_M2'])} | {fmt(r['AUROC_M5'])} | {fmt(r['AUROC_M9'])} | "
                 f"{r['wrong_M5']} | {r['wrong_M9']} |")
    with open(os.path.join(out, "study3_report.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"Study 3 report: {os.path.relpath(os.path.join(out, 'study3_report.md'), ROOT)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["estimate", "collect", "evaluate", "freeze"])
    ap.add_argument("--model")
    ap.add_argument("--split", choices=["dev", "test"], default="dev")
    ap.add_argument("--runs-dir", default=os.path.join(HERE, "runs"))
    a = ap.parse_args()
    cfg, rubric, charts = setup(a.runs_dir)
    if a.command == "estimate":
        return cmd_estimate(cfg, rubric, charts, a.split)
    if a.command == "freeze":
        if os.path.exists(FREEZE):
            sys.exit("Already frozen.")
        h = frozen_hashes()
        if not any("/weights/" in k for k in h):
            sys.exit("Nothing to freeze yet: evaluate on dev first so that dev-fitted weights exist.")
        with open(FREEZE, "w") as f:
            json.dump({"frozen_at": dt.datetime.now().isoformat(timespec="seconds"), "hashes": h}, f, indent=2)
        print("Study 3 frozen. Record this SHA-256 somewhere dated:", sha256(FREEZE))
        return
    if a.model not in cfg["models"]:
        sys.exit(f"--model must be one of {list(cfg['models'])}")
    if a.model == "mock" and os.path.abspath(a.runs_dir).startswith(HERE):
        sys.exit("Mock runs must go to a scratch --runs-dir outside the repository.")
    if not rp.key_present(cfg["models"][a.model]["provider"]):
        sys.exit("No API key in the environment for this model.")
    if a.split == "test":
        require_frozen()
        if a.command == "evaluate" and os.path.exists(os.path.join(HERE, f"TEST_DONE_{a.model}.json")):
            sys.exit("Refusing: the study-3 test split was already evaluated for this model.")
    if a.command == "collect":
        for kind in ("extract", "verbal"):
            rp.collect_kind(cfg, rubric, charts, a.model, a.split, kind)
        fu.collect_m9(cfg, rubric, charts, a.model, a.split)
    else:
        rp.evaluate(cfg, rubric, charts, a.model, a.split)
        report(cfg, rubric, charts, a.model, a.split)


if __name__ == "__main__":
    main()
