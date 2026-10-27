"""
Independent consistency checks for the follow-up charts (generator v3).

Reads only charts.jsonl. For every chart it re-reads the note text and checks that the text is consistent
with the label, the intended answers and the scenario: diabetes type wording, CKD stage wording, cause
wording, signature and credentials, provider type, encounter type, which eGFR results the note shows, and
Q2 recomputed from the dated eGFR results in the text. It does not call any model.

Run:  python followup/check_charts_v3.py [followup/data/charts.jsonl]
Exit code 1 if any check fails.
"""

import collections
import datetime as dt
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def clean(text):
    """Undo the format noise well enough for keyword checks (not used for quote verification)."""
    t = re.sub(r"\n--- Page \d of \d ---[^\n]*\n", " ", text)
    t = t.replace("-\n", "").replace("’", "'").replace("–", "-").replace(" ", " ")
    t = re.sub(r"(?<=[A-Za-z])1|1(?=[a-z])", "l", t)       # l -> 1 swaps
    t = re.sub(r"(?<=[A-Z])0|0(?=[A-Z])", "O", t)           # O -> 0 swaps
    t = re.sub(r"(?<=[A-Z])l(?=[A-Z])|\bl(?=[A-Z]{2})", "I", t)  # I -> l swaps in capitals
    return t


def section(t, title_regex):
    m = re.search(title_regex, t)
    if not m:
        return ""
    nxt = re.search(r"\n\n[A-Z][A-Z /\-]{6,}\n", t[m.end():])
    return t[m.start(): m.end() + (nxt.start() if nxt else len(t))]


def egfr_results(t):
    """Dated eGFR results in the text: table lines and 'eGFR was X on DATE and Y on DATE' sentences."""
    out = []
    for m in re.finditer(r"(\d{4}-\d{2}-\d{2})\s+eGFR\s+(>?\d+)", t):
        v = m.group(2)
        out.append((dt.date.fromisoformat(m.group(1)), 61 if v.startswith(">") else int(v)))
    m = re.search(r"eGFR was (\d+) on (\d{4}-\d{2}-\d{2}) and (\d+) on (\d{4}-\d{2}-\d{2})", t)
    if m:
        out += [(dt.date.fromisoformat(m.group(2)), int(m.group(1))), (dt.date.fromisoformat(m.group(4)), int(m.group(3)))]
    return sorted(set(out))


def q2_from(results):
    low = [(d, v) for d, v in results if v < 60]
    if len(low) >= 2 and (low[-1][0] - low[0][0]).days >= 90:
        return "yes"
    if results and results[-1][1] >= 60:
        return "no"
    return "not_documented"


LINK_WORDS = r"due to (type 2 |type 1 )?diabetes|secondary to (type 2 |type 1 )?diabetes|diabetic kidney|diabetic chronic|" \
             r"diabetic nephropathy|due to longstanding diabetes|attributed it to longstanding diabetes|attributed to (his|her) diabetes|diabetic in origin|" \
             r"attributed to both|most likely due to"
OTHER_WORDS = r"nephrosclerosis|polycystic|adpkd|obstructive|post-obstructive|iga nephropathy|ckd [^\n]{0,20}, hypertensive|disease [^\n]{0,20}, hypertensive|long-standing hypertension"
STAGE_WORDS = r"stage (1|2|3a|3b|4|5)\b|\bckd (1|2|3a|3b|4|5)\b"
CRED = r"(, MD|, DO|, FNP-C|, PA-C|, RN|, RD)\b"


