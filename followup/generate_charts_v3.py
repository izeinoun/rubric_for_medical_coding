"""
Synthetic outpatient chart generator for the EWC follow-up transfer test. Version 3.

Writes 300 charts, all in the test split, for the candidate code E11.22 (type 2 diabetes mellitus with
diabetic chronic kidney disease). See followup/SPEC.md for the design.

Each chart is built from a fact sheet. From the facts the generator derives, independently:
  - the intended answer to every rubric question (G1, G2, Q1-Q4), following the frozen rubric (version 2);
  - the label, from coding rules applied to the facts: the pilot rule plus R1-R3 (SPEC.md section 3).
For every family except F the two agree with the pilot's rubric-based label rule; for family F the rubric
answers look positive but the label is 0 (outside the rubric). Both facts are asserted for every chart.

Answer semantics (as in the pilot)
  yes            the note affirmatively documents the fact
  no             the note explicitly documents the opposite, or explicitly says the fact is not established
  not_documented the note is silent

About half the charts get format stress (OCR-style swaps, words hyphenated across lines, page headers,
irregular lab tables, non-ASCII punctuation). Evidence strings are recorded after the noise, so they are
exact substrings of the final text.

The pilot generator (generate_charts.py) and pilot data are not modified; its phrase banks are imported.
All patients, providers and dates are fictional. Run:  python followup/generate_charts_v3.py [out_dir]
"""

import csv
import datetime as dt
import hashlib
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import generate_charts as v2  # noqa: E402  (pilot phrase banks and helpers; not modified)

SEED = 20261027
VERSION = "3"
YES, NO, ND = v2.YES, v2.NO, v2.ND
QUESTIONS = v2.QUESTIONS

# scenario id -> (family, description, count, label)
SCENARIOS = {
    # A: pilot scenarios, regenerated with the new template (F1b replaced by family B)
    "A_P1_stage_and_link":     ("A", "CKD with stage, explicitly due to type 2 diabetes in the assessment, addressed in plan", 5, 1),
    "A_P2_with_convention":    ("A", "CKD with stage, no cause stated, addressed in plan", 5, 1),
    "A_P3_link_no_stage":      ("A", "Diabetic CKD addressed in plan, stage not documented", 5, 1),
    "A_P4_link_in_hpi":        ("A", "CKD addressed in plan; diabetic cause stated only in the HPI", 5, 1),
    "A_F1a_copy_fwd_current":  ("A", "Plan carried forward, CKD line uses today's results and a current action", 5, 1),
    "A_N1a_problem_list_only": ("A", "CKD on the problem list only", 5, 0),
    "A_N1b_laundry_list":      ("A", "CKD named in a list of problems in the plan, no status or action", 5, 0),
    "A_N2_other_cause":        ("A", "CKD attributed to a non-diabetic cause", 5, 0),
    "A_N3_labs_only":          ("A", "Low eGFR results, no CKD diagnosis", 5, 0),
    "A_N4_type1":              ("A", "Type 1 diabetes with CKD", 5, 0),
    "A_N5_uncertain_dx":       ("A", "CKD only possible or not yet established", 5, 0),
    "A_N6_aki_not_ckd":        ("A", "Resolved acute kidney injury; CKD explicitly absent", 5, 0),
    # B: copy-forward
    "B1_copy_current":         ("B", "Plan copied forward; CKD line cites today's eGFR with today's date and a current action", 8, 1),
    "B2_copy_stale":           ("B", "Plan copied from a dated prior visit; old eGFR and action only; no current CKD content", 11, 0),
    "B3_copy_plus_new":        ("B", "Copied CKD line followed by a new line from today", 8, 1),
    "B4_per_last_visit":       ("B", "Copied CKD line marked per last visit; today's labs not mentioned", 10, 0),
    "B5_interval_labs":        ("B", "Interval history gives today's renal labs; copied plan line refers to them", 8, 1),
    # C: harder gates
    "C1_dm_untyped":           ("C", "Diabetes with no type documented (ICD-10-CM default type 2); CKD addressed", 5, 1),
    "C2_t2_on_insulin":        ("C", "Type 2 diabetes on insulin; CKD addressed", 5, 1),
    "C3_t1_in_hpi_only":       ("C", "Type 1 diabetes stated only in the HPI; assessment says 'diabetes'", 7, 0),
    "C4_secondary_dm":         ("C", "Steroid-induced or post-pancreatectomy diabetes with CKD (rule R3)", 7, 0),
    "C5_history_of_ckd":       ("C", "'History of CKD' in the HPI; plan gives a current CKD status and action", 5, 1),
    "C6_ckd_ruled_out":        ("C", "CKD removed from the problem list; repeat testing shows no CKD", 7, 0),
    # D: Q2 lab and date edge cases (label from the base scenario)
    "D_eq60":                  ("D", "Latest eGFR exactly 60", 3, 0),
    "D_gt60":                  ("D", "Latest eGFR reported as '>60'", 3, 0),
    "D_gap89_pos":             ("D", "Two low eGFRs 89 days apart; CKD addressed", 1, 1),
    "D_gap89_neg":             ("D", "Two low eGFRs 89 days apart; CKD on problem list only", 3, 0),
    "D_gap90_pos":             ("D", "Two low eGFRs exactly 90 days apart; CKD addressed", 2, 1),
    "D_gap90_neg":             ("D", "Two low eGFRs exactly 90 days apart; CKD on problem list only", 1, 0),
    "D_gap91_pos":             ("D", "Two low eGFRs 91 days apart; CKD addressed", 1, 1),
    "D_gap91_neg":             ("D", "Two low eGFRs 91 days apart; CKD on problem list only", 2, 0),
    "D_nodate_pos":            ("D", "One dated low eGFR plus one undated outside result; CKD addressed", 1, 1),
    "D_nodate_neg":            ("D", "One dated low eGFR plus one undated outside result; CKD on problem list only", 2, 0),
    "D_creat_only_pos":        ("D", "Creatinine reported, no eGFR anywhere; CKD addressed", 1, 1),
    "D_creat_only_neg":        ("D", "Creatinine reported, no eGFR anywhere; CKD on problem list only", 2, 0),
    "D_sentence_pos":          ("D", "eGFR results written in a sentence, not a lab table; CKD addressed", 2, 1),
    "D_sentence_neg":          ("D", "eGFR results written in a sentence, not a lab table; CKD on problem list only", 2, 0),
    # E: cause attribution
    "E1_dm_and_htn":           ("E", "CKD due to diabetes and hypertension", 8, 1),
    "E2_likely_diabetic":      ("E", "Likely diabetic nephropathy, with CKD stage", 8, 1),
    "E3_link_in_prior_visit":  ("E", "Diabetic cause stated only in a dated prior-visit section", 8, 1),
    # G: borderline
    "G1_reviewed_stable":      ("G", "CKD addressed only by 'renal function reviewed, stable'", 11, 1),
    "G2_see_nephrology":       ("G", "CKD in the plan with only 'see nephrology note'", 15, 0),
    "G3_med_change":           ("G", "CKD addressed by a medication change for kidney function, CKD not named in that line", 11, 1),
    "G4_list_entry":           ("G", "CKD as one entry in a reviewed list of problems, no status or action", 16, 0),
    "G5_minimal":              ("G", "'CKD 3a, stable on losartan' as its own plan line", 11, 1),
    # F: stress test, outside the rubric (rubric answers look positive; label 0 under R1/R2)
    "F1_non_acceptable_provider": ("F", "Visit documented by an RN or a dietitian only (R1)", 15, 0),
    "F2_unsigned":             ("F", "Note unsigned, or signed without credentials (R2)", 15, 0),
    "F3_not_face_to_face":     ("F", "Chart-review e-consult; patient not seen (R1)", 15, 0),
}
N_TOTAL, N_MAIN, N_STRESS = 300, 255, 45

