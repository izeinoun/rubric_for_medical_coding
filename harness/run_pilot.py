#!/usr/bin/env python3
"""EWC pilot runner.

Commands (run from the harness folder):
  python run_pilot.py check                          config, keys and data sanity
  python run_pilot.py estimate --model gpt           calls and approximate tokens for dev and test
  python run_pilot.py collect  --model gpt --split dev      extraction and verbal-confidence calls (resumable)
  python run_pilot.py evaluate --model gpt --split dev      verify, fit (dev only), score, metrics, report
  python run_pilot.py collect-m6 --model gpt --split dev    ablation M6 (needs weights from evaluate on dev)
  python run_pilot.py freeze                         record hashes of the plan, pipeline, data and weights
  python run_pilot.py collect/evaluate ... --split test     only after freeze; evaluate on test runs once

See RUNNING.md for the full procedure.
"""

import argparse
import datetime as dt
import hashlib
import json
import math
import os
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

import numpy as np

import pipeline as P
import prompts
from providers import key_present, make_provider

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def load_cfg():
    with open(os.path.join(HERE, "config.json")) as f:
        cfg = json.load(f)
    with open(os.path.join(HERE, cfg["rubric_file"])) as f:
        rubric = json.load(f)
    return cfg, rubric


def load_charts(cfg):
    path = os.path.join(HERE, cfg["data_file"])
    with open(path) as f:
        return {c["chart_id"]: c for c in map(json.loads, f)}


def run_dir(cfg, model, split):
    d = os.path.join(HERE, cfg["runs_dir"], model, split)
    os.makedirs(d, exist_ok=True)
    return d


def weights_dir(cfg, model):
    d = os.path.join(HERE, cfg["runs_dir"], model, "weights")
    os.makedirs(d, exist_ok=True)
    return d


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

# --------------------------------------------------------------- freeze guard

FROZEN_FILES = ["PREREGISTRATION.md", "harness/prompts.py", "harness/pipeline.py", "harness/providers.py",
                "harness/run_pilot.py", "harness/config.json"]


def current_hashes(cfg, rubric):
    files = FROZEN_FILES + ["harness/" + cfg["rubric_file"], os.path.relpath(os.path.join(HERE, cfg["data_file"]), ROOT)]
    out = {f: sha256(os.path.join(ROOT, f)) for f in files}
    wroot = os.path.join(HERE, cfg["runs_dir"])
    if os.path.isdir(wroot):
        for m in sorted(os.listdir(wroot)):
            wd = os.path.join(wroot, m, "weights")
            if os.path.isdir(wd):
                for w in sorted(os.listdir(wd)):
                    out[os.path.relpath(os.path.join(wd, w), ROOT)] = sha256(os.path.join(wd, w))
    return out


def require_frozen(cfg, rubric, model):
    fz = os.path.join(ROOT, "FREEZE.json")
    if not os.path.exists(fz):
        sys.exit("Refusing: the test split needs a frozen pipeline. Finish dev work, then run `python run_pilot.py freeze`.")
    with open(fz) as f:
        frozen = json.load(f)["hashes"]
    now = current_hashes(cfg, rubric)
    changed = [k for k, v in frozen.items() if now.get(k) != v]
    if changed:
        sys.exit("Refusing: these files changed after freeze:\n  " + "\n  ".join(changed))
    if not any(k.startswith(f"harness/{cfg['runs_dir']}/{model}/weights/") for k in frozen):
        sys.exit(f"Refusing: no dev-fitted weights for model '{model}' were frozen.")

# --------------------------------------------------------------------- tasks

def tasks_for(cfg, split_ids, kind):
    n = cfg["extraction_runs"] if kind == "extract" else cfg["verbal_runs"] if kind == "verbal" else 1
    return [(cid, r) for cid in split_ids for r in range(n)]


