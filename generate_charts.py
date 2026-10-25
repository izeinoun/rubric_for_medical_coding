"""
Synthetic outpatient chart generator for the evidence-weighted confidence (EWC) pilot. Version 2.

Every chart is scored against one candidate code, E11.22 (type 2 diabetes mellitus with
diabetic chronic kidney disease). Each chart carries:
  - a ground-truth label (1 = documentation supports E11.22 for a risk-adjustment submission)
  - the intended answer to every rubric question (G1, G2, Q1-Q4)
  - the exact evidence strings inserted into the note for each answer
  - a stratified dev/test assignment

Answer semantics
  yes            the note affirmatively documents the fact
  no             the note explicitly documents the opposite, or explicitly says the fact is not established
  not_documented the note is silent

All patients, providers and dates are fictional. Run:  python generate_charts.py [out_dir]

v2 changes (after an independent label audit): split the copy-forward scenario into a supported and a
stale variant, added a "laundry list" negative and a positive with the diabetic link stated only in the
HPI, moved some other-cause attributions to the HPI, widened every phrase bank to reduce label-leaking
phrases, added copy-forward markers to some ordinary charts, made "stable" statements match the eGFR
trend, named the ACE inhibitor or ARB, removed SGLT2 inhibitors from polycystic kidney disease plans,
kept albuminuria below 30 mg/g in AKI and possible-CKD charts, and fixed several smaller inconsistencies.
"""

import csv
import datetime as dt
import hashlib
import json
import os
import sys
import random

SEED = 20261024
N_TOTAL = 200
N_TEST = 60
VERSION = "2"

# scenario id -> (description, count, expected label, test count)
SCENARIOS = {
    "P1_stage_and_link":     ("CKD with stage, explicitly due to type 2 diabetes in the assessment, addressed in plan", 32, 1, 10),
    "P2_with_convention":    ("CKD with stage, no cause stated anywhere, addressed in plan ('with' presumption)", 28, 1, 8),
    "P3_link_no_stage":      ("Diabetic CKD addressed in plan, stage not documented", 14, 1, 4),
    "P4_link_in_hpi":        ("CKD addressed in plan; diabetic cause stated only in the HPI", 8, 1, 2),
    "F1a_copy_fwd_current":  ("Plan carried forward, but CKD line reflects today's results and a current action", 6, 1, 2),
    "F1b_copy_fwd_stale":    ("Plan carried forward with stale eGFR and no sign of current CKD evaluation (needs review)", 6, 0, 2),
    "N1a_problem_list_only": ("CKD on the problem list only, absent from the assessment and plan", 18, 0, 5),
    "N1b_laundry_list":      ("CKD named in a list of problems in the plan, with no status or action", 12, 0, 4),
    "N2_other_cause":        ("CKD attributed to a non-diabetic cause, in the assessment or only in the HPI", 20, 0, 6),
    "N3_labs_only":          ("Low eGFR results, no CKD diagnosis documented", 18, 0, 6),
    "N4_type1":              ("Type 1 diabetes with CKD", 14, 0, 4),
    "N5_uncertain_dx":       ("CKD documented only as possible or not yet established", 14, 0, 4),
    "N6_aki_not_ckd":        ("Resolved acute kidney injury; CKD explicitly absent", 10, 0, 3),
}

QUESTIONS = {
    "G1": "Type 2 diabetes mellitus documented as a current diagnosis",
    "G2": "Chronic kidney disease documented as an established diagnosis",
    "Q1": "CKD stage documented",
    "Q2": "eGFR below 60 on two results at least 90 days apart",
    "Q3": "Provider attributes CKD to diabetes",
    "Q4": "CKD addressed this encounter (monitored, evaluated, assessed or treated)",
}

YES, NO, ND = "yes", "no", "not_documented"

# ---------------------------------------------------------------- phrase banks

CC = [
    "Follow-up of diabetes and chronic conditions.",
    "Routine diabetes follow-up.",
    "3-month follow-up, review of labs.",
    "Chronic disease management visit.",
    "Follow-up visit; medication refills.",
    "Here to go over recent blood work.",
    "Diabetes check and lab review.",
]

HPI_OPEN = [
    "{age}-year-old {sexw} presents for scheduled follow-up.",
    "{age}-year-old {sexw} seen today for routine chronic care.",
    "Patient is a {age}-year-old {sexw} returning for follow-up of chronic conditions.",
    "{age}-year-old {sexw} here for a {months}-month check-in.",
    "Established patient, {age}-year-old {sexw}, presenting for chronic disease follow-up.",
]