Q4_YES_MODES = {"full", "copy_current", "copy_plus_new", "interval_labs", "reviewed_stable", "med_change", "minimal"}
ACCEPTABLE_PROVIDERS = {"MD", "DO", "NP", "PA"}

STAGE_TEXT = dict(v2.STAGE_TEXT)
EGFR_RANGE = dict(v2.EGFR_RANGE)

# ------------------------------------------------------------- new phrase banks

PROVIDERS = {
    "MD": ("Synthetic Provider, MD", "Internal Medicine"),
    "DO": ("Synthetic Physician, DO", "Family Medicine"),
    "NP": ("Synthetic Practitioner, FNP-C", "Primary Care"),
    "PA": ("Synthetic Associate, PA-C", "Internal Medicine"),
    "RN": ("Synthetic Nurse, RN", "Diabetes Education"),
    "RD": ("Synthetic Dietitian, RD", "Medical Nutrition Therapy"),
}
VISIT_TYPE = {
    "MD": "Office visit, established patient, face-to-face",
    "DO": "Office visit, established patient, face-to-face",
    "NP": "Office visit, established patient, face-to-face",
    "PA": "Office visit, established patient, face-to-face",
    "RN": "Nurse visit, diabetes education, in person",
    "RD": "Medical nutrition therapy visit, in person",
}

ROS = [
    "Constitutional: denies fever, chills or unintended weight loss.",
    "Eyes: no blurred vision; last dilated eye exam {eye_yr}.",
    "Cardiovascular: no chest pain, palpitations or orthopnea.",
    "Respiratory: no cough or dyspnea on exertion.",
    "Gastrointestinal: no nausea, vomiting, diarrhea or constipation.",
    "Genitourinary: no dysuria, hematuria or change in urine output.",
    "Musculoskeletal: chronic knee stiffness, otherwise negative.",
    "Neurological: no numbness or tingling in the feet; no headaches.",
    "Psychiatric: mood stable; sleeping 6 to 7 hours a night.",
    "Endocrine: no polyuria, polydipsia or heat or cold intolerance.",
    "Skin: no rashes or non-healing wounds.",
]
SURGICAL = ["Cholecystectomy (2011)", "Right knee arthroscopy (2015)", "Appendectomy (1988)",
            "Cataract extraction, left eye (2022)", "Colonoscopy with polypectomy (2021)", "Tonsillectomy (childhood)"]
FAMILY = ["Mother: hypertension.", "Father: coronary artery disease, died age {fa}.",
          "Sister: hypothyroidism.", "Brother: hyperlipidemia.", "No family history of kidney disease reported."]
SMOKING = ["Former smoker, quit {quit}; {py} pack-years.", "Never smoker."]
SOCIAL = ["Alcohol: {alc}.", "Lives with {lives}. Retired {job}.", "Works part time as a {job2}.",
          "Walks {walk} times per week, about 20 minutes."]
HEALTH_MAINT = ["Influenza vaccine given this season.", "Pneumococcal vaccination up to date.",
                "Colorectal cancer screening up to date.", "Diabetic foot exam completed today.",
                "Retinal exam due; referral placed.", "Shingles vaccine series completed.",
                "Dental visit within the past year."]
EDUCATION = ["Discussed hypoglycemia recognition and treatment.", "Reviewed sick-day rules for medications.",
             "Encouraged 150 minutes of moderate activity weekly.", "Reviewed carbohydrate counting handout.",
             "Patient verbalized understanding of the plan."]
MED_REC = ["Medication reconciliation completed; no changes other than those noted in the plan.",
           "Medications reviewed with patient and pharmacy list; list above is current.",
           "Med rec done with patient's pill bottles."]
ALLERGIES = ["NKDA.", "Penicillin (rash).", "Sulfa drugs (hives).", "No known drug allergies.", "Codeine (nausea)."]

DX_LINK_STAGE = ["Chronic kidney disease {stage} due to {dmx}", "CKD {stage} secondary to {dmx}",
                 "Diabetic chronic kidney disease, {stage}", "Diabetic kidney disease, CKD {stage}"]
DX_LINK_NOSTAGE = ["Chronic kidney disease due to {dmx}", "CKD secondary to {dmx}",
                   "Diabetic chronic kidney disease", "Diabetic kidney disease"]
DX_DM_HTN = ["CKD {stage} due to {dmx} and hypertension",
             "Chronic kidney disease {stage}, attributed to both {dmx} and hypertension"]
DX_LIKELY = ["CKD {stage}, likely diabetic nephropathy", "Chronic kidney disease {stage}, most likely due to {dmx}"]

B1_LINES = ["eGFR {egfr} today ({today}), {trend}. Continue {sglt2}; recheck BMP in 3 months.",
            "Today's eGFR {egfr} ({today}), {trend}. Continue {raas} and {sglt2}. Labs again in 3 months."]
B2_LINES = ["eGFR {old_egfr} ({old_date}), stable at that time. Continue regimen as previously outlined.",
            "Last eGFR {old_egfr} on {old_date}. Continue current renal regimen. Labs before next visit."]
B3_NEW = ["Update today: eGFR {egfr} ({today}), {trend}; continue {sglt2}.",
          "Addendum {today}: eGFR {egfr} today, {trend}. No change to {raas}."]
B4_LINES = ["Per last visit, stable; unchanged from {old_my}.", "Unchanged from {old_my}; per last visit."]
B5_INTERVAL = ["Labs drawn {today} were reviewed with the patient today: eGFR {egfr}, UACR {uacr} mg/g.",
               "Reviewed this morning's labs ({today}) with the patient: eGFR {egfr}, potassium {k}."]
B5_LINES = ["See today's labs above; at baseline. Continue {raas}.",
            "Today's results as above, at baseline; continue {raas} and {sglt2}."]
G1_LINES = ["Renal function reviewed, stable.", "Renal function reviewed; stable."]
G2_LINES = ["See nephrology note.", "Per nephrology; see their note."]
G3_LINES = ["Metformin reduced to 500 mg twice daily because eGFR is now {egfr} ({trend}).",
            "Metformin dose lowered to 500 mg daily given eGFR {egfr}; recheck BMP in 6 weeks."]
G4_LINES = ["Chronic conditions reviewed: {items}.", "Other chronic problems reviewed: {items}."]
G5_LINES = ["CKD {stg}, stable on {raas}.", "CKD {stg}, stable on {raas}; no changes."]

PRIOR_HDR = ["PRIOR VISIT SUMMARY ({d})", "INTERVAL NOTE - PREVIOUS VISIT {d}", "FROM LAST OFFICE VISIT ({d})"]

PAGE_HDR = "--- Page {p} of {n} --- {cid} --- printed {d} ---"

# ------------------------------------------------------------------ helpers

fmt_date = v2.fmt_date
rand_date = v2.rand_date


def answer_q2(dated):
    """Q2 from the dated eGFR results shown in the note (undated results cannot show the 90-day span)."""
    return v2.answer_q2(sorted(dated))


def label_from_facts(p):
    """Pilot rule on the facts, plus R1 (face-to-face, acceptable provider), R2 (signature with
    credentials) and R3 (secondary diabetes is not type 2)."""
    pilot = (p["dm"] in {"2", "2_insulin", "unspec"} and p["ckd"] == "est" and p["ap"] in Q4_YES_MODES and p["cause"] != "other")
    r1 = p["encounter"] == "f2f" and p["prov"] in ACCEPTABLE_PROVIDERS
    r2 = p["sign"] == "full"
    return int(pilot and r1 and r2)


def creat_for(egfr):
    """Creatinine (mg/dL) that falls as eGFR rises, so the two lab rows agree."""
    return round(0.95 * 65 / egfr, 2)


# --------------------------------------------------------------- scenario facts