def collect_kind(cfg, rubric, charts, model, split, kind, weights=None):
    spec = cfg["models"][model]
    prov = make_provider(spec, cfg, charts=charts)
    out_path = os.path.join(run_dir(cfg, model, split), f"{kind}.jsonl")
    done = {(r["chart_id"], r["run"]) for r in read_jsonl(out_path) if r.get("text") is not None}
    ids = sorted(c for c, v in charts.items() if v["split"] == split)
    todo = [t for t in tasks_for(cfg, ids, kind) if t not in done]
    if not todo:
        print(f"{kind}: nothing to do ({len(done)} done)")
        return
    system = {"extract": prompts.EXTRACT_SYSTEM, "verbal": prompts.VERBAL_SYSTEM, "m6": prompts.M6_SYSTEM}[kind]

    def user_for(cid):
        t = charts[cid]["text"]
        if kind == "extract":
            return prompts.extract_user(rubric, t)
        if kind == "verbal":
            return prompts.verbal_user(rubric, t)
        return prompts.m6_user(rubric, t, weights)

    def one(task):
        cid, r = task
        try:
            text, usage = prov.complete(system, user_for(cid), task=kind, chart_id=cid, weights=weights)
            obj, err = P.parse_json(text)
            if obj is None:  # one retry on unparseable output
                text, usage2 = prov.complete(system, user_for(cid) + "\n\nReturn valid JSON only.", task=kind,
                                             chart_id=cid, weights=weights)
                usage = {k: (usage.get(k) or 0) + (usage2.get(k) or 0) for k in usage}
                obj, err = P.parse_json(text)
            return {"chart_id": cid, "run": r, "text": text, "parse_error": err, "usage": usage,
                    "model": spec["model"], "prompt_version": prompts.PROMPT_VERSION,
                    "rubric_version": rubric["version"], "ts": dt.datetime.now().isoformat(timespec="seconds")}
        except Exception as e:
            return {"chart_id": cid, "run": r, "text": None, "error": str(e)}

    print(f"{kind}: {len(todo)} calls to {spec['provider']}:{spec['model']} ...")
    n_ok = n_err = 0
    with open(out_path, "a") as f, ThreadPoolExecutor(cfg["concurrency"]) as ex:
        for fut in as_completed([ex.submit(one, t) for t in todo]):
            rec = fut.result()
            f.write(json.dumps(rec) + "\n")
            f.flush()
            n_ok += rec.get("text") is not None
            n_err += rec.get("text") is None
            if (n_ok + n_err) % 100 == 0:
                print(f"  {n_ok + n_err}/{len(todo)}")
    print(f"{kind}: {n_ok} ok, {n_err} errors (rerun the command to retry errors)")


def latest(records):
    """Keep the last successful record per (chart_id, run)."""
    out = {}
    for r in records:
        if r.get("text") is not None:
            out[(r["chart_id"], r["run"])] = r
    return out

# ----------------------------------------------------------------- evaluation

def extraction_view(cfg, rubric, charts, model, split):
    qids = rubric["gates"] + rubric["weighted"]
    recs = latest(read_jsonl(os.path.join(run_dir(cfg, model, split), "extract.jsonl")))
    by_chart = {}
    for (cid, r), rec in recs.items():
        obj, err = P.parse_json(rec["text"])
        raw, problems = P.clean_answers(obj, qids)
        ver, vrec, review = P.verify(raw, charts[cid]["text"], rubric["gates"])
        by_chart.setdefault(cid, {})[r] = {"raw": raw, "verified": ver, "records": vrec, "needs_review": review,
                                           "parse_error": err, "problems": problems, "usage": rec.get("usage", {})}
    return by_chart


def verbal_view(cfg, model, split):
    recs = latest(read_jsonl(os.path.join(run_dir(cfg, model, split), "verbal.jsonl")))
    out = {}
    for (cid, r), rec in recs.items():
        obj, _ = P.parse_json(rec["text"])
        try:
            conf = float(obj["confidence"]) / 100.0
            sup = bool(obj["supported"])
        except Exception:
            conf, sup = None, None
        out.setdefault(cid, {})[r] = {"conf": None if conf is None else min(1, max(0, conf)), "supported": sup,
                                      "usage": rec.get("usage", {})}
    return out


def m6_view(cfg, model, split):
    recs = latest(read_jsonl(os.path.join(run_dir(cfg, model, split), "m6.jsonl")))
    out = {}
    for (cid, _), rec in recs.items():
        obj, _ = P.parse_json(rec["text"])
        try:
            out[cid] = min(1.0, max(0.0, float(obj["probability"])))
        except Exception:
            pass
    return out


