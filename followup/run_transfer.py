"""
Follow-up transfer test: apply the frozen pilot pipeline, unchanged, to the follow-up charts.

The frozen harness (harness/run_pilot.py, pipeline.py, prompts.py, providers.py, config.json, rubric v2 and the
dev-fitted weights) is imported, never edited. This script only:
  - points it at followup/data/charts.jsonl and an output folder (followup/runs/);
  - runs the charts in two pre-registered stages (stage 1: the 100 charts in stage1_ids.txt; stage 2: the rest);
  - adds the M9 baseline (verbal confidence with the rubric's criteria in the prompt, 1 run per chart);
  - adds the follow-up analyses: paired bootstrap tests (H6, H7), family breakdown, the family F stress test,
    and the stage-1 technical go/no-go checks.

Commands (run from the repository root):
  python followup/run_transfer.py select-stage1                     choose the 100 stage-1 charts (before freeze)
  python followup/run_transfer.py estimate --stage 1                calls and tokens per model
  python followup/run_transfer.py freeze                            hash follow-up files into followup/FREEZE.json
  python followup/run_transfer.py collect  --model gpt --stage 1    extraction, verbal, M6 and M9 calls (resumable)
  python followup/run_transfer.py evaluate --model gpt --stage 1    once per model and stage
  python followup/run_transfer.py evaluate --model gpt --stage all  after stage 2: all 300 charts together

Testing with the offline mock model (results must not be committed):
  python followup/run_transfer.py collect  --model mock --stage 1 --runs-dir <scratch> --weights-from gpt --no-freeze-check
"""

import argparse
import collections
import datetime as dt
import hashlib
import json
import os
import shutil
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))
import pipeline as P      # noqa: E402  frozen
import prompts            # noqa: E402  frozen
import run_pilot as rp    # noqa: E402  frozen
from providers import make_provider  # noqa: E402  frozen

DATA = os.path.join(HERE, "data", "charts.jsonl")
STAGE1 = os.path.join(HERE, "stage1_ids.txt")
FREEZE = os.path.join(HERE, "FREEZE.json")
STAGE1_SEED = 101
STAGE1_MAIN, STAGE1_STRESS_PER_TYPE = 85, 5
M9_RUNS = 1
CONCURRENCY = 8  # only how many calls run at once; does not affect any result
FOLLOWUP_FILES = ["followup/data/charts.jsonl", "followup/stage1_ids.txt", "followup/run_transfer.py",
                  "followup/generate_charts_v3.py", "followup/check_charts_v3.py", "followup/PREREGISTRATION.md"]

# --------------------------------------------------------------------------- M9 prompt (new, frozen at follow-up freeze)

M9_VERSION = "1"
M9_SYSTEM = """You review outpatient notes for diagnosis-code support in Medicare Advantage risk adjustment.
Consider the criteria listed in the user message.
Return JSON only, with no other text, in this shape:
{"supported": true or false, "confidence": <integer 0-100>}
"confidence" is your probability, in percent, that the note supports reporting the code."""


def m9_user(rubric, note_text):
    qs = []
    for qid in rubric["gates"] + rubric["weighted"]:
        q = rubric["questions"][qid]
        qs.append(f'- {q["text"]} {q["guidance"]}')
    return (f'Does this note support reporting ICD-10-CM {rubric["candidate_code"]} ({rubric["code_description"]}) '
            f'for a risk-adjustment submission?\n\nCRITERIA TO CONSIDER\n' + "\n".join(qs) +
            f'\n\nNOTE\n<<<\n{note_text}>>>')

# --------------------------------------------------------------------------- helpers


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_all():
    with open(DATA) as f:
        return {c["chart_id"]: c for c in map(json.loads, f)}


def stage_ids(charts, stage):
    s1 = [l.strip() for l in open(STAGE1) if l.strip()]
    if stage == "1":
        return s1
    if stage == "2":
        return sorted(set(charts) - set(s1))
    return sorted(charts)


def make_cfg(runs_dir):
    cfg, rubric = rp.load_cfg()
    cfg = dict(cfg)
    cfg["runs_dir"] = os.path.abspath(runs_dir)
    cfg["concurrency"] = CONCURRENCY
    return cfg, rubric


