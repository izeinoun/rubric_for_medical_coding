"""Deterministic parts of the method: parsing, quote verification, gates, encoding, scoring, fitting, metrics.
Implements Appendix A of the paper and the pre-registration."""

import json
import math
import re
import unicodedata

import numpy as np

ANSWERS = ("yes", "no", "not_documented")

# ------------------------------------------------------------------ parsing

def parse_json(text):
    """Pull the first JSON object out of a model response. Returns (obj or None, error or None)."""
    if text is None:
        return None, "empty"
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.S)
    i, j = t.find("{"), t.rfind("}")
    if i < 0 or j <= i:
        return None, "no_json_object"
    try:
        return json.loads(t[i:j + 1]), None
    except json.JSONDecodeError as e:
        return None, f"json_error: {e}"


def clean_answers(obj, qids):
    """Normalize an extraction object to {qid: {answer, quotes}}; missing or invalid answers become not_documented."""
    raw = (obj or {}).get("answers", {}) if isinstance(obj, dict) else {}
    out, problems = {}, []
    for q in qids:
        a = raw.get(q, {}) if isinstance(raw, dict) else {}
        ans = str(a.get("answer", "")).strip().lower().replace(" ", "_") if isinstance(a, dict) else ""
        if ans not in ANSWERS:
            problems.append(f"{q}:invalid_answer")
            ans = "not_documented"
        quotes = a.get("quotes", []) if isinstance(a, dict) else []
        if isinstance(quotes, str):
            quotes = [quotes]
        quotes = [str(x) for x in quotes if str(x).strip()]
        out[q] = {"answer": ans, "quotes": quotes}
    return out, problems

# ------------------------------------------------------------- verification

_TRANS = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-",
                        " ": " "})


def _normalize_with_map(s):
    """Lowercase, unify quote/dash characters, collapse whitespace. Returns normalized text and an index map
    from normalized positions back to original positions."""
    s = unicodedata.normalize("NFKC", s).translate(_TRANS)
    out, idx, prev_space = [], [], False
    for i, ch in enumerate(s):
        if ch.isspace():
            if prev_space:
                continue
            out.append(" ")
            idx.append(i)
            prev_space = True
        else:
            out.append(ch.lower())
            idx.append(i)
            prev_space = False
    return "".join(out), idx


def normalize(s):
    return _normalize_with_map(s)[0].strip()


def locate(quote, text):
    """Exact match after normalization. Returns (start, end) in the original text, or None."""
    nq = normalize(quote)
    if len(nq) < 3:
        return None
    nt, idx = _normalize_with_map(text)
    k = nt.find(nq)
    if k < 0:
        return None
    return idx[k], idx[k + len(nq) - 1] + 1


def verify(answers, text, gates):
    """Apply the pre-registered verification rule. Returns verified answers, per-answer records, and the
    needs_review flag (a gate answer or a 'no' answer failed verification)."""
    verified, records, needs_review = {}, {}, False
    for q, a in answers.items():
        ans, quotes = a["answer"], a["quotes"]
        if ans == "not_documented":
            verified[q] = ans
            records[q] = {"answer": ans, "status": "not_required", "spans": []}
            continue
        spans = [locate(x, text) for x in quotes]
        ok = bool(quotes) and all(s is not None for s in spans)
        if ok:
            verified[q] = ans
            records[q] = {"answer": ans, "status": "verified", "spans": spans}
        else:
            verified[q] = "not_documented"
            records[q] = {"answer": ans, "status": "failed" if quotes else "no_quote", "spans": spans}
            if q in gates or ans == "no":
                needs_review = True
    return verified, records, needs_review

# ------------------------------------------------------------------ scoring

def gates_pass(answers, gates):
    return all(answers[g] == "yes" for g in gates)


def feature_names(weighted, two_way=False):
    return [f"{q}_{v}" for q in weighted for v in (("yes",) if two_way else ("yes", "no"))]


