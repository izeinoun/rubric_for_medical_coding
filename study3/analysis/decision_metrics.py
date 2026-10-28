"""
Exploratory, post-test: precision, recall and F0.5 for methods A (recalibrated), B and C, for every study-3 model, at
0.5 and at each method's frozen dev-chosen auto-accept threshold. Reads the frozen results only (no model calls).
Charts the verification rule flags for review are never auto-accepted by B, as in the harness.

Run:  python study3/analysis/decision_metrics.py   (writes study3/analysis/decision_metrics.md)
"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S3 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(os.path.dirname(S3), "harness")); sys.path.insert(0, os.path.join(os.path.dirname(S3), "followup"))
import pipeline as P  # noqa: E402

MODELS = [("gpt", "GPT-5.4"), ("claude", "Claude Sonnet 5.5"), ("claude_haiku", "Claude Haiku 5.5"),
          ("gemini", "Gemini 3.8 Flash"), ("gemini_lite", "Gemini 3.5 Flash-Lite")]
METHODS = [("M2", "A own confidence (recalibrated)"), ("M5", "B our method"), ("M9", "C given the questions")]


def m9(model):
    out = {}
    for l in open(os.path.join(S3, "runs", model, "test", "m9.jsonl")):
        r = json.loads(l)
        if r.get("text"):
            obj, _ = P.parse_json(r["text"])
            try:
                out[r["chart_id"]] = min(1.0, max(0.0, float(obj["confidence"]) / 100))
            except Exception:
                pass
    return out


def fmt(x):
    return "n/a" if x is None else f"{x:.3f}"


L = ["# Precision, recall and F0.5 on the study-3 test split (exploratory, post-test)", "",
     "F0.5 weights precision twice as much as recall (a wrongly accepted chart costs more than a missed one). "
     "'Frozen threshold' = chosen on dev for 95% precision and applied unchanged; n/a = no dev threshold reached 95%. "
     "C is not recalibrated, so its 0.5 cut-off is the model's own 50%.", ""]
for key, name in MODELS:
    rows = list(csv.DictReader(open(os.path.join(S3, "runs", key, "test", "predictions.csv"))))
    y = [int(r["label"]) for r in rows]
    review = [r["needs_review"] == "1" for r in rows]
    thr = json.load(open(os.path.join(S3, "runs", key, "weights", "thresholds.json")))["thresholds"]
    thr["M9"] = json.load(open(os.path.join(S3, "runs", key, "weights", "C_threshold.json")))["M9"]
    c9 = m9(key)
    L += [f"## {name} (n = {len(rows)}, {sum(y)} supported)", "",
          "| Method | At 0.5: precision | recall | F0.5 | At frozen threshold: threshold | accepted | precision | recall | F0.5 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for m, label in METHODS:
        p = [c9.get(r["chart_id"], 0.0) if m == "M9" else float(r[m]) for r in rows]
        blk = review if m == "M5" else [False] * len(rows)
        d5 = P.decision_at(p, y, 0.5, blk, beta=0.5)
        dt_ = P.decision_at(p, y, thr.get(m), blk, beta=0.5) if thr.get(m) is not None else None
        acc = sum(1 for x, b in zip(p, blk) if thr.get(m) is not None and x >= thr[m] and not b)
        L.append(f"| {label} | {fmt(d5.get('precision'))} | {fmt(d5.get('recall'))} | {fmt(d5.get('f_beta'))} | "
                 f"{fmt(thr.get(m))} | {acc if dt_ else 0} | {fmt(dt_.get('precision') if dt_ else None)} | "
                 f"{fmt(dt_.get('recall') if dt_ else None)} | {fmt(dt_.get('f_beta') if dt_ else None)} |")
    L.append("")
open(os.path.join(HERE, "decision_metrics.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