HPI_DM = [
    "Reports checking glucose {freq}; fasting readings mostly {lo}-{hi} mg/dL.",
    "Home glucose log reviewed, fasting values {lo}-{hi} mg/dL with occasional post-meal readings above 200.",
    "States adherence to medications is good. Denies hypoglycemic episodes.",
    "Has been trying to walk {walk} times per week. Glucose readings {lo}-{hi} mg/dL fasting.",
    "Notes some difficulty with diet recently; fasting sugars {lo}-{hi} mg/dL.",
    "Brought meter today; morning values {lo}-{hi} mg/dL, no lows.",
]

HPI_MISC = [
    "Denies chest pain, shortness of breath or leg swelling.",
    "No polyuria or polydipsia. No visual changes.",
    "Sleeping reasonably well. Mood is good.",
    "Mild bilateral knee stiffness in the mornings, unchanged.",
    "No urinary symptoms. No foot ulcers or numbness reported.",
    "Appetite stable. Denies nausea or abdominal pain.",
    "Energy fair. No new complaints today.",
]

HPI_LINK_DIABETES = [
    "Nephrology evaluated {pro} kidney disease in {yr} and attributed it to longstanding diabetes.",
    "{Pro} kidney disease was felt by nephrology to be diabetic in origin.",
    "Kidney function decline has been attributed to {pro} diabetes; no other renal disease identified on workup.",
]

HPI_LINK_OTHER = {
    "hypertensive nephrosclerosis": [
        "Followed by nephrology for CKD from hypertensive nephrosclerosis.",
        "Nephrology attributes {pro} kidney disease to long-standing hypertension rather than diabetes.",
    ],
    "polycystic kidney disease": [
        "Known autosomal dominant polycystic kidney disease with resulting CKD, followed by nephrology.",
        "Has polycystic kidney disease (mother also affected), which nephrology considers the cause of {pro} CKD.",
    ],
    "obstructive uropathy": [
        "CKD dates to obstructive uropathy from a prostate problem treated in {yr}; nephrology does not feel it is diabetic.",
        "Kidney disease followed by nephrology, attributed to prior obstructive uropathy.",
    ],
    "IgA nephropathy": [
        "Biopsy in {yr} showed IgA nephropathy as the cause of {pro} kidney disease.",
        "Followed by nephrology for IgA nephropathy, biopsy-proven in {yr}.",
    ],
}

AP_OTHER_CAUSE = {
    "hypertensive nephrosclerosis": ["CKD {stage} due to hypertensive nephrosclerosis",
                                     "Chronic kidney disease {stage}, hypertensive"],
    "polycystic kidney disease": ["CKD {stage} secondary to polycystic kidney disease",
                                  "Chronic kidney disease {stage} due to ADPKD"],
    "obstructive uropathy": ["CKD {stage} from prior obstructive uropathy",
                             "Chronic kidney disease {stage}, post-obstructive"],
    "IgA nephropathy": ["CKD {stage} due to IgA nephropathy",
                        "Chronic kidney disease {stage}, IgA nephropathy"],
}

EXAM = [
    "General: well appearing, no acute distress.\nCV: regular rate and rhythm, no murmur.\nLungs: clear bilaterally.\nExt: no edema.",
    "General: alert, oriented, NAD.\nHeart: RRR.\nLungs: CTAB.\nExtremities: trace bilateral ankle edema.\nFeet: monofilament sensation intact, pulses 2+.",
    "Gen: NAD.\nCV: RRR, normal S1/S2.\nResp: clear to auscultation.\nAbd: soft, nontender.\nExt: no edema; feet without lesions.",
    "General: comfortable.\nCardiac: regular, no gallop.\nPulmonary: no wheezes or crackles.\nSkin: warm and dry.\nExt: no pedal edema.",
]