def encode(answers, weighted, two_way=False):
    """Reference coding: not_documented is the baseline. two_way merges not_documented into no (ablation M8),
    so only a 'yes' indicator remains per question."""
    if two_way:
        return [int(answers[q] == "yes") for q in weighted]
    return [int(answers[q] == v) for q in weighted for v in ("yes", "no")]


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def score(answers, weights, gates, weighted, two_way=False):
    if not gates_pass(answers, gates):
        return 0.0, None
    names = feature_names(weighted, two_way)
    x = encode(answers, weighted, two_way)
    z = weights["intercept"] + sum(weights.get(n, 0.0) * xi for n, xi in zip(names, x))
    return sigmoid(z), z

# ------------------------------------------------------------------ fitting

def fit_weights(X, y, seed=0, grid=None):
    """Appendix A.3: L2 log-loss, unpenalized intercept, repeated stratified 5-fold CV over C, lowest mean
    log-loss; extend the grid to 1e6 if the choice is at the upper edge."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold

    X, y = np.asarray(X), np.asarray(y)
    if len(set(y.tolist())) < 2:
        raise ValueError("training data has only one class")
    min_class = int(min((y == 0).sum(), (y == 1).sum()))
    n_splits = max(2, min(5, min_class))
    grid = np.logspace(-3, 3, 13) if grid is None else grid

    def run(g):
        s = GridSearchCV(LogisticRegression(solver="lbfgs", max_iter=10_000), {"C": g}, scoring="neg_log_loss",
                         cv=RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=10, random_state=seed), refit=True)
        s.fit(X, y)
        return s

    s = run(grid)
    at_edge = bool(np.isclose(s.best_params_["C"], grid.max()))
    extended = False
    if at_edge:
        grid = np.logspace(-3, 6, 19)
        s = run(grid)
        extended = True
        at_edge = bool(np.isclose(s.best_params_["C"], grid.max()))
    return s.best_estimator_, {"C": float(s.best_params_["C"]), "grid_extended": extended,
                               "still_at_edge": at_edge, "n_splits": n_splits}


def model_to_table(model, names):
    return {"intercept": float(model.intercept_[0]), **{n: float(w) for n, w in zip(names, model.coef_[0])}}


def out_of_fold(X, y, C, seed=0):
    """Out-of-fold probabilities on the training split, for dev-time reporting only (C chosen on all of dev,
    so these are slightly optimistic)."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold, cross_val_predict
    X, y = np.asarray(X), np.asarray(y)
    k = max(2, min(5, int(min((y == 0).sum(), (y == 1).sum()))))
    return cross_val_predict(LogisticRegression(C=C, solver="lbfgs", max_iter=10_000), X, y,
                             cv=StratifiedKFold(k, shuffle=True, random_state=seed), method="predict_proba")[:, 1]


def fit_platt(conf, y):
    """M2: logistic map from verbalized confidence (0-1) to probability."""
    from sklearn.linear_model import LogisticRegression
    m = LogisticRegression(C=1e6, solver="lbfgs", max_iter=10_000)
    m.fit(np.asarray(conf).reshape(-1, 1), np.asarray(y))
    return {"a": float(m.coef_[0][0]), "b": float(m.intercept_[0])}


def apply_platt(params, conf):
    return [sigmoid(params["a"] * c + params["b"]) for c in conf]

# ------------------------------------------------------------------ metrics

def ece(p, y, bins=10):
    p, y = np.asarray(p, float), np.asarray(y, float)
    edges = np.linspace(0, 1, bins + 1)
    total = 0.0
    for i in range(bins):
        m = (p >= edges[i]) & ((p < edges[i + 1]) if i < bins - 1 else (p <= edges[i + 1]))
        if m.any():
            total += m.mean() * abs(p[m].mean() - y[m].mean())
    return float(total)


def brier(p, y):
    p, y = np.asarray(p, float), np.asarray(y, float)
    return float(np.mean((p - y) ** 2))


def auroc(p, y):
    from sklearn.metrics import roc_auc_score
    y = np.asarray(y)
    if len(set(y.tolist())) < 2:
        return float("nan")
    return float(roc_auc_score(y, p))