def scenario_params(s, rng):
    fam = SCENARIOS[s][0]
    p = dict(sid=s, family=fam, dm="2", sec_kind=None, ckd="est", staged=True, cause=None, other=None,
             cause_loc=None, ap="full", hx_ckd_hpi=False, egfr_variant=None, encounter="f2f",
             prov=rng.choices(["MD", "DO", "NP", "PA"], weights=[55, 15, 18, 12])[0], sign="full",
             prior_section=rng.random() < 0.25, copy_marker=False, ambiguous=[], flags=[])
    p["stage"] = rng.choices(["3a", "3b", "4"], weights=[55, 35, 10])[0]

    if fam == "A":
        base = s[2:]
        if base.startswith("P1"):
            p.update(cause="diabetes", cause_loc="ap")
        elif base.startswith("P2"):
            pass
        elif base.startswith("P3"):
            p.update(staged=False, cause="diabetes", cause_loc="ap")
        elif base.startswith("P4"):
            p.update(cause="diabetes", cause_loc="hpi")
        elif base.startswith("F1a"):
            p.update(ap="copy_current", copy_marker=True)
            if rng.random() < 0.5:
                p.update(cause="diabetes", cause_loc="ap")
        elif base.startswith("N1a"):
            p.update(ap="none", staged=rng.random() < 0.65)
            if rng.random() < 0.3:
                p.update(cause="diabetes", cause_loc="pl")
        elif base.startswith("N1b"):
            p.update(ap="laundry", staged=rng.random() < 0.7)
            p["ambiguous"].append("Q4")
        elif base.startswith("N2"):
            p.update(cause="other", other=rng.choice(v2.OTHER_CAUSES), cause_loc="ap" if rng.random() < 0.6 else "hpi")
        elif base.startswith("N3"):
            p.update(ckd="labs", ap="none", staged=False)
            p["ambiguous"].append("G2")
        elif base.startswith("N4"):
            p.update(dm="1")
            if rng.random() < 0.5:
                p.update(cause="diabetes", cause_loc="ap")
        elif base.startswith("N5"):
            p.update(ckd="possible", ap="possible", staged=False)
            p["ambiguous"].append("Q4")
        elif base.startswith("N6"):
            p.update(ckd="aki", ap="aki", staged=False)
            p["ambiguous"].append("Q4")
    elif fam == "B":
        p["copy_marker"] = True
        p["ap"] = {"B1": "copy_current", "B2": "stale_copy", "B3": "copy_plus_new", "B4": "per_last_visit",
                   "B5": "interval_labs"}[s[:2]]
        if rng.random() < 0.5:
            p.update(cause="diabetes", cause_loc="ap")
        p["prior_section"] = False
        if s[:2] in {"B2", "B4"}:
            p["flags"].append("label_needs_review")  # contested in the human label review (2026-10-27)
    elif fam == "C":
        k = s[:2]
        if k == "C1":
            p["dm"] = "unspec"
        elif k == "C2":
            p["dm"] = "2_insulin"
        elif k == "C3":
            p["dm"] = "1_hpi_only"
        elif k == "C4":
            p.update(dm="sec", sec_kind=rng.choice(["steroid", "pancreatectomy"]))
        elif k == "C5":
            p["hx_ckd_hpi"] = True
        elif k == "C6":
            p.update(ckd="ruled_out", ap="ruled_out", staged=False)
            p["ambiguous"].append("Q4")
        if k in {"C1", "C2", "C3", "C4"} and rng.random() < 0.5:
            p.update(cause="diabetes", cause_loc="ap")
    elif fam == "D":
        var = s[2:].replace("_pos", "").replace("_neg", "")
        p["egfr_variant"] = var
        p["stage"] = "3a" if var in {"eq60", "gt60"} else rng.choice(["3a", "3b"])
        if s.endswith("_neg") or var in {"eq60", "gt60"}:
            p["ap"] = "none"
        if var == "nodate":
            p["ambiguous"].append("Q2")
        p["prior_section"] = False
    elif fam == "E":
        k = s[:2]
        if k == "E1":
            p.update(cause="dm_htn", cause_loc="ap")
            p["ambiguous"].append("Q3")
        elif k == "E2":
            p.update(cause="likely_dm", cause_loc="ap")
            p["ambiguous"].append("Q3")
        else:
            p.update(cause="diabetes", cause_loc="prior", prior_section=True)
    elif fam == "G":
        k = s[:2]
        p["ap"] = {"G1": "reviewed_stable", "G2": "see_nephro", "G3": "med_change", "G4": "list_entry",
                   "G5": "minimal"}[k]
        if k == "G1":
            p.update(staged=False)
        if k == "G5":
            p["stage"] = rng.choice(["3a", "3b"])
        if k == "G3":
            p["stage"] = rng.choice(["3a", "3b"])
        p["ambiguous"].append("Q4")
        p["flags"].append("borderline")
        if k == "G4":
            p["flags"].append("label_needs_review")  # contested in the human label review (2026-10-27)
    elif fam == "F":
        if rng.random() < 0.5:
            p.update(cause="diabetes", cause_loc="ap")
        k = s[:2]
        if k == "F1":
            p["prov"] = rng.choice(["RN", "RD"])
        elif k == "F2":
            p["sign"] = rng.choice(["unsigned", "nocred"])
        else:
            p["encounter"] = "econsult"
        p["flags"].append("outside_rubric")
    return p


# ----------------------------------------------------------------- the builder