DISTRACTORS = {
    "htn": ("Essential hypertension", "lisinopril 20 mg daily",
            ["Hypertension: BP {bp} today. Continue lisinopril 20 mg daily. Home BP log reviewed.",
             "HTN: at goal on current regimen. Continue lisinopril.",
             "Essential hypertension: BP {bp}. Reinforced low-sodium diet; continue lisinopril 20 mg."]),
    "hld": ("Hyperlipidemia", "atorvastatin 40 mg nightly",
            ["Hyperlipidemia: LDL {ldl} mg/dL. Continue atorvastatin 40 mg.",
             "HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months."]),
    "obesity": ("Obesity", None,
                ["Obesity, BMI {bmi}: discussed nutrition and activity goals; referred to dietitian.",
                 "Obesity: weight {wt} kg. Continue lifestyle changes."]),
    "oa": ("Osteoarthritis, bilateral knees", "acetaminophen 650 mg as needed",
           ["Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.",
            "OA of knees: continue home exercises and acetaminophen PRN."]),
    "gerd": ("GERD", "omeprazole 20 mg daily",
             ["GERD: symptoms controlled on omeprazole. Continue.",
              "Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit."]),
    "hypothyroid": ("Hypothyroidism", "levothyroxine 75 mcg daily",
                    ["Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.",
                     "Hypothyroid: clinically euthyroid. Continue current dose."]),
    "stones": ("History of nephrolithiasis (2019), no recurrence", None,
               ["History of kidney stones: no recurrence; encouraged fluid intake."]),
    "allergic": ("Seasonal allergic rhinitis", "loratadine 10 mg as needed",
                 ["Allergic rhinitis: seasonal symptoms; continue loratadine PRN."]),
}
SHORT_NAME = {"htn": "hypertension", "hld": "hyperlipidemia", "obesity": "obesity", "oa": "knee osteoarthritis",
              "gerd": "GERD", "hypothyroid": "hypothyroidism", "stones": "history of nephrolithiasis",
              "allergic": "allergic rhinitis"}

STAGE_TEXT = {"3a": "stage 3a", "3b": "stage 3b", "4": "stage 4"}
EGFR_RANGE = {"3a": (45, 59), "3b": (30, 44), "4": (16, 29)}

DX_STAGE_LINK = [
    "Chronic kidney disease {stage} due to type 2 diabetes",
    "CKD {stage} secondary to type 2 diabetes mellitus",
    "Diabetic chronic kidney disease, {stage}",
    "Type 2 diabetes with diabetic CKD {stage}",
    "Diabetic kidney disease, CKD {stage}",
]
DX_STAGE_NOLINK = [
    "Chronic kidney disease {stage}",
    "CKD {stage}",
    "Chronic kidney disease, {stage}",
    "CKD, {stage}",
]
DX_LINK_NOSTAGE = [
    "Chronic kidney disease due to type 2 diabetes",
    "CKD secondary to type 2 diabetes",
    "Diabetic chronic kidney disease",
    "Diabetic kidney disease",
]
OTHER_CAUSES = list(HPI_LINK_OTHER)

CKD_PLAN = [
    "eGFR {egfr} today ({trend}). Continue {sglt2}. Recheck BMP and urine albumin-to-creatinine ratio in 3 months.",
    "Renal function reviewed: eGFR {egfr} ({trend}). Continue {raas} and {sglt2}. Avoid NSAIDs. Nephrology follow-up as scheduled.",
    "eGFR {egfr}, UACR {uacr} mg/g. On {sglt2} and {raas}; counseled on avoiding nephrotoxins. Repeat labs in 3 months.",
    "Latest eGFR {egfr} ({trend}); potassium acceptable. Continue {raas} and {sglt2}. BMP in 3 months.",
    "Labs reviewed with patient, eGFR {egfr}. Continue {sglt2}; metformin dose appropriate for current eGFR. Recheck in 3 to 4 months.",
    "eGFR {egfr} ({trend}), albuminuria {uacr} mg/g. Increased {raas_up}. Repeat potassium and creatinine in 2 weeks.",
]
CKD_PLAN_STAGE4 = [
    "eGFR {egfr} ({trend}). Metformin discontinued given renal function. Continue {sglt2}. Referred to nephrology for co-management.",
    "Advanced kidney disease, eGFR {egfr}. Off metformin. Nephrology following; discussed renal diet and avoidance of contrast and NSAIDs.",
]
CKD_PLAN_T1 = [
    "eGFR {egfr} today ({trend}). Continue {raas}. Recheck BMP and urine albumin-to-creatinine ratio in 3 months.",
    "Renal function reviewed: eGFR {egfr}, UACR {uacr} mg/g. Continue {raas}; avoid NSAIDs. Nephrology follow-up as scheduled.",
]
CKD_PLAN_PKD = [
    "eGFR {egfr} ({trend}). BP goal below 130/80; continue {raas}. Nephrology following; not a tolvaptan candidate at present.",
    "Kidney function eGFR {egfr}. Continue {raas}, encourage fluids. Nephrology visit next month.",
]
CKD_PLAN_STALE = [
    "eGFR {old_egfr} on {old_date}, stable. Continue {sglt2}. Recheck labs in 3 months.",
    "Last eGFR {old_egfr} ({old_date}). Continue current renal regimen. Labs before next visit.",
]