def coverage_at_precision(p, y, target=0.95, blocked=None):
    """Largest share of charts that can be auto-accepted (score >= threshold, not blocked) while keeping
    precision >= target."""
    p, y = np.asarray(p, float), np.asarray(y, int)
    blocked = np.zeros(len(p), bool) if blocked is None else np.asarray(blocked, bool)
    best = 0.0
    for t in sorted(set(p.tolist()), reverse=True):
        acc = (p >= t) & ~blocked
        if acc.sum() == 0:
            continue
        if y[acc].mean() >= target:
            best = max(best, acc.mean())
    return float(best)


def bootstrap_ci(fn, p, y, n=2000, seed=0, **kw):
    rng = np.random.default_rng(seed)
    p, y = np.asarray(p), np.asarray(y)
    vals = []
    for _ in range(n):
        i = rng.integers(0, len(p), len(p))
        v = fn(p[i], y[i], **{k: (np.asarray(val)[i] if isinstance(val, (list, np.ndarray)) else val)
                              for k, val in kw.items()})
        if not (isinstance(v, float) and math.isnan(v)):
            vals.append(v)
    if not vals:
        return float("nan"), float("nan")
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def reliability_points(p, y, bins=10):
    p, y = np.asarray(p, float), np.asarray(y, float)
    edges = np.linspace(0, 1, bins + 1)
    pts = []
    for i in range(bins):
        m = (p >= edges[i]) & ((p < edges[i + 1]) if i < bins - 1 else (p <= edges[i + 1]))
        if m.any():
            pts.append((float(p[m].mean()), float(y[m].mean()), int(m.sum())))
    return pts


# ------------------------------------------------- extraction and decision metrics

def class_metrics(pred, true, classes=ANSWERS):
    """Per-class precision, recall and F1, macro-F1 over classes present in the intended answers, plain agreement,
    and the confusion matrix (rows = intended, columns = predicted)."""
    per, f1s = {}, []
    for c in classes:
        tp = sum(p == c and t == c for p, t in zip(pred, true))
        fp = sum(p == c and t != c for p, t in zip(pred, true))
        fn = sum(p != c and t == c for p, t in zip(pred, true))
        support = tp + fn
        prec = tp / (tp + fp) if tp + fp else float("nan")
        rec = tp / support if support else float("nan")
        f1 = (2 * prec * rec / (prec + rec)) if support and tp else (0.0 if support else float("nan"))
        per[c] = {"precision": prec, "recall": rec, "f1": f1, "support": support}
        if support:
            f1s.append(f1)
    confusion = {t: {p: sum(a == p and b == t for a, b in zip(pred, true)) for p in classes} for t in classes}
    return {"per_class": per, "macro_f1": float(np.mean(f1s)) if f1s else float("nan"),
            "agreement": float(np.mean([p == t for p, t in zip(pred, true)])) if pred else float("nan"),
            "confusion": confusion, "n": len(pred)}


def threshold_for_precision(p, y, target=0.95, blocked=None):
    """Lowest score threshold whose auto-accepted set (not blocked) has precision >= target; None if none does."""
    p, y = np.asarray(p, float), np.asarray(y, int)
    blocked = np.zeros(len(p), bool) if blocked is None else np.asarray(blocked, bool)
    best = None
    for t in sorted(set(p.tolist()), reverse=True):
        acc = (p >= t) & ~blocked
        if acc.sum() and y[acc].mean() >= target:
            best = t
    return best


def decision_at(p, y, t, blocked=None, beta=0.5):
    """Precision, recall and F-beta when charts with score >= t (and not blocked) are accepted as supported."""
    p, y = np.asarray(p, float), np.asarray(y, int)
    blocked = np.zeros(len(p), bool) if blocked is None else np.asarray(blocked, bool)
    if t is None:
        return {"threshold": None, "precision": float("nan"), "recall": 0.0, "f_beta": float("nan"), "accepted": 0.0}
    acc = (p >= t) & ~blocked
    tp = int((acc & (y == 1)).sum())
    prec = tp / acc.sum() if acc.sum() else float("nan")
    rec = tp / (y == 1).sum() if (y == 1).sum() else float("nan")
    b2 = beta * beta
    fb = ((1 + b2) * prec * rec / (b2 * prec + rec)) if (acc.sum() and tp) else 0.0
    return {"threshold": float(t), "precision": float(prec), "recall": float(rec), "f_beta": float(fb),
            "accepted": float(acc.mean())}