def charts_for(charts, ids, tag):
    """Main-set charts in this stage get split=tag; stress-test charts get split=tag+'F'; the rest 'other'."""
    out = {}
    for cid, c in charts.items():
        c = dict(c)
        if cid in ids:
            c["split"] = tag + "F" if c["family"] == "F" else tag
        else:
            c["split"] = "other"
        out[cid] = c
    return out


def check_pilot_freeze(cfg, rubric, models):
    """The pilot's frozen files and each model's frozen weights must match the pilot FREEZE.json."""
    with open(os.path.join(ROOT, "FREEZE.json")) as f:
        frozen = json.load(f)["hashes"]
    now = rp.current_hashes(rp.load_cfg()[0], rubric)
    changed = [k for k, v in frozen.items() if now.get(k) != v]
    if changed:
        sys.exit("Refusing: pilot files changed since the pilot freeze:\n  " + "\n  ".join(changed))
    for m in models:
        src = os.path.join(ROOT, "harness", "runs", m, "weights")
        for w in sorted(os.listdir(src)):
            key = f"harness/runs/{m}/weights/{w}"
            if frozen.get(key) != sha256(os.path.join(src, w)):
                sys.exit(f"Refusing: {key} does not match the pilot freeze.")


def check_followup_freeze():
    if not os.path.exists(FREEZE):
        sys.exit("Refusing: the follow-up is not frozen. Run `python followup/run_transfer.py freeze` first.")
    with open(FREEZE) as f:
        frozen = json.load(f)["hashes"]
    changed = [k for k, v in frozen.items() if sha256(os.path.join(ROOT, k)) != v]
    if changed:
        sys.exit("Refusing: follow-up files changed after the follow-up freeze:\n  " + "\n  ".join(changed))


def install_weights(cfg, model, weights_from):
    """Copy the frozen pilot weights into this run's weights folder and confirm the copies are identical."""
    src = os.path.join(ROOT, "harness", "runs", weights_from, "weights")
    dst = rp.weights_dir(cfg, model)
    for w in sorted(os.listdir(src)):
        shutil.copyfile(os.path.join(src, w), os.path.join(dst, w))
        assert sha256(os.path.join(src, w)) == sha256(os.path.join(dst, w))
    return dst

# --------------------------------------------------------------------------- stage 1 selection


def cmd_select_stage1(charts):
    if os.path.exists(FREEZE):
        sys.exit("Refusing: stage 1 is part of the follow-up freeze and cannot be re-drawn.")
    import random
    rng = random.Random(STAGE1_SEED)
    by_s = collections.defaultdict(list)
    for c in charts.values():
        by_s[c["scenario"]].append(c["chart_id"])
    main = {s: sorted(v) for s, v in by_s.items() if charts[v[0]]["family"] != "F"}
    total = sum(len(v) for v in main.values())
    quota = {s: len(v) * STAGE1_MAIN / total for s, v in main.items()}
    n = {s: int(q) for s, q in quota.items()}
    for s in sorted(quota, key=lambda s: quota[s] - n[s], reverse=True)[:STAGE1_MAIN - sum(n.values())]:
        n[s] += 1                                            # largest-remainder rounding to exactly 85
    picked = []
    for s in sorted(main):
        picked += rng.sample(main[s], n[s])
    for s in sorted(by_s):
        if charts[by_s[s][0]]["family"] == "F":
            picked += rng.sample(sorted(by_s[s]), STAGE1_STRESS_PER_TYPE)
    picked.sort()
    with open(STAGE1, "w") as f:
        f.write("\n".join(picked) + "\n")
    fam = collections.Counter(charts[c]["family"] for c in picked)
    pos = sum(charts[c]["label"] for c in picked if charts[c]["family"] != "F")
    print(f"stage 1: {len(picked)} charts {dict(sorted(fam.items()))}; main-set positives {pos} of {STAGE1_MAIN}")

# --------------------------------------------------------------------------- collection