def check(c):
    errs = []
    t = clean(c["text"])
    low = t.lower()
    f, a, s = c["facts"], c["intended_answers"], c["scenario"]
    ap = section(t, r"\n(ASSESSMENT AND PLAN|ASSESSMENT/PLAN|IMPRESSION AND PLAN|E-CONSULT ASSESSMENT AND RECOMMENDATIONS)\s")
    hpi = section(t, r"\nHISTORY OF PRESENT ILLNESS\s")
    prior = section(t, r"\n(PRIOR VISIT SUMMARY|INTERVAL NOTE - PREVIOUS VISIT|FROM LAST OFFICE VISIT)[^\n]*\n")
    ap_today = ap.lower()

    # diabetes type wording
    t2 = re.search(r"type 2|t2dm|dm2\b", low)
    t1 = re.search(r"type 1", low)
    if f["diabetes"] in {"2", "2_insulin"}:
        if not t2 or t1:
            errs.append("type 2 chart must say type 2 and never type 1")
    elif f["diabetes"] == "unspec":
        if t2 or t1:
            errs.append("untyped-diabetes chart mentions a type")
    elif f["diabetes"] == "1":
        if not t1 or t2:
            errs.append("type 1 chart must say type 1 and never type 2")
    elif f["diabetes"] == "1_hpi_only":
        if t2 or "type 1" not in hpi.lower() or "type 1" in ap_today:
            errs.append("type 1 must appear in the HPI only")
    elif f["diabetes"] == "sec":
        if t2 or t1 or not re.search(r"steroid-induced|pancreatectomy", low):
            errs.append("secondary-diabetes chart wording")
    if (a["G1"] == "yes") != (f["diabetes"] in {"2", "2_insulin", "unspec"}):
        errs.append("G1 inconsistent with diabetes type")

    # CKD stage wording
    has_stage = re.search(STAGE_WORDS, low)
    if (a["Q1"] == "yes") != bool(has_stage):
        errs.append(f"Q1={a['Q1']} but stage wording present={bool(has_stage)}")

    # cause wording
    link = re.search(LINK_WORDS, low)
    other = re.search(OTHER_WORDS, low)
    if a["Q3"] == "yes" and not link:
        errs.append("Q3=yes without diabetic-cause wording")
    if a["Q3"] == "no" and (not other or link):
        errs.append("Q3=no needs other-cause wording and no diabetic link")
    if a["Q3"] == "not_documented" and f["ckd"] == "est" and (link or other):
        errs.append("Q3=not_documented but cause wording present")
    if s.startswith("E3") and (re.search(LINK_WORDS, ap_today) or not re.search(LINK_WORDS, prior.lower())):
        errs.append("E3: link must be in the prior-visit section only")

    # signature, provider, encounter
    sig = re.findall(r"Electronically signed: [^\n]*", t)
    if f["signature"] == "full" and not (sig and re.search(CRED, sig[-1])):
        errs.append("signed chart lacks signature with credentials")
    if f["signature"] == "unsigned" and (sig or "NOT SIGNED" not in t):
        errs.append("unsigned chart has a signature")
    if f["signature"] == "nocred" and (not sig or re.search(CRED, sig[-1]) or re.search(CRED, t.split("\n")[3])):
        errs.append("no-credentials chart shows credentials")
    if f["provider_type"] in {"RN", "RD"} and not re.search(r", (RN|RD)\b", t):
        errs.append("RN/RD chart lacks RN/RD credentials")
    if f["provider_type"] not in {"RN", "RD"} and re.search(r", (RN|RD)\b", t):
        errs.append("non-RN chart mentions RN/RD")
    if f["encounter"] == "econsult" and "patient not seen" not in low:
        errs.append("e-consult chart must say patient not seen")
    if f["encounter"] == "f2f" and ("not seen" in low or not re.search(r"face-to-face|in person", low)):
        errs.append("face-to-face chart wording")
    if c["family"] == "F" and c["label"] != 0:
        errs.append("family F must be label 0")

    # eGFR results shown, and Q2 recomputed from the text
    res = egfr_results(t)
    visit = dt.date.fromisoformat(f["visit_date"])
    if f["egfr_variant"] == "creat_only":
        if "egfr" in low:
            errs.append("creatinine-only chart mentions eGFR")
    elif not res:
        errs.append("no dated eGFR results found in text")
    if q2_from(res) != a["Q2"]:
        errs.append(f"Q2 recomputed from text {q2_from(res)} != intended {a['Q2']}")
    if f["ap_mode"] in {"stale_copy", "per_last_visit"} and any((visit - d).days <= 30 for d, _ in res):
        errs.append("stale chart shows a recent eGFR")
    if f["ap_mode"] in {"copy_current", "copy_plus_new"} and f["visit_date"] not in ap and "today" not in ap_today:
        errs.append("current-copy chart: plan does not reference today")
    var = f["egfr_variant"]
    if var in {"gap89", "gap90", "gap91"} and (len(res) != 2 or (res[1][0] - res[0][0]).days != int(var[3:])):
        errs.append(f"{var}: day gap in text is wrong")
    if var == "eq60" and (not res or res[-1][1] != 60):
        errs.append("eq60: latest eGFR is not 60")
    if var == "gt60" and ">60" not in t:
        errs.append("gt60: '>60' missing")
    if var == "nodate" and "date not recorded" not in t:
        errs.append("nodate: undated result missing")

    # Q4 wording for the copy-forward and borderline families
    if f["ap_mode"] == "stale_copy" and not re.search(r"continue regimen as previously outlined|last egfr", ap_today):
        errs.append("B2 plan wording")
    if f["ap_mode"] == "per_last_visit" and "per last visit" not in ap_today:
        errs.append("B4 plan wording")
    if f["ap_mode"] == "see_nephro" and "nephrology" not in ap_today:
        errs.append("G2 plan wording")
    if f["ap_mode"] == "list_entry" and not re.search(r"reviewed: [^\n]*ckd (3a|3b|4)", ap_today):
        errs.append("G4 list wording")

    # evidence strings are exact substrings
    for q, spans in c["evidence"].items():
        for sp in spans:
            if sp not in c["text"]:
                errs.append(f"evidence for {q} not in text")
    return errs


def main(path):
    charts = [json.loads(l) for l in open(path)]
    bad = 0
    for c in charts:
        errs = check(c)
        if errs:
            bad += 1
            print(c["chart_id"], c["scenario"], "; ".join(errs))
    fam = collections.Counter((c["family"], c["label"]) for c in charts)
    main_pos = sum(c["label"] for c in charts if c["family"] != "F")
    n_main = sum(c["family"] != "F" for c in charts)
    lens = [len(c["text"]) for c in charts]
    stress = sum("format_stress" in c["flags"] for c in charts)
    print(f"\n{len(charts)} charts; {bad} with problems")
    print("family/label counts:", dict(sorted(fam.items())))
    print(f"main set: {n_main} charts, {main_pos} positive ({main_pos / n_main:.0%}); stress test: {len(charts) - n_main}")
    print(f"note length (characters): median {statistics.median(lens):.0f}, min {min(lens)}, max {max(lens)}")
    print(f"format stress: {stress} charts ({stress / len(charts):.0%})")
    print("splits:", dict(collections.Counter(c["split"] for c in charts)))
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "data", "charts.jsonl")) else 0)
