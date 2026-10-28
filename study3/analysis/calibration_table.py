"""
Exploratory, post-test: does high confidence mean high accuracy? For each study-3 model and method, the test charts are
grouped by the confidence the method gave; each group shows how many charts it holds and how often they were actually
supported. A well-calibrated method's groups match their own confidence (charts given 90%+ are supported about 90%+ of the
time; charts given under 10% almost never are). Reads frozen results only (no model calls).

Run:  python study3/analysis/calibration_table.py   (writes study3/analysis/calibration_table.md)
"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S3 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(os.path.dirname(S3), "harness"))
import pipeline as P  # noqa: E402

MODELS = [("gpt", "GPT-5.4"), ("claude", "Claude Sonnet 5.5"), ("claude_haiku", "Claude Haiku 5.5"),
          ("gemini", "Gemini 3.8 Flash"), ("gemini_lite", "Gemini 3.5 Flash-Lite")]
METHODS = [("M1", "A own confidence, as stated"), ("M2", "A own confidence, recalibrated"), ("M5", "B our method"),
           ("M9", "C given the questions")]
BINS = [(0.0, 0.1, "under 10%"), (0.1, 0.5, "10-50%"), (0.5, 0.9, "50-90%"), (0.9, 1.01, "90% and over")]


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


def cell(ps, ys, lo, hi):
    idx = [i for i, p in enumerate(ps) if lo <= p < hi]
    if not idx:
        return "—"
    sup = sum(ys[i] for i in idx) / len(idx)
    avg = sum(ps[i] for i in idx) / len(idx)
    return f"{len(idx)} charts: said {avg:.0%}, actually {sup:.0%}"


L = ["# Does high confidence mean high accuracy? (study-3 test split, exploratory)", "",
     "Each cell: how many of the 200 test charts the method put in that confidence range, the average confidence it gave, "
     "and the share of those charts actually supported. Calibrated = 'said' and 'actually' match. ECE is the weighted "
     "average gap over ten bins.", ""]
summary = []
for key, name in MODELS:
    rows = list(csv.DictReader(open(os.path.join(S3, "runs", key, "test", "predictions.csv"))))
    ys = [int(r["label"]) for r in rows]
    c9 = m9(key)
    L += [f"## {name}", "", "| Method | " + " | ".join(b[2] for b in BINS) + " | ECE |", "|---|" + "---|" * (len(BINS) + 1)]
    for m, label in METHODS:
        ps = [c9.get(r["chart_id"], 0.0) if m == "M9" else float(r[m]) for r in rows]
        L.append(f"| {label} | " + " | ".join(cell(ps, ys, lo, hi) for lo, hi, _ in BINS) + f" | {P.ece(ps, ys):.3f} |")
        hi_idx = [i for i, p in enumerate(ps) if p >= 0.9]
        summary.append((name, label, len(hi_idx), (sum(ys[i] for i in hi_idx) / len(hi_idx)) if hi_idx else None,
                        (sum(ps[i] for i in hi_idx) / len(hi_idx)) if hi_idx else None))
    L.append("")
L += ["## Summary: charts given 90% or more", "", "| Model | Method | Charts | Average confidence | Actually supported |", "|---|---|---|---|---|"]
for name, label, n, sup, avg in summary:
    L.append(f"| {name} | {label} | {n} | {'—' if avg is None else f'{avg:.0%}'} | {'—' if sup is None else f'{sup:.0%}'} |")
open(os.path.join(HERE, "calibration_table.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