def collect_m9(cfg, rubric, charts, model, split):
    spec = cfg["models"][model]
    prov = make_provider(spec, cfg, charts=charts)
    out_path = os.path.join(rp.run_dir(cfg, model, split), "m9.jsonl")
    done = {(r["chart_id"], r["run"]) for r in rp.read_jsonl(out_path) if r.get("text") is not None}
    ids = sorted(c for c, v in charts.items() if v["split"] == split)
    todo = [(c, r) for c in ids for r in range(M9_RUNS) if (c, r) not in done]
    if not todo:
        print(f"m9: nothing to do ({len(done)} done)")
        return

    def one(task):
        cid, r = task
        try:
            user = m9_user(rubric, charts[cid]["text"])
            text, usage = prov.complete(M9_SYSTEM, user, task="verbal", chart_id=cid)  # task only steers the mock
            obj, err = P.parse_json(text)
            if obj is None:
                text, u2 = prov.complete(M9_SYSTEM, user + "\n\nReturn valid JSON only.", task="verbal", chart_id=cid)
                usage = {k: (usage.get(k) or 0) + (u2.get(k) or 0) for k in usage}
                obj, err = P.parse_json(text)
            return {"chart_id": cid, "run": r, "text": text, "parse_error": err, "usage": usage, "model": spec["model"],
                    "m9_version": M9_VERSION, "rubric_version": rubric["version"],
                    "ts": dt.datetime.now().isoformat(timespec="seconds")}
        except Exception as e:
            return {"chart_id": cid, "run": r, "text": None, "error": str(e)}

    print(f"m9: {len(todo)} calls to {spec['provider']}:{spec['model']} ...")
    n_ok = n_err = 0
    with open(out_path, "a") as f, ThreadPoolExecutor(cfg["concurrency"]) as ex:
        for fut in as_completed([ex.submit(one, t) for t in todo]):
            rec = fut.result()
            f.write(json.dumps(rec) + "\n")
            f.flush()
            n_ok += rec.get("text") is not None
            n_err += rec.get("text") is None
    print(f"m9: {n_ok} ok, {n_err} errors (rerun the command to retry errors)")


def cmd_collect(cfg, rubric, charts, model, stage, weights_from):
    tag = f"stage{stage}"
    ids = set(stage_ids(charts, stage))
    wdir = install_weights(cfg, model, weights_from)
    with open(os.path.join(wdir, "M5.json")) as f:
        w = json.load(f)["weights"]
    for split in (tag, tag + "F"):
        ch = charts_for(charts, ids, tag)
        for kind in ("extract", "verbal"):
            rp.collect_kind(cfg, rubric, ch, model, split, kind)
        rp.collect_kind(cfg, rubric, ch, model, split, "m6", weights=w)
        collect_m9(cfg, rubric, ch, model, split)

# --------------------------------------------------------------------------- evaluation


def m9_view(cfg, model, split):
    out = {}
    for (cid, _), rec in rp.latest(rp.read_jsonl(os.path.join(rp.run_dir(cfg, model, split), "m9.jsonl"))).items():
        obj, _ = P.parse_json(rec["text"])
        try:
            out.setdefault(cid, []).append(min(1.0, max(0.0, float(obj["confidence"]) / 100.0)))
        except Exception:
            pass
    return {c: float(np.mean(v)) for c, v in out.items()}