POSSIBLE_CKD = [
    "Possible chronic kidney disease",
    "Rule out chronic kidney disease",
    "Mildly reduced eGFR, CKD not yet established",
    "Decreased eGFR, possible early CKD versus lab variation",
]
POSSIBLE_PLAN = [
    "eGFR {egfr} today, previously {prior}. Repeat BMP and urine albumin in 3 months to confirm chronicity.",
    "eGFR {egfr} (was {prior}). Will recheck renal panel in 90 days; diagnosis deferred until repeat testing.",
    "Single low eGFR of {egfr} after prior {prior}. Encouraged hydration, recheck in 3 months.",
]
AKI_AP = [
    ("History of acute kidney injury, resolved: eGFR {egfr} today, back to baseline. ", "No evidence of chronic kidney disease."),
    ("AKI ({aki}) from volume depletion has resolved; eGFR {egfr}. ", "Kidney function normal; CKD not present."),
    ("Prior AKI, recovered. eGFR {egfr} today. ", "Does not meet criteria for chronic kidney disease."),
]

COPY_MARKERS = [
    "(A/P carried forward from {d}; reviewed and unchanged.)",
    "(Assessment copied from note dated {d} and updated where noted.)",
    "(Plan unchanged from visit of {d}.)",
]
LAUNDRY = ["Problem list reviewed: {items}.", "Also on problem list: {items}."]
AP_HEADERS = ["ASSESSMENT AND PLAN", "ASSESSMENT/PLAN", "IMPRESSION AND PLAN"]

SGLT2 = ["empagliflozin 10 mg daily", "dapagliflozin 10 mg daily"]

DM_PLAN = [
    "A1c {a1c}% today ({trend}). Continue current regimen. Foot exam done; annual eye exam reminder given.",
    "A1c {a1c}%, {trend}. Reviewed diet and activity. Continue medications. Retinal exam due.",
    "A1c {a1c}% ({trend}). Medications unchanged; reinforced carbohydrate counting.",
]
DM_PLAN_GLP1 = "Hemoglobin A1c {a1c}% ({trend}). Discussed adding GLP-1 agonist at next visit if not at goal. Continue current medications."
T1DM_PLAN = [
    "A1c {a1c}%. Continue basal-bolus insulin; reviewed CGM download, time in range 61%. Endocrinology follow-up in 3 months.",
    "A1c {a1c}% on insulin pump. Adjusted overnight basal rate. Continue CGM.",
]

# ------------------------------------------------------------------- helpers

def fmt_date(d):
    return d.strftime("%Y-%m-%d")


def rand_date(rng, start, end):
    return start + dt.timedelta(days=rng.randint(0, (end - start).days))


def answer_q2(egfrs):
    low = [(d, v) for d, v in egfrs if v < 60]
    if len(low) >= 2 and (low[-1][0] - low[0][0]).days >= 90:
        return YES
    if egfrs and egfrs[-1][1] >= 60:
        return NO
    return ND


def label_from_answers(a):
    """E11.22 is supported for risk adjustment when type 2 diabetes and established CKD are
    documented, CKD is addressed this encounter, and the provider has not attributed CKD to a
    different cause (ICD-10-CM 'with' convention presumes the diabetes-CKD link)."""
    return int(a["G1"] == YES and a["G2"] == YES and a["Q3"] != NO and a["Q4"] == YES)


def egfr_trend(egfrs):
    if len(egfrs) < 2:
        return "no prior for comparison"
    prior, latest = egfrs[-2][1], egfrs[-1][1]
    d = latest - prior
    if abs(d) <= 5:
        return f"stable from {prior}"
    return f"up from {prior}" if d > 0 else f"down from {prior}"


# ------------------------------------------------------------------ builder

