"""
Exploratory, post-test: one simple chart for a general audience. For each study-3 model, of the test charts given 90% or
more, the share actually supported: the model's own stated confidence (A, raw) against EWC (B). Reads frozen results only.

Run:  python study3/analysis/linkedin_chart.py   (writes paper/figures/linkedin_chart.png)
"""
import contextlib, csv, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S3 = os.path.dirname(HERE); ROOT = os.path.dirname(S3)
sys.path.insert(0, HERE)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
with contextlib.redirect_stdout(io.StringIO()):
    from calibration_table import MODELS  # noqa: E402

ORANGE, BLUE, INK, MUTED, GRID, BG = "#eb6834", "#2a78d6", "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"


def high(rows, m):
    idx = [r for r in rows if float(r[m]) >= 0.9]
    return (sum(int(r["label"]) for r in idx) / len(idx), sum(float(r[m]) for r in idx) / len(idx)) if idx else (None, None)


names, own, ours, said = [], [], [], []
for key, name in MODELS:
    rows = list(csv.DictReader(open(os.path.join(S3, "runs", key, "test", "predictions.csv"))))
    a, s = high(rows, "M1"); b, _ = high(rows, "M5")
    names.append(name)
    own.append(a * 100); ours.append(b * 100); said.append(s * 100)

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
fig, ax = plt.subplots(figsize=(7.5, 7.5), facecolor=BG)
ax.set_facecolor(BG)
y = list(range(len(names)))[::-1]
h = 0.36
ax.barh([v + h / 2 + 0.02 for v in y], own, height=h, color=ORANGE, label="The model's own confidence")
ax.barh([v - h / 2 - 0.02 for v in y], ours, height=h, color=BLUE, label="My method")
for v, a, b in zip(y, own, ours):
    ax.text(a + 1, v + h / 2 + 0.02, f"{a:.0f}%", va="center", fontsize=13, color=INK)
    ax.text(b + 1, v - h / 2 - 0.02, f"{b:.0f}%", va="center", fontsize=13, color=INK, fontweight="bold")
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=13, color=INK)
ax.set_xlim(0, 112); ax.set_xticks([0, 25, 50, 75, 100]); ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"], color=MUTED)
ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(MUTED)
ax.tick_params(axis="y", length=0)
fig.text(0.04, 0.955, "When the AI said it was 90%+ sure,\nhow often was it actually right?", fontsize=19, fontweight="bold",
         color=INK, va="top")
fig.text(0.04, 0.845, f"Models' own claims averaged {min(said):.0f}–{max(said):.0f}% confident. "
         "200 held-out medical coding cases.", fontsize=11.5, color=MUTED, va="top")
ax.legend(loc="upper center", bbox_to_anchor=(0.42, -0.06), ncol=2, frameon=False, fontsize=12.5)
fig.subplots_adjust(left=0.27, right=0.97, top=0.79, bottom=0.14)
out = os.path.join(ROOT, "paper", "figures", "linkedin_chart.png")
fig.savefig(out, dpi=200, facecolor=BG)
print(out, [round(x) for x in own], [round(x) for x in ours])