def scores_for(cfg, rubric, charts, model, split):
    """Per-chart probabilities for every method, computed exactly as the frozen evaluate() does on test."""
    wdir = rp.weights_dir(cfg, model)
    tables = {n: json.load(open(os.path.join(wdir, f"{n}.json")))["weights"] for n in ("M5", "M7", "M8")}
    platt = json.load(open(os.path.join(wdir, "M2_platt.json")))
    ex = rp.extraction_view(cfg, rubric, charts, model, split)
    vb = rp.verbal_view(cfg, model, split)
    m6 = rp.m6_view(cfg, model, split)
    m9 = m9_view(cfg, model, split)
    ids = sorted(c for c, v in charts.items() if v["split"] == split)
    variants = {"M5": ("verified", False), "M7": ("raw", False), "M8": ("verified", True)}
    probs = {m: {} for m in ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9"]}
    review = {}
    for cid in ids:
        e0 = ex[cid][0]
        ans = {"verified": e0["verified"], "raw": {q: a["answer"] for q, a in e0["raw"].items()}}
        review[cid] = e0["needs_review"]
        probs["M4"][cid] = P.score(ans["verified"], rubric["expert_weights"], rubric["gates"], rubric["weighted"])[0]
        for name, (key, tw) in variants.items():
            probs[name][cid] = (P.score(ans[key], tables[name], rubric["gates"], rubric["weighted"], tw)[0]
                                if P.gates_pass(ans[key], rubric["gates"]) else 0.0)
        v = vb.get(cid, {})
        if 0 in v and v[0]["conf"] is not None:
            probs["M1"][cid] = v[0]["conf"]
            probs["M2"][cid] = P.apply_platt(platt, [v[0]["conf"]])[0]
        sups = [x["supported"] for x in v.values() if x["supported"] is not None]
        if sups:
            probs["M3"][cid] = sum(sups) / len(sups)
        if cid in m6:
            probs["M6"][cid] = m6[cid]
        if cid in m9:
            probs["M9"][cid] = m9[cid]
    return probs, review, ex


def paired_auroc_diff(pa, pb, y, n=2000, seed=0):
    pa, pb, y = np.asarray(pa), np.asarray(pb), np.asarray(y)
    rng = np.random.default_rng(seed)
    point = P.auroc(pa, y) - P.auroc(pb, y)
    d = []
    for _ in range(n):
        i = rng.integers(0, len(y), len(y))
        if len(set(y[i].tolist())) < 2:
            continue
        d.append(P.auroc(pa[i], y[i]) - P.auroc(pb[i], y[i]))
    return point, float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))


def technical_checks(cfg, model, splits, n_charts, est_tokens_per_chart):
    """Stage-1 go/no-go: technical problems only (pre-registered). Results never count."""
    calls = errors = parse_err = tok_in = tok_out = 0
    for split in splits:
        for kind in ("extract", "verbal", "m6", "m9"):
            recs = rp.read_jsonl(os.path.join(rp.run_dir(cfg, model, split), f"{kind}.jsonl"))
            ok = rp.latest(recs)                      # last successful record per (chart, run)
            tasks = {(r["chart_id"], r["run"]) for r in recs}
            calls += len(tasks)
            errors += len(tasks - set(ok))            # tasks that never succeeded
            for r in ok.values():
                parse_err += bool(r.get("parse_error"))
                u = r.get("usage") or {}
                tok_in += u.get("input_tokens") or 0
                tok_out += u.get("output_tokens") or 0
    return {"calls": calls, "errors": errors, "parse_errors": parse_err, "input_tokens": tok_in,
            "output_tokens": tok_out, "error_rate": errors / calls if calls else float("nan"),
            "parse_error_rate": parse_err / calls if calls else float("nan"),
            "input_tokens_per_chart": tok_in / n_charts, "estimated_input_tokens_per_chart": est_tokens_per_chart}


def estimate_tokens_per_chart(cfg, rubric, charts, ids):
    ex = [len(prompts.EXTRACT_SYSTEM) + len(prompts.extract_user(rubric, charts[c]["text"])) for c in ids]
    vb = [len(prompts.VERBAL_SYSTEM) + len(prompts.verbal_user(rubric, charts[c]["text"])) for c in ids]
    m9 = [len(M9_SYSTEM) + len(m9_user(rubric, charts[c]["text"])) for c in ids]
    per = (np.mean(ex) * (cfg["extraction_runs"] + 1.1) + np.mean(vb) * cfg["verbal_runs"] + np.mean(m9) * M9_RUNS) / 4
    return float(per)


def cmd_estimate(cfg, rubric, charts, stage):
    ids = stage_ids(charts, stage)
    per = estimate_tokens_per_chart(cfg, rubric, charts, ids)
    calls = len(ids) * (cfg["extraction_runs"] + cfg["verbal_runs"] + 1 + M9_RUNS)
    print(f"stage {stage}: {len(ids)} charts, about {calls} calls and {per * len(ids) / 1e6:.2f}M input tokens per model; "
          f"visible output about {len(ids) * (cfg['extraction_runs'] * 450 + (cfg['verbal_runs'] + M9_RUNS) * 30 + 480) / 1e6:.2f}M "
          f"(plus hidden reasoning or thinking tokens)")