def build_chart(rng, idx, s):
    p = scenario_params(s, rng)
    cid = f"FU-{idx:04d}"
    ev = {q: [] for q in QUESTIONS}

    def add(q, text):
        ev[q].append(text)
        return text

    sex = rng.choice(["M", "F"])
    sexw, pro = ("man", "his") if sex == "M" else ("woman", "her")
    age = rng.randint(48, 84)
    visit = rand_date(rng, dt.date(2026, 1, 12), dt.date(2026, 9, 30))
    today = fmt_date(visit)
    est = p["ckd"] == "est"
    stage = p["stage"]
    st = STAGE_TEXT[stage]
    stg = stage  # short form for "CKD 3a"
    dm_type1 = p["dm"] in {"1", "1_hpi_only"}

    # --- eGFR series: list of (date or None, value, display) -------------------------------
    lo, hi = EGFR_RANGE[stage]
    prior_date = visit - dt.timedelta(days=rng.randint(100, 240))
    recent_date = visit - dt.timedelta(days=rng.randint(0, 10))
    if p["ap"] in {"copy_current", "copy_plus_new", "interval_labs"}:
        recent_date = visit  # the plan refers to today's labs
    var = p["egfr_variant"]
    egfr_rows = []  # (date, value, display)
    undated = None
    egfr_in_table = True
    aki_date = None
    if p["ckd"] == "labs":
        egfr_rows = [(prior_date, rng.randint(46, 58)), (recent_date, rng.randint(45, 58))]
    elif p["ckd"] == "possible":
        egfr_rows = [(prior_date, rng.randint(61, 68)), (recent_date, rng.randint(54, 59))]
    elif p["ckd"] == "aki":
        aki_date = visit - dt.timedelta(days=rng.randint(60, 150))
        egfr_rows = [(aki_date, rng.randint(28, 42)), (recent_date, rng.randint(68, 88))]
    elif p["ckd"] == "ruled_out":
        old = visit - dt.timedelta(days=rng.randint(330, 420))
        egfr_rows = [(old, rng.randint(52, 58)), (prior_date, rng.randint(72, 80)), (recent_date, rng.randint(74, 84))]
    elif p["ap"] in {"stale_copy", "per_last_visit"}:
        d1 = visit - dt.timedelta(days=rng.randint(60, 150))
        d0 = d1 - dt.timedelta(days=rng.randint(100, 200))
        egfr_rows = [(d0, rng.randint(lo, hi)), (d1, rng.randint(lo, hi))]
    elif var == "eq60":
        egfr_rows = [(prior_date, rng.randint(52, 58)), (recent_date, 60)]
    elif var == "gt60":
        egfr_rows = [(prior_date, rng.randint(50, 58)), (recent_date, 61)]
    elif var in {"gap89", "gap90", "gap91"}:
        gap = int(var[3:])
        egfr_rows = [(recent_date - dt.timedelta(days=gap), rng.randint(lo, hi)), (recent_date, rng.randint(lo, hi))]
    elif var == "nodate":
        egfr_rows = [(recent_date, rng.randint(lo, hi))]
        undated = rng.randint(lo, hi)
    elif var == "creat_only":
        egfr_rows = [(prior_date, rng.randint(lo, hi)), (recent_date, rng.randint(lo, hi))]
        egfr_in_table = False
    elif var == "sentence":
        egfr_rows = [(prior_date, rng.randint(lo, hi)), (recent_date, rng.randint(lo, hi))]
        egfr_in_table = False
    elif rng.random() < 0.7:
        egfr_rows = [(prior_date, rng.randint(lo, hi)), (recent_date, rng.randint(lo, hi))]
    else:
        egfr_rows = [(recent_date, rng.randint(lo, hi))]
    egfr_rows.sort()
    if len(egfr_rows) >= 2 and egfr_rows[-1][1] == egfr_rows[-2][1] and var is None and p["ap"] != "reviewed_stable":
        egfr_rows[-1] = (egfr_rows[-1][0], egfr_rows[-1][1] + (1 if egfr_rows[-1][1] < hi else -1))
    if p["ap"] == "reviewed_stable" and len(egfr_rows) >= 2:  # 'stable' must match the trend
        egfr_rows[-1] = (egfr_rows[-1][0], max(lo, min(hi, egfr_rows[-2][1] + rng.randint(-3, 3))))
    latest = egfr_rows[-1][1]
    show = (lambda v: ">60" if (var == "gt60" and v == 61) else str(v))
    trend = v2.egfr_trend(egfr_rows)
    if var == "gt60":
        trend = f"up from {egfr_rows[-2][1]}"
    current_egfr_shown = p["ap"] not in {"stale_copy", "per_last_visit"}  # B2/B4 show no eGFR from today

    # --- distractors, vitals, labs -------------------------------------------------------
    pool = ["htn", "hld", "obesity", "oa", "gerd", "hypothyroid", "allergic"]
    if dm_type1:
        pool.remove("htn")
    distractors = rng.sample(pool, rng.randint(2, 4))
    if (p["other"] == "hypertensive nephrosclerosis" or p["cause"] == "dm_htn") and "htn" not in distractors:
        distractors.append("htn")
    bp = f"{rng.randint(118, 148)}/{rng.randint(68, 92)}"
    height = rng.uniform(1.62, 1.88) if sex == "M" else rng.uniform(1.52, 1.75)
    bmi = round(rng.uniform(30.5, 38.5) if "obesity" in distractors else rng.uniform(23.5, 29.8), 1)
    wt = round(bmi * height * height, 1)
    ldl = rng.randint(58, 132)
    a1c = round(rng.uniform(6.4, 9.6), 1)
    prior_a1c = round(a1c + rng.choice([-1, 1]) * rng.uniform(0.2, 1.4), 1)
    a1c_trend = ("improved from" if prior_a1c > a1c else "up from") + f" {prior_a1c}%"
    sglt2_full = rng.choice(v2.SGLT2)
    sglt2 = sglt2_full.split(" ")[0]
    low_alb = p["ckd"] in {"possible", "aki", "ruled_out"}
    uacr = rng.randint(8, 26) if low_alb else rng.randint(35, 420)
    k_val = round(rng.uniform(3.8, 5.1), 1)

    # --- medications -------------------------------------------------------------------------
    meds = []
    if p["dm"] == "sec" and p["sec_kind"] == "steroid":
        meds += ["prednisone 10 mg daily (polymyalgia rheumatica)", "glipizide 5 mg daily"]
    elif p["dm"] == "sec":
        meds += ["insulin glargine 14 units nightly", "insulin aspart sliding scale with meals",
                 "pancrelipase with meals"]
    elif dm_type1:
        meds.append(rng.choice(["insulin glargine 22 units nightly and insulin lispro with meals; continuous glucose monitor",
                                "insulin pump (lispro) with continuous glucose monitor"]))
    elif p["dm"] == "2_insulin":
        meds += ["insulin glargine 24 units nightly", "metformin 500 mg twice daily (renally dosed)"]
    else:
        if est and stage == "4":
            meds.append("insulin glargine 18 units nightly")
        elif p["ap"] == "med_change":
            meds.append("metformin 1000 mg twice daily (dose being reduced today)")
        elif est and stage == "3b":
            meds.append("metformin 500 mg twice daily (renally dosed)")
        else:
            meds.append("metformin 1000 mg twice daily")
        if rng.random() < 0.3:
            meds.append("semaglutide 0.5 mg weekly")
    if (est and p["other"] != "polycystic kidney disease") or rng.random() < 0.3:
        meds.append(sglt2_full)
    if "htn" in distractors:
        raas = "lisinopril"
    else:
        raas = "losartan"
        if est or dm_type1:
            meds.append("losartan 50 mg daily")
    for d in distractors:
        if v2.DISTRACTORS[d][1]:
            meds.append(v2.DISTRACTORS[d][1])

    # --- diabetes wording --------------------------------------------------------------------
    dmx = {"2": "type 2 diabetes", "2_insulin": "type 2 diabetes", "unspec": "diabetes", "1": "type 1 diabetes",
           "1_hpi_only": "diabetes", "sec": "diabetes"}[p["dm"]]
    if p["dm"] in {"2"}:
        dm_pl = rng.choice(["Type 2 diabetes mellitus", "Diabetes mellitus type 2", "T2DM, on oral agents"])
        dm_ap = rng.choice(["Type 2 diabetes mellitus", "Diabetes mellitus, type 2", "T2DM"])
    elif p["dm"] == "2_insulin":
        dm_pl = rng.choice(["Type 2 diabetes mellitus, insulin-requiring", "Type 2 diabetes on insulin"])
        dm_ap = rng.choice(["Type 2 diabetes mellitus on insulin", "T2DM, insulin-requiring"])
    elif p["dm"] == "unspec":
        dm_pl = rng.choice(["Diabetes mellitus", "DM, on metformin", "Diabetes"])
        dm_ap = rng.choice(["Diabetes mellitus", "Diabetes", "DM"])
    elif p["dm"] == "1":
        dm_pl = rng.choice(["Type 1 diabetes mellitus", "Diabetes mellitus type 1, on insulin", "Type 1 DM"])
        dm_ap = "Type 1 diabetes mellitus"
    elif p["dm"] == "1_hpi_only":
        dm_pl = rng.choice(["Diabetes mellitus, on insulin", "Diabetes, insulin pump"])
        dm_ap = "Diabetes mellitus"
    else:
        dm_pl = {"steroid": "Steroid-induced diabetes mellitus", "pancreatectomy": "Diabetes mellitus due to total pancreatectomy"}[p["sec_kind"]]
        dm_ap = dm_pl

    # --- CKD diagnosis wording ------------------------------------------------------------------
    def dx_text(with_cause):
        if with_cause and p["cause"] == "diabetes":
            return (rng.choice(DX_LINK_STAGE).format(stage=st, dmx=dmx) if p["staged"]
                    else rng.choice(DX_LINK_NOSTAGE).format(dmx=dmx))
        if with_cause and p["cause"] == "dm_htn":
            return rng.choice(DX_DM_HTN).format(stage=st, dmx=dmx)
        if with_cause and p["cause"] == "likely_dm":
            return rng.choice(DX_LIKELY).format(stage=st, dmx=dmx)
        if with_cause and p["cause"] == "other":
            return rng.choice(v2.AP_OTHER_CAUSE[p["other"]]).format(stage=st)
        return rng.choice(v2.DX_STAGE_NOLINK).format(stage=st) if p["staged"] else "Chronic kidney disease"

    cause_in_ap = p["cause_loc"] == "ap"
    dx_ap = dx_text(cause_in_ap) if est else None
    pl_dx = None
    if est:
        if p["cause_loc"] == "pl" or (cause_in_ap and p["cause"] == "other"):
            pl_dx = dx_text(True) if p["cause_loc"] == "pl" else dx_ap
        else:
            pl_dx = dx_text(False)
    if p["ap"] in {"see_nephro", "minimal", "list_entry"} and est:
        dx_ap = f"CKD {stg}" if p["ap"] != "see_nephro" else dx_ap

    # --- CKD plan line ------------------------------------------------------------------------
    fill = dict(egfr=latest, trend=trend, sglt2=sglt2, raas=raas, raas_up=f"{raas} to {'40' if raas == 'lisinopril' else '100'} mg daily",
                uacr=uacr, today=today, k=k_val)
    if var == "creat_only":
        cr_prev, cr_now = creat_for(egfr_rows[0][1]), creat_for(egfr_rows[-1][1])
        plan_full = rng.choice([f"Creatinine {cr_now} mg/dL today (was {cr_prev}). Continue {sglt2}. Recheck BMP in 3 months.",
                                f"Renal function: creatinine {cr_now} mg/dL, previously {cr_prev}. Continue {raas}; avoid NSAIDs."])
    elif var == "gt60":
        plan_full = f"eGFR >60 today. Continue {raas}. Recheck BMP and UACR in 6 months."
    else:
        if dm_type1:
            bank = v2.CKD_PLAN_T1
        elif p["other"] == "polycystic kidney disease":
            bank = v2.CKD_PLAN_PKD
        elif stage == "4":
            bank = v2.CKD_PLAN_STAGE4
        else:
            bank = v2.CKD_PLAN
        plan_full = rng.choice(bank).format(**fill)
        if p["encounter"] == "econsult":
            plan_full = ("Latest eGFR {egfr} ({trend}), UACR {uacr} mg/g. Recommend continuing {raas} and {sglt2}; "
                         "repeat BMP and UACR in 3 months.").format(**fill)
        if p["prov"] in {"RN", "RD"}:
            plan_full = rng.choice([
                "eGFR {egfr} reviewed ({trend}); reinforced low-sodium diet and medication adherence. Provider to review labs.",
                "Kidney labs reviewed with patient: eGFR {egfr}, UACR {uacr} mg/g. Reviewed renal diet handout; continue {sglt2} as prescribed."]).format(**fill)
        if "metformin" in plan_full and p["dm"] in {"sec", "2_insulin"} | ({"1", "1_hpi_only"}):
            plan_full = rng.choice(v2.CKD_PLAN[:4]).format(**fill)

    old_d, old_v = egfr_rows[-1][0], egfr_rows[-1][1]
    if p["ap"] in {"stale_copy", "per_last_visit"}:
        old_d, old_v = egfr_rows[-1]
    prior_visit_date = (old_d + dt.timedelta(days=rng.randint(0, 6))) if p["ap"] in {"stale_copy", "per_last_visit"} \
        else visit - dt.timedelta(days=rng.randint(85, 190))
    if p["prior_section"] and len(egfr_rows) >= 2 and p["ap"] not in {"stale_copy", "per_last_visit"}:
        prior_visit_date = egfr_rows[-2][0] + dt.timedelta(days=rng.randint(0, 6))
        if prior_visit_date >= recent_date:
            prior_visit_date = egfr_rows[-2][0]

    # ------------------------------------------------------------------ note sections
    def section(title, body):
        return [title] + body + [""]

    prov_name, prov_spec = PROVIDERS[p["prov"]]
    if p["sign"] == "nocred":
        prov_name = prov_name.split(",")[0]
    visit_type = VISIT_TYPE[p["prov"]] if p["encounter"] == "f2f" else \
        "Interprofessional e-consult (chart review; patient not seen)"
    hdr = ["SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY",
           f"Patient ID: {cid}    Age: {age}    Sex: {sex}",
           f"Date of service: {today}    Visit type: {visit_type}",
           f"Clinician: {prov_name} ({prov_spec})" if p["sign"] != "nocred" else f"Clinician: {prov_name}",
           f"Location: Synthetic Primary Care Clinic, Room {rng.randint(2, 14)}", ""]

    if p["encounter"] == "econsult":
        cc = section("REASON FOR E-CONSULT", [rng.choice([
            "Question from primary care team about diabetes and kidney function management.",
            "Chart review requested for chronic disease management; patient not present."])])
    else:
        cc = section("CHIEF COMPLAINT", [rng.choice(v2.CC)])

    hpi = [rng.choice(v2.HPI_OPEN).format(age=age, sexw=sexw, months=rng.choice([3, 4, 6]))]
    if p["encounter"] == "econsult":
        hpi = [f"Chart reviewed for {age}-year-old {sexw}; patient not seen or examined for this consult."]
    yrs = rng.randint(4, 22)
    if p["dm"] == "2":
        hpi.append(f"History of type 2 diabetes diagnosed {yrs} years ago.")
    elif p["dm"] == "2_insulin":
        hpi.append(f"Type 2 diabetes for {yrs} years; started basal insulin {rng.randint(2, 6)} years ago when oral agents were no longer enough.")
    elif p["dm"] == "unspec":
        hpi.append(f"History of diabetes diagnosed {yrs} years ago, managed with metformin.")
    elif dm_type1:
        hpi.append(f"Type 1 diabetes since age {rng.randint(9, 30)}.")
    elif p["sec_kind"] == "steroid":
        hpi.append(f"Steroid-induced diabetes since starting long-term prednisone for polymyalgia rheumatica in {rng.randint(2017, 2022)}.")
    else:
        hpi.append(f"Diabetes since total pancreatectomy for chronic pancreatitis in {rng.randint(2015, 2021)}.")
    if p["dm"] in {"1", "1_hpi_only"} or p["dm"] == "sec":
        add("G1", hpi[-1])
    if p["encounter"] == "econsult":
        hpi.append(f"Glucose log documented at last office visit: fasting {rng.randint(105, 130)}-{rng.randint(135, 175)} mg/dL.")
    else:
        hpi.append(rng.choice(v2.HPI_DM).format(freq=rng.choice(["daily", "twice daily", "a few times a week"]),
                                                lo=rng.randint(105, 130), hi=rng.randint(135, 175), walk=rng.randint(2, 5)))
    yr = rng.randint(2016, 2023)
    if p["hx_ckd_hpi"]:
        hpi.append(f"History of CKD, diagnosed {yr}, followed in this clinic.")
    if p["cause_loc"] == "hpi":
        bank_h = v2.HPI_LINK_DIABETES if p["cause"] == "diabetes" else v2.HPI_LINK_OTHER[p["other"]]
        hpi.append(add("Q3", rng.choice(bank_h).format(pro=pro, Pro=pro.capitalize(), yr=yr)))
    if aki_date:
        hpi.append(f"Hospitalized {fmt_date(aki_date)} with dehydration from viral gastroenteritis; "
                   "creatinine rose and has since returned to baseline.")
    if undated is not None:
        hpi.append(add("Q2", f"Outside lab result brought by patient: eGFR {undated} (date not recorded)."))
    if var == "sentence":
        (d0, e0), (d1, e1) = egfr_rows[0], egfr_rows[-1]
        s0 = f"eGFR was {e0} on {fmt_date(d0)}"
        s1 = f"{e1} on {fmt_date(d1)}"
        add("Q2", s0)
        add("Q2", s1)
        hpi.append(f"Recent kidney labs: {s0} and {s1}.")
    if p["ap"] == "interval_labs":
        hpi.append(add("Q4", rng.choice(B5_INTERVAL).format(**fill)))
    if p["encounter"] == "f2f":
        hpi += rng.sample(v2.HPI_MISC, 2)
    hpi_sec = section("HISTORY OF PRESENT ILLNESS", [" ".join(hpi)])

    ros_sec = [] if p["encounter"] == "econsult" else section(
        "REVIEW OF SYSTEMS", [r.format(eye_yr=rng.randint(2023, 2025)) for r in rng.sample(ROS, rng.randint(6, 9))])

    pl = ["- " + (add("G1", dm_pl) if p["dm"] in {"2", "2_insulin", "unspec", "sec"} else dm_pl)]
    if p["dm"] == "1":
        add("G1", dm_pl)
    if est:
        pl.append("- " + pl_dx)
        add("G2", pl_dx)
        if p["staged"]:
            add("Q1", pl_dx)
        if p["cause_loc"] == "pl":
            add("Q3", pl_dx)
    elif p["ckd"] == "ruled_out":
        pl.append("- Chronic kidney disease (entered 2024) - see assessment")
    if aki_date:
        pl.append(f"- Acute kidney injury ({fmt_date(aki_date)}), resolved")
    for d in distractors:
        pl.append("- " + v2.DISTRACTORS[d][0])
    if p["dm"] == "sec" and p["sec_kind"] == "steroid":
        pl.append("- Polymyalgia rheumatica, on long-term prednisone")
    pmh_sec = section("PAST MEDICAL HISTORY / PROBLEM LIST", pl)
    psh_sec = section("PAST SURGICAL HISTORY", ["- " + x for x in rng.sample(SURGICAL, rng.randint(1, 3))]
                      + (["- Total pancreatectomy (see HPI)"] if p["sec_kind"] == "pancreatectomy" else []))
    fh_sec = section("FAMILY HISTORY", [x.format(fa=rng.randint(62, 80)) for x in rng.sample(FAMILY, rng.randint(2, 3))])
    sh_sec = section("SOCIAL HISTORY", [x.format(quit=rng.randint(1995, 2015), py=rng.randint(5, 30),
                                                 alc=rng.choice(["none", "1 to 2 drinks per week", "rare"]),
                                                 lives=rng.choice(["spouse", "daughter", "alone"]),
                                                 job=rng.choice(["teacher", "machinist", "accountant", "bus driver"]),
                                                 job2=rng.choice(["cashier", "consultant", "librarian"]),
                                                 walk=rng.randint(2, 5))
                                        for x in [rng.choice(SMOKING)] + rng.sample(SOCIAL, 2)])
    med_rec = rng.choice(MED_REC) if p["encounter"] == "f2f" else "Medication list taken from the chart; not reconciled with the patient."
    med_sec = section("MEDICATIONS", ["- " + m for m in meds] + [med_rec])
    all_sec = section("ALLERGIES", [rng.choice(ALLERGIES)])

    if p["encounter"] == "econsult":
        vit_sec = section("VITALS", [f"Last recorded in clinic: BP {bp}, weight {wt} kg (not measured today)."])
        exam_sec = section("EXAM", ["Not performed; patient not seen for this e-consult."])
    else:
        vit_sec = section("VITALS", [f"BP {bp} | HR {rng.randint(62, 92)} | Temp {round(rng.uniform(97.6, 98.8), 1)} F | "
                                     f"Wt {wt} kg | BMI {bmi} | SpO2 {rng.randint(94, 99)}%"])
        exam_sec = section("EXAM", [rng.choice(v2.EXAM)])

    # labs table
    stress = rng.random() < 0.5
    p["stress"] = stress
    sep = (lambda w: "\t" if rng.random() < 0.4 else " " * rng.randint(1, max(2, w // 3))) if stress else None

    def lab_line(d, test, res):
        if stress:
            return f"{fmt_date(d)}{sep(12)}{test}{sep(28)}{res}"
        return f"{fmt_date(d):<12}{test:<28}{res}"

    labs = []
    lab_today = recent_date if current_egfr_shown else visit - dt.timedelta(days=rng.randint(0, 5))
    for d, v in egfr_rows:
        if egfr_in_table:
            labs.append((d, add("Q2", lab_line(d, "eGFR", f"{show(v)} mL/min/1.73m2"))))
        if var == "creat_only" or rng.random() < 0.6:
            labs.append((d, lab_line(d, "Creatinine", f"{creat_for(v)} mg/dL")))
    labs.append((lab_today, lab_line(lab_today, "Hemoglobin A1c", f"{a1c}%")))
    labs.append((lab_today, lab_line(lab_today, "Glucose, fasting", f"{rng.randint(102, 188)} mg/dL")))
    if current_egfr_shown:
        if est or rng.random() < 0.4:
            labs.append((recent_date, lab_line(recent_date, "Urine albumin/creatinine", f"{uacr} mg/g")))
        labs.append((recent_date, lab_line(recent_date, "Potassium", f"{k_val} mmol/L")))
        labs.append((recent_date, lab_line(recent_date, "Sodium", f"{rng.randint(136, 143)} mmol/L")))
    labs.append((lab_today, lab_line(lab_today, "LDL cholesterol", f"{ldl} mg/dL")))
    labs.append((lab_today, lab_line(lab_today, "Hemoglobin", f"{round(rng.uniform(11.2, 14.8), 1)} g/dL")))
    labs.sort(key=lambda x: x[0])
    lab_head = lab_line(dt.date(2000, 1, 1), "Test", "Result").replace("2000-01-01", "Date")
    lab_sec = section("LABS", [lab_head] + [l for _, l in labs])

    # assessment and plan
    items = []
    head = add("G1", dm_ap) if p["dm"] in {"2", "2_insulin", "unspec", "1", "sec"} else dm_ap
    if dm_type1:
        items.append(head + ": " + rng.choice(v2.T1DM_PLAN).format(a1c=a1c))
    elif p["dm"] == "sec":
        items.append(head + f": A1c {a1c}% ({a1c_trend}). Continue current regimen; reviewed glucose log.")
    elif p["encounter"] == "econsult":
        items.append(head + f": A1c {a1c}% ({a1c_trend}). Recommend continuing the current regimen.")
    elif p["prov"] in {"RN", "RD"}:
        items.append(head + f": A1c {a1c}% ({a1c_trend}). Reviewed meal plan and carbohydrate counting; medications per provider.")
    elif p["ap"] == "med_change":
        g3 = rng.choice(G3_LINES).format(**fill)
        add("Q4", g3)
        items.append(head + f": A1c {a1c}% ({a1c_trend}). " + g3)
    else:
        items.append(head + ": " + rng.choice(v2.DM_PLAN).format(a1c=a1c, trend=a1c_trend))

    laundry_pool = []
    ap = p["ap"]
    if est and ap in {"full", "copy_current"}:
        line = rng.choice(B1_LINES).format(**fill) if ap == "copy_current" else plan_full
        items.append(f"{add('G2', dx_ap)}: {add('Q4', line)}")
    elif est and ap == "stale_copy":
        line = rng.choice(B2_LINES).format(old_egfr=old_v, old_date=fmt_date(old_d))
        items.append(f"{add('G2', dx_ap)}: {line}")
    elif est and ap == "copy_plus_new":
        stale = rng.choice(B2_LINES).format(old_egfr=egfr_rows[0][1], old_date=fmt_date(egfr_rows[0][0])) \
            if len(egfr_rows) >= 2 else "Continue current renal regimen."
        new = add("Q4", rng.choice(B3_NEW).format(**fill))
        items.append(f"{add('G2', dx_ap)}: {stale} {new}")
    elif est and ap == "per_last_visit":
        line = rng.choice(B4_LINES).format(old_my=old_d.strftime("%m/%Y"))
        items.append(f"{add('G2', dx_ap)}: {line}")
    elif est and ap == "interval_labs":
        line = add("Q4", rng.choice(B5_LINES).format(**fill))
        items.append(f"{add('G2', dx_ap)}: {line}")
    elif est and ap == "reviewed_stable":
        line = add("Q4", rng.choice(G1_LINES))
        items.append(f"{add('G2', dx_ap)}: {line}")
    elif est and ap == "see_nephro":
        items.append(f"{add('G2', dx_ap)}: {rng.choice(G2_LINES)}")
    elif est and ap == "minimal":
        line = rng.choice(G5_LINES).format(stg=stg, raas=raas)
        items.append(add("G2", add("Q1", add("Q4", line))))
    elif est and ap == "list_entry":
        laundry_pool.append(add("G2", add("Q1", f"CKD {stg}")))
    elif est and ap == "laundry":
        laundry_pool.append(add("G2", dx_ap[0].lower() + dx_ap[1:] if dx_ap.startswith("Chronic") else dx_ap))
        if p["staged"]:
            add("Q1", laundry_pool[-1])
    elif ap == "possible":
        h = rng.choice(v2.POSSIBLE_CKD)
        items.append(add("G2", h) + ": " + rng.choice(v2.POSSIBLE_PLAN).format(egfr=latest, prior=egfr_rows[0][1]))
    elif ap == "aki":
        a, b = rng.choice(v2.AKI_AP)
        items.append(a.format(egfr=latest, aki=fmt_date(aki_date)) + add("G2", b))
    elif ap == "ruled_out":
        old = egfr_rows[0]
        g2 = add("G2", rng.choice(["Does not have chronic kidney disease.", "Chronic kidney disease ruled out."]))
        items.append(f"Chronic kidney disease on problem list, removed today: eGFR {egfr_rows[1][1]} and {latest} on repeat "
                     f"testing over 6 months, urine albumin normal; prior eGFR {old[1]} ({fmt_date(old[0])}) was during an "
                     f"acute illness. {g2}")
    dx_in_ap = est and dx_ap is not None and any(it.startswith(dx_ap + ":") for it in items)
    if dx_in_ap and p["staged"]:
        add("Q1", dx_ap)
    if dx_in_ap and p["cause_loc"] == "ap":
        add("Q3", dx_ap)

    # distractor items; some go into a bare reviewed-problems line
    dlist = list(distractors)
    rng.shuffle(dlist)
    use_list = ap in {"laundry", "list_entry"} or rng.random() < 0.25
    if use_list:
        n_l = rng.randint(1, min(2, len(dlist)))
        laundry_pool += [v2.SHORT_NAME[d] for d in dlist[:n_l]]
        dlist = dlist[n_l:]
    for d in dlist:
        if p["encounter"] == "econsult":
            items.append(f"{v2.SHORT_NAME[d][0].upper() + v2.SHORT_NAME[d][1:]}: stable per chart review; no change recommended.")
        elif p["prov"] in {"RN", "RD"}:
            items.append(f"{v2.SHORT_NAME[d][0].upper() + v2.SHORT_NAME[d][1:]}: managed by primary care provider.")
        else:
            items.append(rng.choice(v2.DISTRACTORS[d][2]).format(bp=bp, ldl=ldl, bmi=bmi, wt=wt))
    head_item, rest = items[:1], items[1:]
    rng.shuffle(rest)
    items = head_item + rest
    if laundry_pool:
        rng.shuffle(laundry_pool)
        bank = G4_LINES if ap == "list_entry" else v2.LAUNDRY
        items.append(rng.choice(bank).format(items=", ".join(laundry_pool)))
    if p["encounter"] == "f2f":
        items.append(" ".join(rng.sample(HEALTH_MAINT, 2)))

    ap_lines = []
    if p["copy_marker"]:
        p["flags"].append("copy_forward_marker")
        ap_lines.append(rng.choice(v2.COPY_MARKERS).format(d=fmt_date(prior_visit_date)))
    ap_lines += [f"{i}. {it}" for i, it in enumerate(items, 1)]
    ap_title = rng.choice(v2.AP_HEADERS) if p["encounter"] == "f2f" else "E-CONSULT ASSESSMENT AND RECOMMENDATIONS"
    ap_sec = section(ap_title, ap_lines)

    # prior-visit section (near-duplicate lines from an earlier visit)
    prior_sec = []
    if p["prior_section"]:
        pv = fmt_date(prior_visit_date)
        lines = [f"{dm_ap}: A1c {prior_a1c}% at that visit; continued medications."]
        if est:
            if p["cause_loc"] == "prior":
                pdx = add("Q3", rng.choice(DX_LINK_STAGE).format(stage=st, dmx=dmx) if p["staged"]
                          else rng.choice(DX_LINK_NOSTAGE).format(dmx=dmx))
            else:
                pdx = dx_ap if dx_ap and ap not in {"list_entry"} else (pl_dx or "Chronic kidney disease")
            if p["staged"] and pdx and ("stage" in pdx or re.search(r"CKD \d", pdx)):
                add("Q1", pdx)
            pv_egfr = [v for d, v in egfr_rows if d <= prior_visit_date]
            tail = f"eGFR {pv_egfr[-1]} at that visit; continued {raas}." if pv_egfr and egfr_in_table else f"continued {raas}."
            lines.append(f"{pdx}: {tail}")
        for d in distractors[:1]:
            lines.append(rng.choice(v2.DISTRACTORS[d][2]).format(bp=bp, ldl=ldl, bmi=bmi, wt=wt))
        prior_sec = section(rng.choice(PRIOR_HDR).format(d=pv), ["(For reference only; not today's assessment.)"] + lines)
        p["flags"].append("prior_visit_section")

    edu_sec = section("PATIENT EDUCATION", rng.sample(EDUCATION, 2)) if p["encounter"] == "f2f" else []
    follow = [f"Return to clinic in {rng.choice([3, 4, 6])} months or sooner as needed."] if p["encounter"] == "f2f" else \
        ["Recommendations sent to the primary care team. Total time spent on chart review: 15 minutes."]
    if p["sign"] == "unsigned":
        sig = ["*** NOTE NOT SIGNED - pending clinician signature ***"]
    elif p["sign"] == "nocred":
        sig = [f"Electronically signed: {prov_name} {today}"]
    else:
        sig = [f"Electronically signed: {PROVIDERS[p['prov']][0]} {today} {rng.randint(8, 17):02d}:{rng.randint(0, 59):02d}"]
    if p["encounter"] == "f2f" and p["prov"] in ACCEPTABLE_PROVIDERS and rng.random() < 0.5:
        follow.append(f"Total time {rng.randint(25, 45)} minutes, more than half in counseling and care coordination.")

    first = [pmh_sec, psh_sec, med_sec, all_sec] if rng.random() < 0.7 else [med_sec, all_sec, pmh_sec, psh_sec]
    social = [fh_sec, sh_sec]
    mid = [vit_sec, exam_sec, lab_sec] if rng.random() < 0.8 else [vit_sec, lab_sec, exam_sec]
    body = hdr + cc + hpi_sec + ros_sec + sum(first, []) + sum(social, []) + sum(mid, []) + prior_sec + ap_sec + edu_sec
    body += follow + sig
    text = "\n".join(body) + "\n"

    # --- intended answers (frozen rubric v2) ---------------------------------------------------
    dated = [(d, v) for d, v in egfr_rows] if var not in {"creat_only"} else []
    a = {
        "G1": YES if p["dm"] in {"2", "2_insulin", "unspec"} else NO,
        "G2": YES if est else (ND if p["ckd"] == "labs" else NO),
        "Q1": YES if (est and p["staged"]) else ND,
        "Q2": answer_q2(dated),
        "Q3": ({"diabetes": YES, "dm_htn": YES, "likely_dm": YES, "other": NO}.get(p["cause"], ND)) if est else ND,
        "Q4": YES if (est and ap in Q4_YES_MODES) else ND,
    }
    label = label_from_facts(p)
    assert label == SCENARIOS[s][3], (cid, s, a, label)
    rubric_label = v2.label_from_answers(a)
    if p["family"] == "F":
        assert rubric_label == 1, (cid, s, a)
    else:
        assert rubric_label == label, (cid, s, a, label)

    # --- format stress ---------------------------------------------------------------------------
    if stress:
        p["flags"].append("format_stress")
        text, ev = apply_noise(text, ev, rng, cid, visit)

    return {
        "chart_id": cid,
        "candidate_code": "E11.22",
        "generator_version": VERSION,
        "label": label,
        "scenario": s,
        "family": p["family"],
        "scenario_description": SCENARIOS[s][1],
        "intended_answers": a,
        "ambiguous_fields": sorted(set(p["ambiguous"])),
        "flags": sorted(set(p["flags"])),
        "evidence": {q: v for q, v in ev.items() if v},
        "facts": {"diabetes": p["dm"], "secondary_kind": p["sec_kind"], "ckd": p["ckd"],
                  "ckd_stage_true": stage if est else None, "staged": p["staged"], "cause": p["cause"],
                  "other_cause": p["other"], "cause_location": p["cause_loc"], "ap_mode": ap,
                  "encounter": p["encounter"], "provider_type": p["prov"], "signature": p["sign"],
                  "egfr_variant": var, "egfr_series": [[fmt_date(d), v] for d, v in egfr_rows],
                  "undated_egfr": undated, "visit_date": today},
        "split": "test",
        "text": text,
    }


# ------------------------------------------------------------------ format noise

OCR_SWAPS = [("l", "1"), ("O", "0"), ("I", "l"), ("rn", "m")]


def apply_noise(text, ev, rng, cid, visit):
    """Apply OCR-style swaps, hyphenated line breaks, a page header and non-ASCII punctuation as edits
    (pos, delete_len, insert). Evidence spans are mapped through the edits so they stay exact."""
    spans = []  # (q, start, end) for every occurrence of every evidence string
    for q, items in ev.items():
        for e in items:
            for m in re.finditer(re.escape(e), text):
                spans.append((q, m.start(), m.end()))
    bounds = {b for _, s0, e0 in spans for b in (s0, e0)}

    def crosses(pos, length):
        """True if the edit would cut across an evidence boundary (partly inside, partly outside)."""
        if length == 0:
            return pos in bounds
        return any(pos < e0 and pos + length > s0 and not (pos >= s0 and pos + length <= e0) for _, s0, e0 in spans)

    edits, used = [], set()

    def ok(pos, length):
        return not crosses(pos, length) and not any(u in used for u in range(pos - 1, pos + max(length, 1) + 1))

    def mark(pos, length):
        used.update(range(pos, pos + max(length, 1)))

    first_text_line = text.index("\n", text.index("Clinician:"))
    ap_start = max(text.find(h) for h in v2.AP_HEADERS + ["E-CONSULT ASSESSMENT"])
    # 1) OCR swaps: half inside the assessment and plan, where most quotes come from
    n_ocr = rng.randint(3, 7)
    for i in range(n_ocr):
        lo = ap_start if (i % 2 == 0 and ap_start > 0) else first_text_line
        for _ in range(50):
            src, dst = rng.choice(OCR_SWAPS)
            pos = text.find(src, rng.randint(lo, len(text) - 2))
            if pos < 0 or not ok(pos, len(src)):
                continue
            edits.append((pos, len(src), dst))
            mark(pos, len(src))
            break
    # 2) hyphenated line breaks inside long words
    words = [m for m in re.finditer(r"[A-Za-z]{9,}", text[first_text_line:])]
    for m in rng.sample(words, min(len(words), rng.randint(1, 3))):
        pos = first_text_line + m.start() + rng.randint(3, len(m.group()) - 3)
        if ok(pos, 0):
            edits.append((pos, 0, "-\n"))
            mark(pos, 0)
    # 3) one page header, either between lines or in the middle of a long line
    hdr = "\n" + PAGE_HDR.format(p=2, n=3, cid=cid, d=fmt_date(visit + dt.timedelta(days=rng.randint(1, 20)))) + "\n"
    long_lines = [m for m in re.finditer(r"[^\n]{160,}", text)]
    for _ in range(30):
        if long_lines and rng.random() < 0.5:
            m = rng.choice(long_lines)
            cands = [m.start() + k for k, ch in enumerate(m.group()) if ch == " "]
            pos = rng.choice(cands)
            if ok(pos, 1):
                edits.append((pos, 1, hdr))
                mark(pos, 1)
                break
        else:
            nl = [k for k, ch in enumerate(text) if ch == "\n" and k > first_text_line]
            pos = rng.choice(nl)
            if ok(pos, 1):
                edits.append((pos, 1, hdr))
                mark(pos, 1)
                break
    # 4) non-ASCII punctuation (forgiven by the verifier's normalization)
    for ch, rep in (("'", "’"), (" - ", " – "), (": ", ": ")):
        for m in list(re.finditer(re.escape(ch), text))[:rng.randint(0, 4)]:
            if ok(m.start(), len(ch)):
                edits.append((m.start(), len(ch), rep))
                mark(m.start(), len(ch))

    edits.sort()
    out, last = [], 0
    for pos, dl, ins in edits:
        out.append(text[last:pos])
        out.append(ins)
        last = pos + dl
    out.append(text[last:])
    new_text = "".join(out)

    def remap(x):
        """Position x in the clean text -> position in the noisy text (edits never straddle a span boundary)."""
        return x + sum(len(ins) - dl for pos, dl, ins in edits if pos + dl <= x and (dl > 0 or pos < x))

    new_ev = {q: [] for q in ev}
    for q, s0, e0 in spans:
        frag = new_text[remap(s0):remap(e0)]
        if frag not in new_ev[q]:
            new_ev[q].append(frag)
    return new_text, new_ev


# --------------------------------------------------------------------------- main

def main(out_dir):
    rng = random.Random(SEED)
    assert sum(v[2] for v in SCENARIOS.values()) == N_TOTAL
    assert sum(v[2] for v in SCENARIOS.values() if v[0] != "F") == N_MAIN
    plan = [s for s, spec in SCENARIOS.items() for _ in range(spec[2])]
    rng.shuffle(plan)
    charts = [build_chart(rng, i + 1, s) for i, s in enumerate(plan)]

    for c in charts:
        for q, spans in c["evidence"].items():
            for sp in spans:
                assert sp in c["text"], (c["chart_id"], q, sp)

    os.makedirs(os.path.join(out_dir, "charts"), exist_ok=True)
    for c in charts:
        with open(os.path.join(out_dir, "charts", f"{c['chart_id']}.txt"), "w") as f:
            f.write(c["text"])
    with open(os.path.join(out_dir, "charts.jsonl"), "w") as f:
        for c in charts:
            f.write(json.dumps(c) + "\n")
    with open(os.path.join(out_dir, "labels.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["chart_id", "family", "label", "scenario", *QUESTIONS, "ambiguous_fields", "flags"])
        for c in charts:
            a = c["intended_answers"]
            w.writerow([c["chart_id"], c["family"], c["label"], c["scenario"], *[a[q] for q in QUESTIONS],
                        ";".join(c["ambiguous_fields"]), ";".join(c["flags"])])
    digest = hashlib.sha256(open(os.path.join(out_dir, "charts.jsonl"), "rb").read()).hexdigest()
    print(f"wrote {len(charts)} charts (v{VERSION}) to {out_dir}; charts.jsonl sha256 {digest}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "data"))