def kfold_platt(conf, y, seed=0):
    from sklearn.model_selection import StratifiedKFold
    conf, y = np.asarray(conf), np.asarray(y)
    k = max(2, min(5, int(min((y == 0).sum(), (y == 1).sum()))))
    out = np.zeros(len(y))
    for tr, te in StratifiedKFold(k, shuffle=True, random_state=seed).split(conf, y):
        out[te] = P.apply_platt(P.fit_platt(conf[tr], y[tr]), conf[te])
    return out.tolist()


def fit_variant(rows, rubric, answers_key, two_way, seed):
    """Fit weights on gate-passing dev charts. rows: list of dicts with answers and label."""
    train = [r for r in rows if P.gates_pass(r[answers_key], rubric["gates"])]
    X = [P.encode(r[answers_key], rubric["weighted"], two_way) for r in train]
    y = [r["label"] for r in train]
    model, info = P.fit_weights(X, y, seed=seed)
    table = P.model_to_table(model, P.feature_names(rubric["weighted"], two_way))
    oof = P.out_of_fold(X, y, info["C"], seed=seed)
    oof_map = {r["chart_id"]: float(p) for r, p in zip(train, oof)}
    info.update({"n_train": len(train), "n_pos": int(sum(y))})
    return table, info, oof_map