def merge_stages(cfg, model):
    """For --stage all: concatenate the stage-1 and stage-2 records into split 'all' / 'allF'."""
    for suffix in ("", "F"):
        dst = rp.run_dir(cfg, model, "all" + suffix)
        for kind in ("extract", "verbal", "m6", "m9"):
            with open(os.path.join(dst, f"{kind}.jsonl"), "w") as out:
                for st in ("stage1", "stage2"):
                    p = os.path.join(rp.run_dir(cfg, model, st + suffix), f"{kind}.jsonl")
                    if os.path.exists(p):
                        out.write(open(p).read())


def cmd_evaluate(cfg, rubric, charts, model, stage):
    tag = "all" if stage == "all" else f"stage{stage}"
    done_flag = os.path.join(cfg["runs_dir"], model, f"EVALUATED_{tag}.json")
    if os.path.exists(done_flag):
        sys.exit(f"Refusing: {tag} was already evaluated for {model} (one evaluation per model and stage).")
    if stage == "all":
        merge_stages(cfg, model)
    ids = set(stage_ids(charts, stage))
    ch = charts_for(charts, ids, tag)

    # 1) the frozen pilot evaluation, unchanged, on the main-set charts of this stage
    rp.evaluate(cfg, rubric, ch, model, tag)

    # 2) follow-up analyses
    probs, review, ex = scores_for(cfg, rubric, ch, model, tag)
    main_ids = sorted(c for c, v in ch.items() if v["split"] == tag)
    y = {c: ch[c]["label"] for c in main_ids}
    with open(os.path.join(rp.weights_dir(cfg, model), "thresholds.json")) as f:
        thr = json.load(f)["thresholds"]
    res = {"model": model, "model_name": cfg["models"][model]["model"], "stage": stage, "n_main": len(main_ids),
           "ts": dt.datetime.now().isoformat(timespec="seconds"), "methods": {}, "paired": {}, "families": {}, "stress": {}}
    for m, pm in probs.items():
        c = [x for x in main_ids if x in pm]
        if len(c) < 10:
            continue
        p, yy = [pm[x] for x in c], [y[x] for x in c]
        res["methods"][m] = {"n": len(c), "AUROC": P.auroc(p, yy), "AUROC_CI": P.bootstrap_ci(P.auroc, p, yy, cfg["bootstrap"], cfg["seed"]),
                             "ECE": P.ece(p, yy), "ECE_CI": P.bootstrap_ci(P.ece, p, yy, cfg["bootstrap"], cfg["seed"])}
    for other in ("M2", "M9"):
        c = [x for x in main_ids if x in probs["M5"] and x in probs[other]]
        if len(c) >= 10:
            d, lo, hi = paired_auroc_diff([probs["M5"][x] for x in c], [probs[other][x] for x in c], [y[x] for x in c],
                                          cfg["bootstrap"], cfg["seed"])
            res["paired"][f"M5 - {other}"] = {"n": len(c), "AUROC_diff": d, "CI": [lo, hi]}
    t5 = thr.get("M5")
    acc = [x for x in main_ids if probs["M5"][x] >= t5 and not review[x]]
    res["frozen_threshold"] = {"threshold": t5, "accepted": len(acc), "coverage": len(acc) / len(main_ids),
                               "precision": (sum(y[x] for x in acc) / len(acc)) if acc else None}
    for fam in sorted({ch[c]["family"] for c in main_ids}):
        c = [x for x in main_ids if ch[x]["family"] == fam]
        yy = [y[x] for x in c]
        res["families"][fam] = {"n": len(c), "positives": sum(yy),
                                "AUROC_M5": P.auroc([probs["M5"][x] for x in c], yy) if 0 < sum(yy) < len(yy) else None,
                                "AUROC_M2": P.auroc([probs["M2"].get(x, 0.5) for x in c], yy) if 0 < sum(yy) < len(yy) else None,
                                "mean_M5_label1": float(np.mean([probs["M5"][x] for x in c if y[x] == 1])) if sum(yy) else None,
                                "mean_M5_label0": float(np.mean([probs["M5"][x] for x in c if y[x] == 0])) if sum(yy) < len(yy) else None}
    # family F stress test: all label 0; how confident is each method that they are supported?
    fprobs, freview, _ = scores_for(cfg, rubric, ch, model, tag + "F")
    fch = ch
    f_ids = sorted(c for c, v in ch.items() if v["split"] == tag + "F")
    for kind in ["all"] + sorted({fch[c]["scenario"] for c in f_ids}):
        c = f_ids if kind == "all" else [x for x in f_ids if fch[x]["scenario"] == kind]
        row = {"n": len(c)}
        for m in ("M1", "M2", "M3", "M5", "M9"):
            v = [fprobs[m][x] for x in c if x in fprobs[m]]
            row[f"mean_{m}"] = float(np.mean(v)) if v else None
        row["share_M5_above_frozen_threshold"] = (sum(fprobs["M5"][x] >= t5 and not freview[x] for x in c) / len(c)) if c else None
        res["stress"][kind] = row
    # technical go/no-go (stage 1)
    est = estimate_tokens_per_chart(cfg, rubric, ch, sorted(ids))
    tech = technical_checks(cfg, model, [tag, tag + "F"], len(ids), est)
    with open(os.path.join(rp.run_dir(cfg, model, tag), "results.json")) as f:
        pilot_style = json.load(f)
    tech["quote_failure_rate"] = pilot_style["quote_failure_rate"]
    tech["go"] = {"errors <= 2%": tech["error_rate"] <= 0.02, "unparseable <= 2%": tech["parse_error_rate"] <= 0.02,
                  "quote failures < 50% (not systematic)": pilot_style["quote_failure_rate"] < 0.5,
                  "input tokens per chart <= 1.5 x estimate": tech["input_tokens_per_chart"] <= 1.5 * est}
    res["technical"] = tech
    out = rp.run_dir(cfg, model, tag)
    with open(os.path.join(out, "followup_results.json"), "w") as f:
        json.dump(res, f, indent=2, default=str)
    write_followup_report(res, out)
    with open(done_flag, "w") as f:
        json.dump({"ts": res["ts"]}, f)
    print(f"Follow-up report: {os.path.relpath(os.path.join(out, 'followup_report.md'), ROOT)}")