def build_chart(rng, idx, s):
    ev = {q: [] for q in QUESTIONS}

    def add(q, text):
        ev[q].append(text)
        return text

    sex = rng.choice(["M", "F"])
    sexw = "man" if sex == "M" else "woman"
    pro = "his" if sex == "M" else "her"
    age = rng.randint(48, 84)
    visit = rand_date(rng, dt.date(2026, 1, 12), dt.date(2026, 9, 30))
    flags, ambiguous = [], []

    dm_type = 1 if s == "N4_type1" else 2
    stage = rng.choices(["3a", "3b", "4"], weights=[55, 35, 10])[0]
    st = STAGE_TEXT[stage]

    est = s not in {"N3_labs_only", "N5_uncertain_dx", "N6_aki_not_ckd"}
    staged = est and (s not in {"P3_link_no_stage", "N1a_problem_list_only", "N1b_laundry_list"}
                      or (s == "N1a_problem_list_only" and rng.random() < 0.65)
                      or (s == "N1b_laundry_list" and rng.random() < 0.7))
    link, link_loc, other = None, None, None
    if s in {"P1_stage_and_link", "P3_link_no_stage"}:
        link, link_loc = "diabetes", "ap"
    elif s == "P4_link_in_hpi":
        link, link_loc = "diabetes", "hpi"
    elif s in {"F1a_copy_fwd_current", "F1b_copy_fwd_stale"} and rng.random() < 0.5:
        link, link_loc = "diabetes", "ap"
    elif s == "N1a_problem_list_only" and rng.random() < 0.3:
        link, link_loc = "diabetes", "problem_list"
    elif s == "N4_type1" and rng.random() < 0.5:
        link, link_loc = "diabetes", "ap"
    elif s == "N2_other_cause":
        other = rng.choice(OTHER_CAUSES)
        link, link_loc = "other", ("ap" if rng.random() < 0.6 else "hpi")

    ap_mode = {"N1a_problem_list_only": "none", "N3_labs_only": "none", "N1b_laundry_list": "laundry",
               "F1b_copy_fwd_stale": "stale", "N5_uncertain_dx": "possible", "N6_aki_not_ckd": "aki"}.get(s, "full")

    # --- eGFR series ----------------------------------------------------------
    lo, hi = EGFR_RANGE[stage]
    prior_date = visit - dt.timedelta(days=rng.randint(100, 240))
    recent_date = visit - dt.timedelta(days=rng.randint(0, 10))
    aki_date = None
    if s == "N3_labs_only":
        egfrs = [(prior_date, rng.randint(46, 58)), (recent_date, rng.randint(45, 58))]
    elif s == "N5_uncertain_dx":
        egfrs = [(prior_date, rng.randint(61, 68)), (recent_date, rng.randint(54, 59))]
    elif s == "N6_aki_not_ckd":
        aki_date = visit - dt.timedelta(days=rng.randint(60, 150))
        egfrs = [(aki_date, rng.randint(28, 42)), (recent_date, rng.randint(68, 88))]
    elif s == "F1b_copy_fwd_stale":
        egfrs = [(prior_date, rng.randint(lo, hi)), (recent_date, rng.randint(lo, hi))]
        while egfrs[1][1] == egfrs[0][1]:
            egfrs[1] = (recent_date, rng.randint(lo, hi))
    elif rng.random() < 0.7:
        egfrs = [(prior_date, rng.randint(lo, hi)), (recent_date, rng.randint(lo, hi))]
    else:
        egfrs = [(recent_date, rng.randint(lo, hi))]
    egfrs.sort()
    latest = egfrs[-1][1]
    trend_txt = egfr_trend(egfrs)

    # --- distractors and vitals --------------------------------------------------
    pool = ["htn", "hld", "obesity", "oa", "gerd", "hypothyroid", "allergic"]
    if dm_type == 1:
        pool.remove("htn")
    distractors = rng.sample(pool, rng.randint(2, 4))
    if other == "hypertensive nephrosclerosis" and "htn" not in distractors:
        distractors.append("htn")
    if rng.random() < 0.12:
        distractors.append("stones")

    bp = f"{rng.randint(118, 148)}/{rng.randint(68, 92)}"
    height = rng.uniform(1.62, 1.88) if sex == "M" else rng.uniform(1.52, 1.75)
    bmi = round(rng.uniform(30.5, 38.5) if "obesity" in distractors else rng.uniform(23.5, 29.8), 1)
    wt = round(bmi * height * height, 1)
    ldl = rng.randint(58, 132)
    a1c = round(rng.uniform(6.4, 9.6), 1)
    prior_a1c = round(a1c + rng.choice([-1, 1]) * rng.uniform(0.2, 1.4), 1)
    if rng.random() < 0.15 or prior_a1c == a1c:
        a1c_trend = "unchanged from prior"
    elif prior_a1c > a1c:
        a1c_trend = f"improved from {prior_a1c}%"
    else:
        a1c_trend = f"up from {prior_a1c}%"
    sglt2 = rng.choice(SGLT2)
    low_alb = s in {"N5_uncertain_dx", "N6_aki_not_ckd"}
    uacr = rng.randint(8, 26) if low_alb else rng.randint(35, 420)

    # --- medications --------------------------------------------------------
    meds = []
    on_glp1 = False
    if dm_type == 2:
        if est and stage == "4":
            meds.append("insulin glargine 18 units nightly")
        elif est and stage == "3b":
            meds.append("metformin 500 mg twice daily (renally dosed)")
        else:
            meds.append("metformin 1000 mg twice daily")
        on_sglt2 = (est and other != "polycystic kidney disease") or rng.random() < 0.35
        if on_sglt2:
            meds.append(sglt2)
        if rng.random() < 0.3:
            meds.append("semaglutide 0.5 mg weekly")
            on_glp1 = True
    else:
        meds.append(rng.choice(["insulin glargine 22 units nightly and insulin lispro with meals; continuous glucose monitor",
                                "insulin pump (lispro) with continuous glucose monitor"]))
    if "htn" in distractors:
        raas, raas_up = "lisinopril", "lisinopril to 40 mg daily"
    else:
        raas, raas_up = "losartan", "losartan to 100 mg daily"
        if est or dm_type == 1:
            meds.append("losartan 50 mg daily")
    for d in distractors:
        if DISTRACTORS[d][1]:
            meds.append(DISTRACTORS[d][1])

    # --- CKD diagnosis text -----------------------------------------------------
    dx_ap = None
    if est:
        if link == "other" and link_loc == "ap":
            dx_ap = rng.choice(AP_OTHER_CAUSE[other]).format(stage=st)
        elif link == "diabetes" and link_loc == "ap":
            dx_ap = (rng.choice(DX_STAGE_LINK).format(stage=st) if staged else rng.choice(DX_LINK_NOSTAGE))
            if dm_type == 1:
                dx_ap = dx_ap.replace("type 2 diabetes mellitus", "type 1 diabetes mellitus").replace(
                    "type 2 diabetes", "type 1 diabetes").replace("Type 2 diabetes", "Type 1 diabetes")
        else:
            dx_ap = rng.choice(DX_STAGE_NOLINK).format(stage=st) if staged else "Chronic kidney disease"

    # --- CKD plan text -------------------------------------------------------------
    fill = dict(egfr=latest, trend=trend_txt, sglt2=sglt2.split(" ")[0], raas=raas, raas_up=raas_up, uacr=uacr)
    if dm_type == 1:
        bank = CKD_PLAN_T1
    elif other == "polycystic kidney disease":
        bank = CKD_PLAN_PKD
    elif est and stage == "4":
        bank = CKD_PLAN_STAGE4
    else:
        bank = CKD_PLAN
    plan_ckd = rng.choice(bank).format(**fill)
    if s == "F1b_copy_fwd_stale":
        plan_ckd = rng.choice(CKD_PLAN_STALE).format(old_egfr=egfrs[0][1], old_date=fmt_date(egfrs[0][0]),
                                                     sglt2=sglt2.split(" ")[0])

    # ------------------------------------------------------------------ note text
    def section(title, body_lines):
        return [title] + body_lines + [""]

    hdr = ["SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY",
           f"Patient ID: SYN-{idx:04d}    Age: {age}    Sex: {sex}",
           f"Visit date: {fmt_date(visit)}    Visit type: Office visit, established patient, face-to-face",
           "Provider: Synthetic Provider, MD (Internal Medicine)", ""]

    cc = section("CHIEF COMPLAINT", [rng.choice(CC)])

    hpi = [rng.choice(HPI_OPEN).format(age=age, sexw=sexw, months=rng.choice([3, 4, 6]))]
    if dm_type == 2:
        hpi.append(f"History of type 2 diabetes diagnosed {rng.randint(4, 22)} years ago.")
    else:
        hpi.append(f"Type 1 diabetes since age {rng.randint(9, 30)}.")
    hpi.append(rng.choice(HPI_DM).format(freq=rng.choice(["daily", "twice daily", "a few times a week"]),
                                         lo=rng.randint(105, 130), hi=rng.randint(135, 175), walk=rng.randint(2, 5)))
    yr = rng.randint(2016, 2023)
    if link_loc == "hpi":
        bank_h = HPI_LINK_DIABETES if link == "diabetes" else HPI_LINK_OTHER[other]
        sent = rng.choice(bank_h).format(pro=pro, Pro=pro.capitalize(), yr=yr)
        hpi.append(add("Q3", sent))
    if s == "N6_aki_not_ckd":
        hpi.append(f"Hospitalized {fmt_date(aki_date)} with dehydration from viral gastroenteritis; "
                   "creatinine rose and has since returned to baseline.")
    hpi.append(rng.choice(HPI_MISC))
    hpi_sec = section("HISTORY OF PRESENT ILLNESS", [" ".join(hpi)])

    pl = []
    if dm_type == 2:
        dm_line = rng.choice(["Type 2 diabetes mellitus", "Diabetes mellitus type 2", "T2DM, on oral agents"])
    else:
        dm_line = rng.choice(["Type 1 diabetes mellitus", "Diabetes mellitus type 1, on insulin", "Type 1 DM"])
    pl.append("- " + add("G1", dm_line))
    if est:
        if s == "N1a_problem_list_only":
            pl_dx = (rng.choice(DX_STAGE_LINK).format(stage=st) if staged else rng.choice(DX_LINK_NOSTAGE)) \
                if link == "diabetes" else (rng.choice(DX_STAGE_NOLINK).format(stage=st) if staged else "Chronic kidney disease")
            add("G2", pl_dx)
            if staged:
                add("Q1", pl_dx)
            if link == "diabetes":
                add("Q3", pl_dx)
        elif link == "other" and link_loc == "ap":
            pl_dx = dx_ap
        else:
            pl_dx = rng.choice(DX_STAGE_NOLINK).format(stage=st) if staged else "Chronic kidney disease"
        pl.append("- " + pl_dx)
    if s == "N6_aki_not_ckd":
        pl.append(f"- Acute kidney injury ({fmt_date(aki_date)}), resolved")
    for d in distractors:
        pl.append("- " + DISTRACTORS[d][0])
    pmh_sec = section("PAST MEDICAL HISTORY / PROBLEM LIST", pl)
    med_sec = section("MEDICATIONS", ["- " + m for m in meds])

    vit_sec = section("VITALS", [f"BP {bp} | HR {rng.randint(62, 92)} | Wt {wt} kg | BMI {bmi} | SpO2 {rng.randint(94, 99)}%"])
    exam_sec = section("EXAM", [rng.choice(EXAM)])

    labs = []
    for d, v in egfrs:
        labs.append((d, add("Q2", f"{fmt_date(d):<12}{'eGFR':<28}{v} mL/min/1.73m2")))
    labs.append((recent_date, f"{fmt_date(recent_date):<12}{'Hemoglobin A1c':<28}{a1c}%"))
    if est or rng.random() < 0.4:
        labs.append((recent_date, f"{fmt_date(recent_date):<12}{'Urine albumin/creatinine':<28}{uacr} mg/g"))
    labs.append((recent_date, f"{fmt_date(recent_date):<12}{'Potassium':<28}{round(rng.uniform(3.8, 5.1), 1)} mmol/L"))
    labs.sort(key=lambda x: x[0])
    lab_sec = section("LABS", [f"{'Date':<12}{'Test':<28}Result"] + [l for _, l in labs])

    # assessment and plan
    items = []
    if dm_type == 2:
        head = rng.choice(["Type 2 diabetes mellitus", "Diabetes mellitus, type 2", "T2DM"])
        plans = DM_PLAN + ([DM_PLAN_GLP1] if a1c >= 7.5 and not on_glp1 else [])
        items.append(add("G1", head) + ": " + rng.choice(plans).format(a1c=a1c, trend=a1c_trend))
    else:
        items.append(add("G1", "Type 1 diabetes mellitus") + ": " + rng.choice(T1DM_PLAN).format(a1c=a1c))

    laundry_pool = []
    if ap_mode in {"full", "stale"}:
        items.append(f"{add('G2', dx_ap)}: {plan_ckd}")
        if ap_mode == "full":
            add("Q4", plan_ckd)
        if staged:
            add("Q1", dx_ap)
        if link_loc == "ap":
            add("Q3", dx_ap)
    elif ap_mode == "laundry":
        laundry_pool.append(add("G2", dx_ap[0].lower() + dx_ap[1:] if dx_ap.startswith("Chronic") else dx_ap))
        if staged:
            add("Q1", laundry_pool[-1])
    elif ap_mode == "possible":
        head = rng.choice(POSSIBLE_CKD)
        items.append(add("G2", head) + ": " + rng.choice(POSSIBLE_PLAN).format(egfr=latest, prior=egfrs[0][1]))
        ambiguous.append("Q4")
    elif ap_mode == "aki":
        a, b = rng.choice(AKI_AP)
        items.append(a.format(egfr=latest, aki=fmt_date(aki_date)) + add("G2", b))
        ambiguous.append("Q4")

    # distractors: some go into a bare problem-list line, the rest get their own item
    dlist = list(distractors)
    rng.shuffle(dlist)
    use_laundry = ap_mode == "laundry" or rng.random() < 0.25
    if use_laundry:
        n_l = rng.randint(1, min(2, len(dlist)))
        laundry_pool += [SHORT_NAME[d] for d in dlist[:n_l]]
        dlist = dlist[n_l:]
    for d in dlist:
        items.append(rng.choice(DISTRACTORS[d][2]).format(bp=bp, ldl=ldl, bmi=bmi, wt=wt))
    head_item, rest = items[:1], items[1:]
    rng.shuffle(rest)
    items = head_item + rest
    if laundry_pool:
        rng.shuffle(laundry_pool)
        items.append(rng.choice(LAUNDRY).format(items=", ".join(laundry_pool)))

    ap_lines = []
    copy_fwd = s.startswith("F1") or (s not in {"N5_uncertain_dx", "N6_aki_not_ckd"} and rng.random() < 0.1)
    if copy_fwd:
        flags.append("copy_forward_marker")
        if s == "F1b_copy_fwd_stale":  # cloned from the visit that produced the stale eGFR
            prior_visit = egfrs[0][0] + dt.timedelta(days=rng.randint(0, 7))
        else:
            prior_visit = visit - dt.timedelta(days=rng.randint(85, 190))
        ap_lines.append(rng.choice(COPY_MARKERS).format(d=fmt_date(prior_visit)))
    ap_lines += [f"{i}. {it}" for i, it in enumerate(items, 1)]
    ap_sec = section(rng.choice(AP_HEADERS), ap_lines)

    # vary section order a little
    first = [pmh_sec, med_sec] if rng.random() < 0.75 else [med_sec, pmh_sec]
    mid = [vit_sec, exam_sec, lab_sec] if rng.random() < 0.8 else [vit_sec, lab_sec, exam_sec]
    body = hdr + cc + hpi_sec + sum(first, []) + sum(mid, []) + ap_sec
    body += [f"Return to clinic in {rng.choice([3, 4, 6])} months or sooner as needed.",
             "Electronically signed: Synthetic Provider, MD"]
    text = "\n".join(body) + "\n"

    # --- intended answers ---------------------------------------------------------
    a = {
        "G1": YES if dm_type == 2 else NO,
        "G2": YES if est else (ND if s == "N3_labs_only" else NO),
        "Q1": YES if staged else ND,
        "Q2": answer_q2(egfrs),
        "Q3": {"diabetes": YES, "other": NO}.get(link, ND) if est else ND,
        "Q4": YES if ap_mode == "full" else ND,
    }
    if s == "N3_labs_only":
        ambiguous.append("G2")
    if s in {"N1b_laundry_list", "F1b_copy_fwd_stale"}:
        ambiguous.append("Q4")
    if s == "F1b_copy_fwd_stale":
        flags.append("label_needs_review")

    label = label_from_answers(a)
    assert label == SCENARIOS[s][2], (idx, s, a)

    return {
        "chart_id": f"SYN-{idx:04d}",
        "candidate_code": "E11.22",
        "generator_version": VERSION,
        "label": label,
        "scenario": s,
        "scenario_description": SCENARIOS[s][0],
        "intended_answers": a,
        "ambiguous_fields": sorted(set(ambiguous)),
        "flags": flags,
        "evidence": {q: v for q, v in ev.items() if v},
        "facts": {"diabetes_type": dm_type, "ckd_stage_true": stage if est else None,
                  "other_cause": other, "link_location": link_loc,
                  "egfr_series": [[fmt_date(d), v] for d, v in egfrs]},
        "text": text,
    }


