"""
Exploratory, post-test: reliability diagram for the paper. One panel per study-3 model; for each method (A stated,
B, C) the test charts are grouped into five confidence bins and the share actually supported is plotted against the
average confidence given. Points on the diagonal mean the confidence matches the accuracy. Bins with fewer than 5
charts are not drawn. Reads frozen results only (no model calls).

Run:  python study3/analysis/reliability_figure.py   (writes paper/figures/reliability.pdf and .png)
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S3 = os.path.dirname(HERE); ROOT = os.path.dirname(S3)
sys.path.insert(0, HERE)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from calibration_table import MODELS, m9  # noqa: E402  (importing reruns the table; output silenced)

METHODS = [("M1", "A: model's stated confidence", "#eb6834", "s"),
           ("M9", "C: model given the questions", "#1baf7a", "^"),
           ("M5", "B: evidence-weighted (ours)", "#2a78d6", "o")]
EDGES = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0001]
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"

plt.rcParams.update({"font.size": 8, "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": MUTED,
                     "ytick.color": MUTED, "font.family": "serif",
                     "font.serif": ["cmr10"], "mathtext.fontset": "cm", "axes.formatter.use_mathtext": True,
                     "axes.unicode_minus": False, "pdf.fonttype": 42})
fig, axes = plt.subplots(2, 3, figsize=(6.4, 4.5), sharex=True, sharey=True)
for ax, (key, name) in zip(axes.flat, MODELS):
    rows = list(csv.DictReader(open(os.path.join(S3, "runs", key, "test", "predictions.csv"))))
    ys = [int(r["label"]) for r in rows]
    c9 = m9(key)
    ax.plot([0, 1], [0, 1], color=MUTED, lw=0.8, ls="--", zorder=1)
    for m, label, col, mk in METHODS:
        ps = [c9.get(r["chart_id"], 0.0) if m == "M9" else float(r[m]) for r in rows]
        xs, ys_ = [], []
        for lo, hi in zip(EDGES, EDGES[1:]):
            idx = [i for i, p in enumerate(ps) if lo <= p < hi]
            if len(idx) >= 5:
                xs.append(sum(ps[i] for i in idx) / len(idx)); ys_.append(sum(ys[i] for i in idx) / len(idx))
        ax.plot(xs, ys_, color=col, lw=1.5, marker=mk, ms=5, mec="white", mew=0.8, label=label, zorder=3)
    ax.set_title(name, fontsize=8.5, color=INK)
    ax.set_xlim(-0.03, 1.03); ax.set_ylim(-0.03, 1.03)
    ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1])
    ax.grid(color=GRID, lw=0.6); ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axes[0, 2].tick_params(labelbottom=True)
leg = axes.flat[5]
leg.axis("off")
h, l = axes.flat[0].get_legend_handles_labels()
leg.legend(h[::-1], l[::-1], loc="center", frameon=False, fontsize=8, title="Diagonal = confidence\nmatches accuracy",
           title_fontsize=8)
fig.supxlabel("Confidence given (average in bin)", fontsize=8.5)
fig.supylabel("Share of charts actually supported", fontsize=8.5)
fig.tight_layout()
out = os.path.join(ROOT, "paper", "figures")
os.makedirs(out, exist_ok=True)
fig.savefig(os.path.join(out, "reliability.pdf"))
fig.savefig(os.path.join(out, "reliability.png"), dpi=200)
print("written", out)