def fmt(x, d=3):
    return "n/a" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{d}f}"


def write_followup_report(res, out):
    L = [f"# Follow-up transfer test — {res['model_name']} ({res['model']}), stage {res['stage']}", "",
         f"Generated {res['ts']}. Main-set charts: {res['n_main']}. The frozen pilot report for the same charts is in report.md.", "",
         "## Methods on the main set", "", "| Method | n | AUROC (95% CI) | ECE (95% CI) |", "|---|---|---|---|"]
    for m, r in res["methods"].items():
        L.append(f"| {m} | {r['n']} | {fmt(r['AUROC'])} ({fmt(r['AUROC_CI'][0])}–{fmt(r['AUROC_CI'][1])}) | "
                 f"{fmt(r['ECE'])} ({fmt(r['ECE_CI'][0])}–{fmt(r['ECE_CI'][1])}) |")
    L += ["", "M9 (criteria-informed verbal confidence) is not Platt-scaled: there is no dev split to fit one. Compare it on AUROC.", "",
          "## Paired AUROC differences (bootstrap, 95% CI)", "", "| Comparison | n | Difference | 95% CI |", "|---|---|---|---|"]
    for k, r in res["paired"].items():
        L.append(f"| {k} | {r['n']} | {fmt(r['AUROC_diff'])} | {fmt(r['CI'][0])} to {fmt(r['CI'][1])} |")
    ft = res["frozen_threshold"]
    L += ["", "## Frozen auto-accept threshold (M5)", "",
          f"Threshold {fmt(ft['threshold'])}: {ft['accepted']} charts accepted (coverage {fmt(ft['coverage'], 2)}), "
          f"precision {fmt(ft['precision'])}.", "",
          "## By family (main set)", "", "| Family | n | Positives | AUROC M5 | AUROC M2 | Mean M5, label 1 | Mean M5, label 0 |",
          "|---|---|---|---|---|---|---|"]
    for fam, r in res["families"].items():
        L.append(f"| {fam} | {r['n']} | {r['positives']} | {fmt(r['AUROC_M5'])} | {fmt(r['AUROC_M2'])} | "
                 f"{fmt(r['mean_M5_label1'])} | {fmt(r['mean_M5_label0'])} |")
    L += ["", "## Stress test: family F (all label 0, outside the rubric)", "",
          "| Group | n | Mean M1 | Mean M2 | Mean M3 | Mean M5 | Mean M9 | M5 above frozen threshold |", "|---|---|---|---|---|---|---|---|"]
    for k, r in res["stress"].items():
        L.append(f"| {k} | {r['n']} | {fmt(r['mean_M1'])} | {fmt(r['mean_M2'])} | {fmt(r['mean_M3'])} | {fmt(r['mean_M5'])} | "
                 f"{fmt(r['mean_M9'])} | {fmt(r['share_M5_above_frozen_threshold'], 2)} |")
    t = res["technical"]
    L += ["", "## Technical checks (stage-1 go/no-go; results never count)", "",
          f"{t['calls']} calls, {t['errors']} errors, {t['parse_errors']} unparseable; {t['input_tokens']:,} input and "
          f"{t['output_tokens']:,} output tokens; {fmt(t['input_tokens_per_chart'], 0)} input tokens per chart "
          f"(estimate {fmt(t['estimated_input_tokens_per_chart'], 0)}); quote failure rate {fmt(t['quote_failure_rate'])}.", "",
          "| Check | Pass |", "|---|---|"] + [f"| {k} | {v} |" for k, v in t["go"].items()]
    with open(os.path.join(out, "followup_report.md"), "w") as f:
        f.write("\n".join(L) + "\n")