def main(out_dir):
    rng = random.Random(SEED)
    assert sum(v[1] for v in SCENARIOS.values()) == N_TOTAL
    assert sum(v[3] for v in SCENARIOS.values()) == N_TEST

    plan = [s for s, spec in SCENARIOS.items() for _ in range(spec[1])]
    rng.shuffle(plan)
    charts = [build_chart(rng, i + 1, s) for i, s in enumerate(plan)]

    by_s = {}
    for c in charts:
        by_s.setdefault(c["scenario"], []).append(c)
    for s, cs in by_s.items():
        test_ids = {c["chart_id"] for c in rng.sample(cs, SCENARIOS[s][3])}
        for c in cs:
            c["split"] = "test" if c["chart_id"] in test_ids else "dev"

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
        w.writerow(["chart_id", "split", "label", "scenario", *QUESTIONS, "ambiguous_fields", "flags"])
        for c in charts:
            a = c["intended_answers"]
            w.writerow([c["chart_id"], c["split"], c["label"], c["scenario"], *[a[q] for q in QUESTIONS],
                        ";".join(c["ambiguous_fields"]), ";".join(c["flags"])])
    with open(os.path.join(out_dir, "rubric_questions.json"), "w") as f:
        json.dump({"questions": QUESTIONS,
                   "answer_values": {YES: "the note affirmatively documents the fact",
                                     NO: "the note explicitly documents the opposite or says it is not established",
                                     ND: "the note is silent"}}, f, indent=2)

    digest = hashlib.sha256(open(os.path.join(out_dir, "charts.jsonl"), "rb").read()).hexdigest()
    print(f"wrote {len(charts)} charts (v{VERSION}) to {out_dir}; charts.jsonl sha256 {digest}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