def evaluate(cfg, rubric, charts, model, split):
    seed = cfg["seed"]
    ids = sorted(c for c, v in charts.items() if v["split"] == split)
    ex = extraction_view(cfg, rubric, charts, model, split)
    vb = verbal_view(cfg, model, split)
    m6 = m6_view(cfg, model, split)
    missing = [c for c in ids if 0 not in ex.get(c, {})]
    if missing:
        sys.exit(f"Missing primary extraction for {len(missing)} charts (e.g. {missing[:3]}). Run collect first.")

    rows = []
    for cid in ids:
        e0 = ex[cid][0]
        rows.append({"chart_id": cid, "label": charts[cid]["label"], "scenario": charts[cid]["scenario"],
                     "flags": charts[cid]["flags"], "intended": charts[cid]["intended_answers"],
                     "ambiguous": charts[cid]["ambiguous_fields"], "raw_full": e0["raw"],
                     "raw": {q: a["answer"] for q, a in e0["raw"].items()}, "verified": e0["verified"],
                     "records": e0["records"], "needs_review": e0["needs_review"]})

    wdir = weights_dir(cfg, model)
    variants = {"M5": ("verified", False), "M7": ("raw", False), "M8": ("verified", True)}
    tables, infos, oof = {}, {}, {}
    if split == "dev":
        for name, (key, tw) in variants.items():
            tables[name], infos[name], oof[name] = fit_variant(rows, rubric, key, tw, seed)
            with open(os.path.join(wdir, f"{name}.json"), "w") as f:
                json.dump({"weights": tables[name], "fit": infos[name], "fitted_on": "dev",
                           "ts": dt.datetime.now().isoformat(timespec="seconds")}, f, indent=2)
        dev_conf = [vb.get(r["chart_id"], {}).get(0, {}).get("conf") for r in rows]
        okc = [(c, r["label"]) for c, r in zip(dev_conf, rows) if c is not None]
        if len({y for _, y in okc}) == 2:
            platt = P.fit_platt([c for c, _ in okc], [y for _, y in okc])
            with open(os.path.join(wdir, "M2_platt.json"), "w") as f:
                json.dump(platt, f, indent=2)
    else:
        for name in variants:
            with open(os.path.join(wdir, f"{name}.json")) as f:
                w = json.load(f)
            tables[name], infos[name] = w["weights"], w["fit"]
        with open(os.path.join(wdir, "M2_platt.json")) as f:
            platt = json.load(f)

    # --- per-method probabilities -------------------------------------------------
    probs = {m: {} for m in ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8"]}
    for r in rows:
        cid = r["chart_id"]
        probs["M4"][cid] = P.score(r["verified"], rubric["expert_weights"], rubric["gates"], rubric["weighted"])[0]
        for name, (key, tw) in variants.items():
            if not P.gates_pass(r[key], rubric["gates"]):
                probs[name][cid] = 0.0
            elif split == "dev":
                probs[name][cid] = oof[name][cid]
            else:
                probs[name][cid] = P.score(r[key], tables[name], rubric["gates"], rubric["weighted"], tw)[0]
        v = vb.get(cid, {})
        if 0 in v and v[0]["conf"] is not None:
            probs["M1"][cid] = v[0]["conf"]
        sups = [x["supported"] for x in v.values() if x["supported"] is not None]
        if sups:
            probs["M3"][cid] = sum(sups) / len(sups)
        if cid in m6:
            probs["M6"][cid] = m6[cid]
    if split == "dev" and probs["M1"]:
        cids = [r["chart_id"] for r in rows if r["chart_id"] in probs["M1"]]
        ys = [charts[c]["label"] for c in cids]
        if len(set(ys)) == 2:
            probs["M2"] = dict(zip(cids, kfold_platt([probs["M1"][c] for c in cids], ys, seed)))
    elif probs["M1"]:
        probs["M2"] = {c: P.apply_platt(platt, [p])[0] for c, p in probs["M1"].items()}

    # --- metrics ------------------------------------------------------------------
    review = {r["chart_id"]: r["needs_review"] for r in rows}
    ewc = {"M4", "M5", "M7", "M8"}

    # --- auto-accept thresholds: chosen on dev, applied unchanged to test ---------------
    tpath = os.path.join(wdir, "thresholds.json")
    if split == "dev":
        thresholds = {}
        for m, pm in probs.items():
            c = [x for x in ids if x in pm]
            if c:
                thresholds[m] = P.threshold_for_precision([pm[x] for x in c], [charts[x]["label"] for x in c],
                                                          cfg["auto_accept_precision"],
                                                          [review[x] if m in ewc else False for x in c])
        with open(tpath, "w") as f:
            json.dump({"target_precision": cfg["auto_accept_precision"], "thresholds": thresholds}, f, indent=2)
    else:
        with open(tpath) as f:
            thresholds = json.load(f)["thresholds"]

    def metrics_for(subset_ids):
        out = {}
        for m, pm in probs.items():
            c = [x for x in subset_ids if x in pm]
            if len(c) < 10:
                continue
            p = [pm[x] for x in c]
            y = [charts[x]["label"] for x in c]
            blk = [review[x] if m in ewc else False for x in c]
            row = {"n": len(c), "ECE": P.ece(p, y), "Brier": P.brier(p, y), "AUROC": P.auroc(p, y),
                   "Coverage@P95": P.coverage_at_precision(p, y, cfg["auto_accept_precision"], blk)}
            n_b = cfg["bootstrap"]
            row["ECE_CI"] = P.bootstrap_ci(P.ece, p, y, n_b, seed)
            row["AUROC_CI"] = P.bootstrap_ci(P.auroc, p, y, n_b, seed)
            row["at_auto_threshold"] = P.decision_at(p, y, thresholds.get(m), blk, beta=0.5)
            row["at_0.5"] = P.decision_at(p, y, 0.5, blk, beta=0.5)
            out[m] = row
        return out

    all_ids = ids
    clean_ids = [c for c in ids if "label_needs_review" not in charts[c]["flags"]]
    met_all, met_clean = metrics_for(all_ids), metrics_for(clean_ids)

    # --- extraction accuracy and faithfulness ---------------------------------------
    qids = rubric["gates"] + rubric["weighted"]
    acc, acc_amb = {}, {}
    for q in qids:
        main = [r for r in rows if q not in r["ambiguous"]]
        amb = [r for r in rows if q in r["ambiguous"]]
        truth = [r["intended"][q] for r in main]
        acc[q] = {"verified": P.class_metrics([r["verified"][q] for r in main], truth),
                  "raw": P.class_metrics([r["raw"][q] for r in main], truth)}
        if amb:
            acc_amb[q] = P.class_metrics([r["verified"][q] for r in amb], [r["intended"][q] for r in amb])
    yn = [(r["records"][q]["status"]) for r in rows for q in qids if r["raw"][q] in ("yes", "no")]
    faith_fail = (sum(s != "verified" for s in yn) / len(yn)) if yn else float("nan")
    faith_by_q = {}
    for q in qids:
        st = [r["records"][q]["status"] for r in rows if r["raw"][q] in ("yes", "no")]
        faith_by_q[q] = {"n_yes_no": len(st), "failed": sum(x != "verified" for x in st),
                         "rate": (sum(x != "verified" for x in st) / len(st)) if st else float("nan")}

    # --- reproducibility --------------------------------------------------------------
    sd_m5, sd_m1 = [], []
    for cid in ids:
        runs = ex.get(cid, {})
        if len(runs) >= 2:
            sc = [P.score(v["verified"], tables["M5"], rubric["gates"], rubric["weighted"])[0] for v in runs.values()]
            sd_m5.append(statistics.pstdev(sc))
        vr = [x["conf"] for x in vb.get(cid, {}).values() if x["conf"] is not None]
        if len(vr) >= 2:
            sd_m1.append(statistics.pstdev(vr))
    repro = {"M5_median_sd": float(np.median(sd_m5)) if sd_m5 else None,
             "M1_median_sd": float(np.median(sd_m1)) if sd_m1 else None,
             "n_charts_M5": len(sd_m5), "n_charts_M1": len(sd_m1)}

    # --- usage ----------------------------------------------------------------------
    tok = {"input": 0, "output": 0, "reasoning": 0, "calls": 0}
    for runs in list(ex.values()) + list(vb.values()):
        for v in runs.values():
            u = v.get("usage") or {}
            tok["input"] += u.get("input_tokens") or 0
            tok["output"] += u.get("output_tokens") or 0
            tok["reasoning"] += u.get("reasoning_tokens") or 0
            tok["calls"] += 1

    # --- hypothesis checks (pre-registration section 6) -----------------------------
    def g(m, k):
        return met_all.get(m, {}).get(k, float("nan"))
    hyp = {
        "H1 macro-F1 >= 0.90 and 'no' recall >= 0.90 on every question": all(
            a["verified"]["macro_f1"] >= 0.90 and (a["verified"]["per_class"]["no"]["support"] == 0
                                                   or a["verified"]["per_class"]["no"]["recall"] >= 0.90)
            for a in acc.values()),
        "H2 quote failures <= 5%": faith_fail <= 0.05,
        "H3 M5 median SD <= 0.05 and below M1": (repro["M5_median_sd"] is not None and repro["M5_median_sd"] <= 0.05
                                                  and (repro["M1_median_sd"] is None or repro["M5_median_sd"] < repro["M1_median_sd"])),
        "H4 M5 AUROC >= M2 AUROC - 0.02 and M5 ECE <= M2 ECE": (g("M5", "AUROC") >= g("M2", "AUROC") - 0.02
                                                                 and g("M5", "ECE") <= g("M2", "ECE")),
        "H5 M5 beats each of M6, M7, M8 on ECE or AUROC": {
            m: (m in met_all) and (g("M5", "ECE") < g(m, "ECE") or g("M5", "AUROC") > g(m, "AUROC"))
            for m in ("M6", "M7", "M8")},
    }
    kill = {
        "M5 worse than M2 on both AUROC and ECE": g("M5", "AUROC") < g("M2", "AUROC") and g("M5", "ECE") > g("M2", "ECE"),
        "a gate question below 0.90 macro-F1 or 'no' recall": any(
            acc[gq]["verified"]["macro_f1"] < 0.90 or (acc[gq]["verified"]["per_class"]["no"]["support"] > 0
                                                       and acc[gq]["verified"]["per_class"]["no"]["recall"] < 0.90)
            for gq in rubric["gates"]),
    }

    result = {"model": model, "model_name": cfg["models"][model]["model"], "split": split,
              "ts": dt.datetime.now().isoformat(timespec="seconds"), "n_charts": len(ids),
              "metrics_all": met_all, "metrics_excluding_needs_review_labels": met_clean,
              "extraction_accuracy": acc, "extraction_accuracy_ambiguous": acc_amb,
              "quote_failure_rate": faith_fail, "quote_failure_by_question": faith_by_q, "needs_review_charts": int(sum(review.values())),
              "parse_errors": sum(1 for c in ex.values() for v in c.values() if v["parse_error"]),
              "reproducibility": repro, "fit": infos, "weights": tables, "tokens": tok,
              "hypotheses": hyp, "kill_criteria": kill}
    out = run_dir(cfg, model, split)
    with open(os.path.join(out, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    with open(os.path.join(out, "predictions.csv"), "w") as f:
        f.write("chart_id,label,scenario,needs_review," + ",".join(probs) + "\n")
        for r in rows:
            f.write(",".join([r["chart_id"], str(r["label"]), r["scenario"], str(int(r["needs_review"]))] +
                             ["" if r["chart_id"] not in probs[m] else f"{probs[m][r['chart_id']]:.4f}" for m in probs]) + "\n")
    write_report(result, probs, charts, out, cfg)
    if split == "test":
        with open(os.path.join(ROOT, f"TEST_DONE_{model}.json"), "w") as f:
            json.dump({"ts": result["ts"]}, f)
    print(f"Report: {os.path.relpath(os.path.join(out, 'report.md'), ROOT)}")

# --------------------------------------------------------------------- report

LABELS = {"M1": "Verbalized confidence", "M2": "M1 + Platt scaling", "M3": "Self-consistency (5 samples)",
          "M4": "EWC, expert weights", "M5": "EWC, fitted weights", "M6": "Ablation: LLM computes score",
          "M7": "Ablation: no quote verification", "M8": "Ablation: two-way answers"}


def fmt(x, d=3):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{d}f}"


def write_report(res, probs, charts, out, cfg):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 5, figsize=(17, 3.6), sharey=True)
    for ax, m in zip(axes, ["M1", "M2", "M3", "M4", "M5"]):
        ax.plot([0, 1], [0, 1], ls="--", lw=1, color="#888")
        pm = probs.get(m, {})
        if pm:
            pts = P.reliability_points([pm[c] for c in pm], [charts[c]["label"] for c in pm])
            ax.scatter([p for p, _, _ in pts], [o for _, o, _ in pts], s=[12 + 3 * n for *_, n in pts], color="#2b6cb0")
            ax.plot([p for p, _, _ in pts], [o for _, o, _ in pts], lw=1, color="#2b6cb0")
        ax.set_title(f"{m}: {LABELS[m]}", fontsize=8)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xlabel("Predicted probability")
    axes[0].set_ylabel("Observed share supported")
    fig.suptitle(f"Reliability diagrams — {res['model_name']}, {res['split']} split (point size = charts in bin)", fontsize=9)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "reliability.png"), dpi=150)
    plt.close(fig)

    L = [f"# EWC pilot report — {res['model_name']} ({res['model']}), {res['split']} split", "",
         f"Generated {res['ts']}. Charts: {res['n_charts']}."]
    if res["split"] == "dev":
        L += ["", "**Development split.** Fitted methods (M2, M5, M7, M8) are scored out-of-fold with C chosen on "
                  "all of dev, so these numbers are mildly optimistic. They are for iteration, not for the paper."]
    if res["model"] == "mock":
        L += ["", "**MOCK PROVIDER. These numbers test the code only and say nothing about any model. Do not report them.**"]
    for title, key in [("All charts", "metrics_all"), ("Excluding charts flagged label_needs_review",
                                                       "metrics_excluding_needs_review_labels")]:
        L += ["", f"## Calibration and discrimination — {title}", "",
              "| Method | n | ECE (95% CI) | Brier | AUROC (95% CI) | Coverage at precision ≥ 0.95 |",
              "|---|---|---|---|---|---|"]
        for m, r in res[key].items():
            L.append(f"| {m} {LABELS[m]} | {r['n']} | {fmt(r['ECE'])} ({fmt(r['ECE_CI'][0])}–{fmt(r['ECE_CI'][1])}) | "
                     f"{fmt(r['Brier'])} | {fmt(r['AUROC'])} ({fmt(r['AUROC_CI'][0])}–{fmt(r['AUROC_CI'][1])}) | "
                     f"{fmt(r['Coverage@P95'], 2)} |")
    L += ["", "## Decisions at operating thresholds (all charts)", "",
          f"Auto-accept threshold: the lowest score giving precision ≥ {cfg['auto_accept_precision']} on dev, applied "
          "unchanged to test. F0.5 weights precision over recall. Charts flagged for review are never auto-accepted."
          + (" On dev the threshold is chosen on these same charts, so dev precision meets the target by construction."
             if res["split"] == "dev" else ""), "",
          "| Method | Threshold | Precision | Recall | F0.5 | Accepted | Precision at 0.5 | Recall at 0.5 | F0.5 at 0.5 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for m, r in res["metrics_all"].items():
        a, h = r["at_auto_threshold"], r["at_0.5"]
        L.append(f"| {m} | {fmt(a['threshold'])} | {fmt(a['precision'])} | {fmt(a['recall'])} | {fmt(a['f_beta'])} | "
                 f"{fmt(a['accepted'], 2)} | {fmt(h['precision'])} | {fmt(h['recall'])} | {fmt(h['f_beta'])} |")
    L += ["", "![Reliability diagrams](reliability.png)", "", "## Extraction quality against intended answers", "",
          "After verification. Plain agreement is shown for reference only; answer types are imbalanced.", "",
          "| Question | Macro-F1 | Recall yes | Recall no | Recall not documented | Precision yes | Precision no | "
          "Agreement | Macro-F1 before verification | n |", "|---|---|---|---|---|---|---|---|---|---|"]
    for q, a in res["extraction_accuracy"].items():
        v, pc = a["verified"], a["verified"]["per_class"]
        def rc(c, k="recall"):
            return fmt(pc[c][k]) + (f" ({pc[c]['support']})" if k == "recall" else "")
        L.append(f"| {q} | {fmt(v['macro_f1'])} | {rc('yes')} | {rc('no')} | {rc('not_documented')} | "
                 f"{rc('yes', 'precision')} | {rc('no', 'precision')} | {fmt(v['agreement'])} | "
                 f"{fmt(a['raw']['macro_f1'])} | {v['n']} |")
    L += ["", "Recall columns show the number of intended answers of that type in parentheses.", "",
          "Confusion matrices (rows = intended answer, columns = model answer after verification):", ""]
    for q, a in res["extraction_accuracy"].items():
        cm = a["verified"]["confusion"]
        L += [f"**{q}**", "", "| intended \\ model | yes | no | not documented |", "|---|---|---|---|"]
        for t in ("yes", "no", "not_documented"):
            L.append(f"| {t} | {cm[t]['yes']} | {cm[t]['no']} | {cm[t]['not_documented']} |")
        L.append("")
    if res["extraction_accuracy_ambiguous"]:
        L += ["Ambiguous fields (two answers defensible), reported separately:", ""]
        for q, a in res["extraction_accuracy_ambiguous"].items():
            L.append(f"- {q}: agreement {fmt(a['agreement'])}, macro-F1 {fmt(a['macro_f1'])} (n = {a['n']})")
    rp = res["reproducibility"]
    L += ["", "## Faithfulness, review flags and reproducibility", "",
          f"- Yes/no answers whose quote failed verification: {fmt(res['quote_failure_rate'])}",
          "- By question: " + "; ".join(f"{q} {fmt(v['rate'])} ({v['failed']} of {v['n_yes_no']})"
                                        for q, v in res["quote_failure_by_question"].items()),
          f"- Charts flagged for human review by the verification rule: {res['needs_review_charts']}",
          f"- Unparseable responses: {res['parse_errors']}",
          f"- Median per-chart score SD across extraction runs, M5: {fmt(rp['M5_median_sd'])} (n = {rp['n_charts_M5']})",
          f"- Median per-chart SD of verbalized confidence across runs, M1: {fmt(rp['M1_median_sd'])} (n = {rp['n_charts_M1']})",
          "", "## Fitted weights (M5, fitted on dev)", "", "| Feature | Weight |", "|---|---|"]
    for k, v in res["weights"].get("M5", {}).items():
        L.append(f"| {k} | {fmt(v)} |")
    fi = res["fit"].get("M5", {})
    L += ["", f"C = {fi.get('C')}; grid extended: {fi.get('grid_extended')}; still at grid edge: {fi.get('still_at_edge')}; "
              f"training charts: {fi.get('n_train')} ({fi.get('n_pos')} positive)."]
    if fi.get("grid_extended"):
        L += ["", "The chosen C reached the edge of the grid: the indicators separate the classes in this data, so the "
                  "weights reflect the penalty rather than measured evidence strength (Appendix A.3, step 5)."]
    L += ["", "## Pre-registered checks", "", "| Check | Result |", "|---|---|"]
    for k, v in res["hypotheses"].items():
        L.append(f"| {k} | {v} |")
    for k, v in res["kill_criteria"].items():
        L.append(f"| Kill criterion: {k} | {'TRIGGERED' if v else 'not triggered'} |")
    t = res["tokens"]
    L += ["", "## Usage", "", f"{t['calls']} extraction and verbal calls; {t['input']:,} input tokens, "
                                 f"{t['output']:,} output tokens including {t.get('reasoning', 0):,} reported "
                                 f"reasoning tokens (M6 calls not included)."]
    with open(os.path.join(out, "report.md"), "w") as f:
        f.write("\n".join(L) + "\n")

# ------------------------------------------------------------------------ CLI

def cmd_check(cfg, rubric, charts):
    print(f"Charts: {len(charts)} (dev {sum(c['split'] == 'dev' for c in charts.values())}, "
          f"test {sum(c['split'] == 'test' for c in charts.values())})")
    for k, spec in cfg["models"].items():
        flag = "key found" if key_present(spec["provider"]) else "NO KEY in environment"
        warn = "  <- set the model name in config.json" if "REPLACE" in spec["model"] else ""
        print(f"  {k:8} {spec['provider']:10} {spec['model']:32} {flag}{warn}")
    print("Frozen:", os.path.exists(os.path.join(ROOT, "FREEZE.json")))


def cmd_estimate(cfg, rubric, charts):
    for split in ("dev", "test"):
        ids = [c for c, v in charts.items() if v["split"] == split]
        ex_in = sum(len(prompts.EXTRACT_SYSTEM) + len(prompts.extract_user(rubric, charts[c]["text"])) for c in ids) / 4
        vb_in = sum(len(prompts.VERBAL_SYSTEM) + len(prompts.verbal_user(rubric, charts[c]["text"])) for c in ids) / 4
        calls = len(ids) * (cfg["extraction_runs"] + cfg["verbal_runs"] + 1)
        tok_in = ex_in * cfg["extraction_runs"] + vb_in * cfg["verbal_runs"] + ex_in * 1.1
        tok_out = len(ids) * (cfg["extraction_runs"] * 450 + cfg["verbal_runs"] * 30 + 480)
        print(f"{split}: about {calls} calls, {tok_in / 1e6:.2f}M input and {tok_out / 1e6:.2f}M output tokens per model "
              f"(output excludes any hidden reasoning tokens)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["check", "estimate", "collect", "collect-m6", "evaluate", "freeze"])
    ap.add_argument("--model")
    ap.add_argument("--split", choices=["dev", "test"], default="dev")
    ap.add_argument("--rerun-test", action="store_true", help="evaluate the test split again (reason must be logged)")
    a = ap.parse_args()
    cfg, rubric = load_cfg()
    charts = load_charts(cfg)

    if a.command == "check":
        return cmd_check(cfg, rubric, charts)
    if a.command == "estimate":
        return cmd_estimate(cfg, rubric, charts)
    if a.command == "freeze":
        h = current_hashes(cfg, rubric)
        if not any("/weights/" in k for k in h):
            sys.exit("Nothing to freeze yet: run evaluate on dev first so that dev-fitted weights exist.")
        with open(os.path.join(ROOT, "FREEZE.json"), "w") as f:
            json.dump({"frozen_at": dt.datetime.now().isoformat(timespec="seconds"), "hashes": h}, f, indent=2)
        print("Frozen. Record this file's SHA-256 somewhere dated:", sha256(os.path.join(ROOT, "FREEZE.json")))
        return

    if not a.model or a.model not in cfg["models"]:
        sys.exit(f"--model must be one of {list(cfg['models'])}")
    spec = cfg["models"][a.model]
    if "REPLACE" in spec["model"]:
        sys.exit(f"Set the model name for '{a.model}' in config.json first.")
    if not key_present(spec["provider"]):
        sys.exit(f"No API key in the environment for {spec['provider']}.")
    if a.split == "test":
        require_frozen(cfg, rubric, a.model)
        if a.command == "evaluate" and os.path.exists(os.path.join(ROOT, f"TEST_DONE_{a.model}.json")) and not a.rerun_test:
            sys.exit("The test split was already evaluated for this model. Use --rerun-test only for a logged reason.")

    if a.command == "collect":
        collect_kind(cfg, rubric, charts, a.model, a.split, "extract")
        collect_kind(cfg, rubric, charts, a.model, a.split, "verbal")
    elif a.command == "collect-m6":
        wpath = os.path.join(weights_dir(cfg, a.model), "M5.json")
        if not os.path.exists(wpath):
            sys.exit("No dev-fitted M5 weights yet: run evaluate on dev first.")
        with open(wpath) as f:
            w = json.load(f)["weights"]
        collect_kind(cfg, rubric, charts, a.model, a.split, "m6", weights=w)
    elif a.command == "evaluate":
        evaluate(cfg, rubric, charts, a.model, a.split)


if __name__ == "__main__":
    main()