# --------------------------------------------------------------------------- freeze and main


def cmd_freeze(cfg, rubric):
    if os.path.exists(FREEZE):
        sys.exit("Already frozen.")
    missing = [f for f in FOLLOWUP_FILES if not os.path.exists(os.path.join(ROOT, f))]
    if missing:
        sys.exit(f"Missing before freeze: {missing}")
    check_pilot_freeze(cfg, rubric, ["gpt", "gemini"])
    h = {f: sha256(os.path.join(ROOT, f)) for f in FOLLOWUP_FILES}
    with open(FREEZE, "w") as f:
        json.dump({"frozen_at": dt.datetime.now().isoformat(timespec="seconds"),
                   "pilot_freeze_sha256": sha256(os.path.join(ROOT, "FREEZE.json")), "hashes": h}, f, indent=2)
    print("Follow-up frozen. Record this SHA-256 somewhere dated:", sha256(FREEZE))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["select-stage1", "estimate", "freeze", "collect", "evaluate"])
    ap.add_argument("--model")
    ap.add_argument("--stage", choices=["1", "2", "all"], default="1")
    ap.add_argument("--runs-dir", default=os.path.join(HERE, "runs"))
    ap.add_argument("--weights-from", help="pilot model whose frozen weights to use (default: --model)")
    ap.add_argument("--no-freeze-check", action="store_true", help="only for the offline mock test")
    a = ap.parse_args()
    charts = load_all()
    cfg, rubric = make_cfg(a.runs_dir)
    if a.command == "select-stage1":
        return cmd_select_stage1(charts)
    if a.command == "estimate":
        return cmd_estimate(cfg, rubric, charts, a.stage)
    if a.command == "freeze":
        return cmd_freeze(cfg, rubric)
    if a.model not in cfg["models"]:
        sys.exit(f"--model must be one of {list(cfg['models'])}")
    if a.model == "mock" and os.path.abspath(a.runs_dir).startswith(HERE):
        sys.exit("Mock runs must go to a scratch --runs-dir outside the repository.")
    if a.model != "mock" and a.no_freeze_check:
        sys.exit("--no-freeze-check is only for the mock model.")
    if not rp.key_present(cfg["models"][a.model]["provider"]):
        sys.exit("No API key in the environment for this model.")
    weights_from = a.weights_from or a.model
    if not a.no_freeze_check:
        check_pilot_freeze(cfg, rubric, [weights_from])
        check_followup_freeze()
    if a.command == "collect":
        if a.stage == "all":
            sys.exit("Collect stage 1 or stage 2; 'all' is only for evaluate.")
        cmd_collect(cfg, rubric, charts, a.model, a.stage, weights_from)
    else:
        cmd_evaluate(cfg, rubric, charts, a.model, a.stage)


if __name__ == "__main__":
    main()
