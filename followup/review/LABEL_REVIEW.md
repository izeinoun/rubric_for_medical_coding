# Label review: 40 follow-up charts

For each chart, read the note and decide whether the **label** (does the note support reporting E11.22 for risk adjustment?) is right, using the reason and the checks given. You do not need to check the rubric answers. Record your verdict in `label_review.csv` (agree / disagree, plus a short note), or just list the chart IDs you disagree with.

About 45% of charts have deliberate 'format noise' (letters swapped with digits such as 'C1inician', words broken across lines, a stray page header). That is intended and is not an error.

Label rules: supported (1) only if type 2 diabetes is documented (untyped diabetes defaults to type 2), CKD is an established diagnosis, CKD is addressed at this visit, no non-diabetic cause is given for the CKD, the visit is face-to-face with an MD, DO, NP or PA (R1), and the note is signed with credentials (R2). Secondary diabetes is not type 2 (R3).

## 1. FU-0008 — A_N1a_problem_list_only

**Label: 0 (does not support E11.22).** CKD appears only on the problem list; the assessment and plan does not address it.

Check:
- [ ] No CKD line in the assessment and plan (a prior-visit section, if any, is not today's plan).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0008    Age: 66    Sex: F
Date of service: 2026-09-16    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 6

CHIEF COMPLAINT
Follow-up visit; medication refills.

HISTORY OF PRESENT ILLNESS
66-year-old woman seen today for routine chronic care. History of type 2 diabetes diagnosed 15 years ago. Notes some difficulty with diet recently; fasting sugars 121-145 mg/dL. No polyuria or polydipsia. No visual changes. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Constitutional: denies fever, chills or unintended weight loss.
Genitourinary: no dysuria, hematuria or change in urine output.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Respiratory: no cough or dyspnea on exertion.
Neurological: no numbness or tingling in the feet; no headaches.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD stage 3a
- Seasonal allergic rhinitis
- Hypothyroidism
- Obesity

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- levothyroxine 75 mcg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Father: coronary artery disease, died age 77.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Walks 5 times per week, about 20 minutes.
Lives with spouse. Retired teacher.

VITALS
BP 144/92 | HR 86 | Temp 97.8 F | Wt 101.1 kg | BMI 38.2 | SpO2 99%

LABS
Date  Test                        Result
2026-04-16  eGFR                        57 mL/min/1.73m2
2026-04-16  Creatinine                  1.08 mg/dL
2026-09-09  eGFR                        50 mL/min/1.73m2
2026-09-09  Creatinine                  1.24 mg/dL
2026-09-09  Hemoglobin A1c              7.2%
2026-09-09  Glucose, fasting            110 mg/dL
2026-09-09  Urine albumin/creatinine    256 mg/g
2026-09-09  Potassium                   4.2 mmol/L
2026-09-09  Sodium                      139 mmol/L
2026-09-09  LDL cholesterol             124 mg/dL
2026-09-09  Hemoglobin                  14.4 g/dL

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus: A1c 7.2% (up from 6.3%). Medications unchanged; reinforced carbohydrate counting.
2. Obesity, BMI 38.2: discussed nutrition and activity goals; referred to dietitian.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. Hypothyroid: clinically euthyroid. Continue current dose.
5. Colorectal cancer screening up to date. Shingles vaccine series completed.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Reviewed sick-day rules for medications.

Return to clinic in 6 months or sooner as needed.
Total time 40 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-09-16 10:58
```

</details>

## 2. FU-0012 — F1_non_acceptable_provider

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but the visit is by a nurse or dietitian only, not an acceptable provider (rule R1).

Check:
- [ ] Header and signature show RN or RD.
- [ ] Otherwise the chart would support E11.22.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0012    Age: 57    Sex: F
Date of service: 2026-05-05    Visit type: Medical nutrition therapy visit, in person
Clinician: Synthetic Dietitian, RD (Medical Nutrition Therapy)
Location: Synthetic Primary Care Clinic, Room 2

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
Patient is a 57-year-old woman returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 11 years ago. Has been trying to walk 3 times per week. Glucose readings 121-143 mg/dL fasting. No urinary symptoms. No foot ulcers or numbness reported. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Constitutional: denies fever, chills or unintended weight loss.
Respiratory: no cough or dyspnea on exertion.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2023.
Skin: no rashes or non-healing wounds.
Neurological: no numbness or tingling in the feet; no headaches.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- atorvastatin 40 mg nightly
- omeprazole 20 mg daily
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Penicillin (rash).

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease stage 3a
- Hyperlipidemia
- GERD
- Essential hypertension

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Cholecystectomy (2011)

FAMILY HISTORY
Brother: hyperlipidemia.
No family history of kidney disease reported.
Father: coronary artery disease, died age 76.

SOCIAL HISTORY
Former smoker, quit 1998; 16 pack-years.
Lives with alone. Retired machinist.
Works part time as a cashier.

VITALS
BP 146/77 | HR 92 | Temp 97.7 F | Wt 58.4 kg | BMI 24.3 | SpO2 97%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2026-04-28  eGFR                        48 mL/min/1.73m2
2026-04-28  Creatinine                  1.29 mg/dL
2026-04-28  Hemoglobin A1c              9.0%
2026-04-28  Glucose, fasting            150 mg/dL
2026-04-28  Urine albumin/creatinine    336 mg/g
2026-04-28  Potassium                   4.5 mmol/L
2026-04-28  Sodium                      136 mmol/L
2026-04-28  LDL cholesterol             64 mg/dL
2026-04-28  Hemoglobin                  12.7 g/dL

ASSESSMENT/PLAN
1. Type 2 diabetes mellitus: A1c 9.0% (up from 8.5%). Reviewed meal plan and carbohydrate counting; medications per provider.
2. CKD, stage 3a: eGFR 48 reviewed (no prior for comparison); reinforced low-sodium diet and medication adherence. Provider to review labs.
3. Hypertension: managed by primary care provider.
4. Hyperlipidemia: managed by primary care provider.
5. GERD: managed by primary care provider.
6. Dental visit within the past year. Influenza vaccine given this season.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Patient verbalized understanding of the plan.

Return to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Dietitian, RD 2026-05-05 15:54
```

</details>

## 3. FU-0022 — A_N5_uncertain_dx

**Label: 0 (does not support E11.22).** CKD only possible or not yet established.

Check:
- [ ] The CKD wording is 'possible', 'rule out' or 'not yet established'.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0022    Age: 50    Sex: M
Date of service: 2026-02-20    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
50-year-old man seen today for routine chronic care. History of type 2 diabetes diagnosed 15 years ago. Has been trying to walk 2 times per week. Glucose readings 130-162 mg/dL fasting. Denies chest pain, shortness of breath or leg swelling. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Neurological: no numbness or tingling in the feet; no headaches.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Genitourinary: no dysuria, hematuria or change in urine output.
Cardiovascular: no chest pain, palpitations or orthopnea.
Eyes: no blurred vision; last dilated eye exam 2024.
Constitutional: denies fever, chills or unintended weight loss.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Skin: no rashes or non-healing wounds.
Respiratory: no cough or dyspnea on exertion.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Hyperlipidemia
- Osteoarthritis, bilateral knees
- GERD
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Appendectomy (1988)

MEDICATIONS
- metformin 1000 mg twice daily
- atorvastatin 40 mg nightly
- acetaminophen 650 mg as needed
- omeprazole 20 mg daily
- loratadine 10 mg as needed
Med rec done with patient's pill bottles.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
Brother: hyperlipidemia.
Mother: hypertension.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Works part time as a librarian.
Walks 5 times per week, about 20 minutes.

VITALS
BP 138/69 | HR 89 | Temp 98.2 F | Wt 65.2 kg | BMI 23.5 | SpO2 97%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2025-09-03  eGFR                        64 mL/min/1.73m2
2025-09-03  Creatinine                  0.96 mg/dL
2026-02-17  eGFR                        57 mL/min/1.73m2
2026-02-17  Hemoglobin A1c              6.6%
2026-02-17  Glucose, fasting            144 mg/dL
2026-02-17  Potassium                   4.9 mmol/L
2026-02-17  Sodium                      139 mmol/L
2026-02-17  LDL cholesterol             113 mg/dL
2026-02-17  Hemoglobin                  12.7 g/dL

IMPRESSION AND PLAN
1. Type 2 diabetes mellitus: A1c 6.6%, up from 6.0%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. Rule out chronic kidney disease: eGFR 57 today, previously 64. Repeat BMP and urine albumin in 3 months to confirm chronicity.
5. GERD: symptoms controlled on omeprazole. Continue.
6. OA of knees: continue home exercises and acetaminophen PRN.
7. Influenza vaccine given this season. Colorectal cancer screening up to date.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 6 months or sooner as needed.
Total time 36 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Practitioner, FNP-C 2026-02-20 12:57
```

</details>

## 4. FU-0029 — B1_copy_current

**Label: 1 (supports E11.22).** Copied plan, but the CKD line cites today's eGFR with today's date and a current action.

Check:
- [ ] Copy-forward marker present.
- [ ] CKD line: today's eGFR (dated the visit day) and an action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0029    Age: 71    Sex: M
Date of service: 2026-07-09    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 9

CHIEF COMPLAINT
Follow-up visit; medication refills.

HISTORY OF PRESENT ILLNESS
71-year-old man here for a 3-month check-in. History of type 2 diabetes diagnosed 22 years ago. Reports checking glucose daily; fasting readings mostly 106-160 mg/dL. Sleeping reasonably well. Mood is good. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Constitutional: denies fever, chills or unintended weight loss.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Cardiovascular: no chest pain, palpitations or orthopnea.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease stage 3a
- Essential hypertension
- Osteoarthritis, bilateral knees
- Obesity
- Hypothyroidism

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)
- Tonsillectomy (childhood)
- Cholecystectomy (2011)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- dapagliflozin 10 mg daily
- lisinopril 20 mg daily
- acetaminophen 650 mg as needed
- levothyroxine 75 mcg daily
Med rec done with patient's pill bottles.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
No family history of kidney disease reported.
Mother: hypertension.

SOCIAL HISTORY
Former smoker, quit 2003; 14 pack-years.
Alcohol: none.
Works part time as a consultant.

VITALS
BP 135/76 | HR 81 | Temp 97.6 F | Wt 111.1 kg | BMI 33.7 | SpO2 99%

LABS
Date  Test                        Result
2026-03-30  eGFR                        54 mL/min/1.73m2
2026-03-30  Creatinine                  1.14 mg/dL
2026-07-09  eGFR                        52 mL/min/1.73m2
2026-07-09  Creatinine                  1.19 mg/dL
2026-07-09  Hemoglobin A1c              8.1%
2026-07-09  Glucose, fasting            137 mg/dL
2026-07-09  Urine albumin/creatinine    335 mg/g
2026-07-09  Potassium                   4.6 mmol/L
2026-07-09  Sodium                      137 mmol/L
2026-07-09  LDL cholesterol             66 mg/dL
2026-07-09  Hemoglobin                  14.6 g/dL

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

ASSESSMENT/PLAN
(Plan unchanged from visit of 2026-03-09.)
1. Type 2 diabetes mellitus: A1c 8.1%, up from 7.6%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
3. OA of knees: continue home exercises and acetaminophen PRN.
4. Hypertension: BP 135/76 today. Continue lisinopril 20 mg daily. Home BP log reviewed.
5. CKD, stage 3a: Today's eGFR 52 (2026-07-09), stable from 54. Continue lisinopril and dapagliflozin. Labs again in 3 months.
6. Obesity: weight 111.1 kg. Continue lifestyle changes.
7. Retinal exam due; referral placed. Shingles vaccine series completed.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Reviewed sick-day rules for medications.

Return to clinic in 4 months or sooner as needed.
Total time 39 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-07-09 14:51
```

</details>

## 5. FU-0032 — C4_secondary_dm

**Label: 0 (does not support E11.22).** Secondary diabetes (steroid-induced or after pancreatectomy) is not type 2 (rule R3).

Check:
- [ ] The diabetes is described as steroid-induced or due to pancreatectomy.
- [ ] Nowhere says type 2.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0032    Age: 76    Sex: F
Date of service: 2026-09-08    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 4

CHlEF COMPLAINT
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
76-year-old woman presents for scheduled follow-up. Steroid-induced diabetes
--- Page 2 of 3 --- FU-0032 --- printed 2026-09-18 ---
since starting long-term prednisone for polymyal-
gia rheumatica in 2017. Notes some difficulty with diet recently; fasting sugars 114-175 mg/dL. Energy fair. No new complaints today. Mild bilateral knee stiffness in the mornings, unchanged.

REVIEW OF SYSTEMS
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Respiratory: no cough or dyspnea on exertion.
Eyes: no blurred vision; last dilated eye exam 2024.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Cardiovascular: no chest pain, palpitations or orthopnea.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Constitutional: denies fever, chills or unintended weight loss.

PAST MEDICAL HISTORY / PROBLEM LIST
- Steroid-induced diabetes mellitus
- CKD, stage 4
- Osteoarthritis, bilateral knees
- GERD
- Obesity
- Seasonal allergic rhinitis
- Polymyalgia rheumatica, on long-term prednisone

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Right knee arthroscopy (2015)
- Appendectomy (1988)

MEDICATIONS
- prednisone 10 mg daily (polymyalgia rheumatica)
- glipizide 5 mg daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- omeprazole 20 mg daily
- loratadine 10 mg as needed
Med rec done with patient’s pill bottles.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Mother: hypertension.
Sister: hypothyroidism.

SOCIAL HISTORY
Never smoker.
Walks 2 times per week, about 20 minutes.
Works part time as a librarian.

VITALS
BP 138/87 | HR 68 | Temp 98.2 F | Wt 80.3 kg | BMI 33.2 | SpO2 97%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date Test	Result
2026-04-26	eGFR    24 mL/min/1.73m2
2026-09-01  eGFR	20 mL/min/1.73m2
2026-09-01   Creatinine      3.09 mg/dL
2026-09-01    Hemoglobin A1c     6.5%
2026-09-01 Glucose, fasting       180 mg/dL
2026-09-01	Urine albumin/creatinine	59 mg/g
2026-09-01  Potassium         5.0 mmol/L
2026-09-01  Sodium	143 mmol/L
2026-09-01	LDL cholesterol   90 mg/dL
2026-09-01 Hemoglobin     13.1 g/dL

PRIOR VISIT SUMMARY (2026-04-30)
(For reference only; not today’s assessment.)
Steroid-induced diabetes mellitus: A1c 5.3% at that visit; continued medications.
Chronic kidney disease, stage 4: eGFR 24 at that visit; continued losartan.
Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.

ASSESSMENT/PLAN
1. Steroid-induced diabetes mellitus: A1c 6.5% (up from 5.3%). Continue current regimen; reviewed g1ucose log.
2. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
3. GERD: symptoms controlled on omeprazole. Continue.
4. Chronic kidney disease, stage 4: eGFR 20 (stable from 24). Metformin discontinued given renal function. Continue dapagliflozin. Referred to nephrology for co-management.
5. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
6. 0besity: weight 80.3 kg. Continue lifestyle changes.
7. Diabetic foot exam completed today. Pneumococcal vacc-
ination up to date.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Reviewed carbohydrate counting handout.

Return to clinic in 6 months or sooner as needed.
Total time 39 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-09-08 13:06
```

</details>

## 6. FU-0040 — D_creat_only_neg

**Label: 0 (does not support E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0040    Age: 61    Sex: M
Date of service: 2026-06-17    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 3

CHIEF COMPLAINT
Follow-up visit; medication refills.

HISTORY OF PRESENT ILLNESS
61-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 7 years ago. Home glucose log reviewed, fasting values 123-162 mg/dL with occasional post-meal readings above 200. No urinary symptoms. No foot ulcers or numbness reported. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Neurological: no numbness or tingling in the feet; no headaches.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Consti-
tutional: denies fever, chills or unintended weight loss.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2025.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- CKD stage 3b
- Obesity
- Essential hypertension
- GERD
- Hypothyroidism

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Colonoscopy with polypectomy (2021)
- Appendectomy (1988)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- lisinopril 20 mg daily
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Mother: hypertension.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2014; 19 pack-years.
Lives with daughter. Retired teacher.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 130/91 | HR 83 | Temp 98.6 F | Wt 101.6 kg | BMI 33.7 | SpO2 97%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
--- Page 2 of 3 --- FU-0040 --- printed 2026-07-04 ---
Date  Test         Result
2026-02-01  Creatinine        1.67 mg/dL
2026-06-16   Creatinine      1.87 mg/dL
2026-06-16    Hemoglobin A1c      9.4%
2026-06-16    Glucose, fasting	107 mg/dL
2026-06-16   Urine albumin/creatinine         137 mg/g
2026-06-16	Potassium  4.7 mmol/L
2026-06-16 Sodium	138 mmol/L
2026-06-16   LDL cholesterol  121 mg/dL
2026-06-16   Hemoglobin	12.8 g/dL

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus: A1c 9.4% (improved from 10.1%). Medications unchanged; reinforced carbohydrate counting.
2. Obesity: weight 101.6 kg. Continue lifestyle changes.
3. HTN: at goal on current regimen. Continue lis-
inopril.
4. Hypothyroid: clinically euthyroid. Continue current dose.
5. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
6. Retinal exam due; referral placed. Shingles vaccine series completed.

PATlENT EDUCATI0N
Reviewed sick-day rules for medications.
Discussed hypoglycemia recognition and treatment.

Retum to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-06-17 13:07
```

</details>

## 7. FU-0050 — D_gap90_neg

**Label: 0 (does not support E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0050    Age: 48    Sex: M
Date of service: 2026-08-05    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
Patient is a 48-year-old man returning for follow-up of chronic conditions. History of type
--- Page 2 of 3 --- FU-0050 --- printed 2026-08-24 ---
2 diabetes diagnosed 14 years ago. Reports checking glucose a few times a week; fasting readings mostly 118-143 mg/dL. Appetite stable. Denies nausea or abdominal pain. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Genitourinary: no dysuria, hematuria or change in urine output.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Skin: no rashes or non-healing wounds.
Neurological: no numbness or tingling in the feet; no headaches.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- lisinopril 20 mg daily
- loratadine 10 mg as needed
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Penicillin (rash).

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD stage 3a
- Essential hypertension
- Seasonal allergic rhinitis
- Obesity

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Colonoscopy with polypectomy (2021)

FAMILY HISTORY
Mother: hypertension.
Father: coronary artery disease, died age 74.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 2010; 20 pack-years.
Walks 5 times per week, about 20 minutes.
Alcohol: none.

VITALS
BP 126/72 | HR 70 | Temp 97.9 F | Wt 93.8 kg | BMI 31.6 | SpO2 98%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test        Result
2026-05-03   eGFR	51 mL/min/1.73m2
2026-08-01   eGFR	46 mL/min/1.73m2
2026-08-01	Creatinine 1.34 mg/dL
2026-08-01    Hemogl-
obin A1c     8.0%
2026-08-01  Glucose, fasting        172 mg/dL
2026-08-01	Urine albumin/creatinine         287 mg/g
2026-08-01 Potassium	3.9 mmol/L
2026-08-01  Sodium       143 mmol/L
2026-08-01 LDL cholesterol  110 mg/dL
2026-08-01   Hemoglobin    13.5 g/dL

IMPRESSION AND PLAN
1. Type 2 diabetes mellitus: A1c 8.0%, up from 7.8%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. 0besity: weight 93.8 kg. Continue lifestyle changes.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. Essential hypertension: BP 126/72. Reinforced 1ow-sodium diet; continue lisinopril 20 mg.
5. Pneumococcal vaccination up to date. Influenza vaccine given this season.

PATIENT EDUCATI0N
Enc-
ouraged 150 minutes of moderate activity weekly.
Reviewed sick-day rules for medications.

Retum to clinic in 3 months or sooner as needed.
Total time 33 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-08-05 13:59
```

</details>

## 8. FU-0052 — B4_per_last_visit

**Label: 0 (does not support E11.22).** CKD line says only 'per last visit / unchanged from <month>'; today's labs are not mentioned.

Check:
- [ ] No eGFR from the last 30 days anywhere.
- [ ] The CKD line has no current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0052    Age: 76    Sex: F
Date of service: 2026-09-14    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 14

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
76-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 14 years ago. Home glucose log reviewed, fasting values 109-135 mg/dL with occasional post-meal readings above 200. Appetite stable. Denies nausea or abdominal pain. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Eyes: no blurred vision; last dilated eye exam 2023.
Constitutional: denies fever, chills or unintended weight loss.
Cardiovascular: no chest pain, palpitations or orthopnea.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease, stage 3a
- Obesity
- GERD
- Hyperlipidemia

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Right knee arthroscopy (2015)

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- atorvastatin 40 mg nightly
Med rec done with patient's pill bottles.

ALLERGIES
NKDA.

FAMILY HISTORY
Mother: hypertension.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Alcohol: rare.
Lives with alone. Retired machinist.

VITALS
BP 139/83 | HR 70 | Temp 98.1 F | Wt 92.7 kg | BMI 36.5 | SpO2 99%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2026-02-16  eGFR                        52 mL/min/1.73m2
2026-02-16  Creatinine                  1.19 mg/dL
2026-07-15  eGFR                        55 mL/min/1.73m2
2026-07-15  Creatinine                  1.12 mg/dL
2026-09-09  Hemoglobin A1c              8.8%
2026-09-09  Glucose, fasting            105 mg/dL
2026-09-09  LDL cholesterol             119 mg/dL
2026-09-09  Hemoglobin                  14.3 g/dL

ASSESSMENT/PLAN
(A/P carried forward from 2026-07-16; reviewed and unchanged.)
1. T2DM: A1c 8.8% today (up from 8.0%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. CKD stage 3a secondary to type 2 diabetes: Unchanged from 07/2026; per last visit.
3. Hyperlipidemia: LDL 119 mg/dL. Continue atorvastatin 40 mg.
4. Obesity: weight 92.7 kg. Continue lifestyle changes.
5. GERD: symptoms controlled on omeprazole. Continue.
6. Colorectal cancer screening up to date. Dental visit within the past year.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Patient verbalized understanding of the plan.

Return to clinic in 4 months or sooner as needed.
Total time 35 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-09-14 16:00
```

</details>

## 9. FU-0066 — F2_unsigned

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but the note is unsigned or signed without credentials (rule R2).

Check:
- [ ] The note is marked not signed, or the signature has no MD/DO/NP/PA credential.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0066    Age: 61    Sex: M
Date of service: 2026-01-30    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician
Location: Synthetic Primary Care Clinic, Room 3

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
Patient is a 61-year-old man retu-
rning for follow-up of chronic conditions. History of type 2 diabetes diagno-
sed 12 years ago. Home glucose log reviewed, fasting values 130-160 mg/dL with occasional post-meal readings above 200. Denies chest pain, shortness of breath or leg swelling. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Respiratory: no cough or dyspnea on exertion.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Genitourinary: no dysuria, hematuria or change in urine output.
Cardiovascular: no chest pain, palpitations or orthopnea.
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease stage 3b
- Hypothyroidism
- GERD
- Seasonal allergic rhinitis
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Appendectomy (1988)

MEDICATI0NS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- losartan 50 mg daily
- levothyroxine 75 mcg daily
- omeprazole 20 mg daily
- loratadine 10 mg as needed
- acetaminophen 650 mg as needed
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
No known drug allergies.
--- Page 2 of 3 --- FU-0066 --- printed 2026-02-10 ---

FAMILY HISTORY
Brother: hyperlipidemia.
Father: coronary artery disease, died age 63.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Lives with daughter. Retired teacher.
Works part time as a librarian.

VITALS
BP 132/89 | HR 73 | Temp 97.8 F | Wt 63.3 kg | BMI 23.5 | SpO2 96%

LABS
Date    Test         Result
2026-01-29 eGFR       37 mL/min/1.73m2
2026-01-29   Hemoglobin A1c         8.9%
2026-01-29    Glucose, fasting     120 mg/dL
2026-01-29  Urine albumin/creatinine       45 mg/g
2026-01-29	Potassium       4.0 mmol/L
2026-01-29	Sodium	142 mmol/L
2026-01-29  LDL cholesterol      60 mg/dL
2026-01-29   Hemoglobin	14.5 g/dL

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

FROM LAST OFFICE VISIT (2025-09-09)
(For reference only; not today’s assessment.)
Type 2 diabetes mellitus: A1c 7.9% at that visit; continued medications.
Chronic kidney disease stage 3b: continued losartan.
Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus: A1c 8.9%, up from 7.9%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hypo-
thyroid: clinically euthyroid. Continue current dose.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. Chronic kidney disease stage 3b: Labs reviewed with patient, eGFR 37. Continue empagliflozin; metformin dose appropriate for current eGFR. Recheck in 3 to 4 months.
5. GERD: symptoms controlled on omeprazole. Continue.
6. OA of knees: continue home exercises and acetaminophen PRN.
7. Dental visit within the past year. Colorectal cancer screening up to date.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity week1y.
Discussed hypoglycemia recognition and treatment.

Retum to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Physician 2026-01-30
```

</details>

## 10. FU-0077 — E1_dm_and_htn

**Label: 1 (supports E11.22).** CKD due to diabetes and hypertension; diabetes is a stated cause. CKD addressed today.

Check:
- [ ] The plan states both diabetes and hypertension as causes.
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0077    Age: 58    Sex: F
Date of service: 2026-01-25    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 11

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
Patient is a 58-year-old woman returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 5 years ago. Brought meter today; morning values 125-165 mg/dL, no lows. Denies chest pain, shortness of breath or leg swelling. No polyuria or polydipsia. No visual changes.

REVIEW 0F SYSTEMS
Musculoskeletal: chronic knee stiffness, otherwise negative.
Respiratory: no cough or dyspnea on exertion.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Eyes: no blurred vision; last dilated eye exam 2025.
Genitour-
inary: no dysuria, hematuria or change in urine output.
Neurological: no numbness or tingling in the feet; no headaches.
Constitutional: denies fever, chills or unintended weight loss.

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- loratadine 10 mg as needed
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Penicillin (rash).

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- CKD stage 3b
- Seasonal allergic rhinitis
- Obesity
- Essential hypertension

PAST SURGICAL HISTORY
- Cholecystectomy (2011)

FAMILY HISTORY
Sister: hypothyroid-
ism.
Father: coronary artery disease, died age 80.

SOCIAL HISTORY
Former smoker, quit 2001; 14 pack-years.
Wa1ks 2 times per week, about 20 minutes.
Lives with daughter. Retired bus driver.

VITALS
BP 119/89 | HR 62 | Temp 98.4 F | Wt 93.1 kg | BMI 34.4 | SpO2 97%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date    Test	Result
2026-01-21   eGFR	30 mL/min/1.73m2
2026-01-21    Creatinine      2.06 mg/dL
2026-01-21	Hemoglobin A1c	8.8%
2026-01-21	Glucose, fasting     136 mg/dL
2026-01-21   Urine albumin/creatinine    101 mg/g
2026-01-21	Potassium	4.3 mmol/L
2026-01-21  Sodium	141 mmol/L
2026-01-21	LDL cholesterol  130 mg/dL
2026-01-21	Hemoglobin	12.8 g/dL

FROM LAST OFFICE VISIT (2025-07-20)
(For reference only; not today’s assessment.)
Diabetes mellitus, type 2: A1c 8.0% at that visit; continued medications.
CKD stage 3b due to type 2 diabetes and hypertension: continued lisinopril.
Allergic rhinitis: seasonal symptoms; continue loratadine PRN.

IMPRESSION AND PLAN
1. Diabetes mellitus, type 2: A1c 8.8%, up from 8.0%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Obesity: weight 93.1 kg. Continue lifestyle changes.
3. CKD stage 3b due to type 2 diabetes and hypertension: eGFR 30 today (no prior for comparison). Continue empagliflozin. Recheck BMP and urine albumin-to-creatinine ratio in 3 months.
4. Hypertension: BP 119/89 today. Continue lisinopril 20 mg daily. Home BP log reviewed.
5. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
6. Pneumococcal vaccination up to date. Colorectal cancer screening up to date.

PATlENT EDUCATION
--- Page 2 of 3 --- FU-0077 --- printed 2026-02-09 ---
Encou-
raged 150 minutes of moderate activity week1y.
Reviewed sick-day rules for medications.

Retum to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Physician, DO 2026-01-25 13:18
```

</details>

## 11. FU-0078 — A_N4_type1

**Label: 0 (does not support E11.22).** Type 1 diabetes, so not E11 (type 2).

Check:
- [ ] The note says type 1 diabetes.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0078    Age: 49    Sex: M
Date of service: 2026-02-10    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 3

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
49-year-old man seen today for routine chronic care. Type 1 diabetes since age 17. Brought meter today; morning values 120-145 mg/dL, no lows. No urinary symptoms. No foot ulcers or numbness reported. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Genitourinary: no dysuria, hematuria or change in urine output.
Respiratory: no cough or dyspnea on exertion.
Neurological: no numbness or tingling in the feet; no headaches.
Eyes: no blurred vision; last dilated eye exam 2024.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Cardiovascular: no chest pain, palpitations or orthopnea.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 1 DM
- Chronic kidney disease, stage 4
- Seasonal allergic rhinitis
- Hypothyroidism
- GERD
- Hyperlipidemia

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- insulin pump (lispro) with continuous glucose monitor
- empagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- levothyroxine 75 mcg daily
- omeprazole 20 mg daily
- atorvastatin 40 mg nightly
Med rec done with patient's pill bottles.

ALLERGIES
NKDA.

FAMILY HISTORY
Sister: hypothyroidism.
Brother: hyperlipidemia.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2008; 25 pack-years.
Works part time as a librarian.
Walks 3 times per week, about 20 minutes.

VITALS
BP 142/69 | HR 79 | Temp 98.6 F | Wt 70.3 kg | BMI 25.5 | SpO2 95%

LABS
Date  Test                        Result
2025-07-02  eGFR                        17 mL/min/1.73m2
2026-02-01  eGFR                        18 mL/min/1.73m2
2026-02-01  Creatinine                  3.43 mg/dL
2026-02-01  Hemoglobin A1c              9.0%
2026-02-01  Glucose, fasting            166 mg/dL
2026-02-01  Urine albumin/creatinine    148 mg/g
2026-02-01  Potassium                   4.5 mmol/L
2026-02-01  Sodium                      139 mmol/L
2026-02-01  LDL cholesterol             76 mg/dL
2026-02-01  Hemoglobin                  14.0 g/dL

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

IMPRESSION AND PLAN
1. Type 1 diabetes mellitus: A1c 9.0% on insulin pump. Adjusted overnight basal rate. Continue CGM.
2. Hyperlipidemia: LDL 76 mg/dL. Continue atorvastatin 40 mg.
3. Diabetic kidney disease, CKD stage 4: eGFR 18 today (stable from 17). Continue losartan. Recheck BMP and urine albumin-to-creatinine ratio in 3 months.
4. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
5. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
6. Problem list reviewed: allergic rhinitis.
7. Pneumococcal vaccination up to date. Colorectal cancer screening up to date.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 3 months or sooner as needed.
Total time 40 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Associate, PA-C 2026-02-10 17:24
```

</details>

## 12. FU-0081 — F3_not_face_to_face

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but it is a chart-review e-consult; the patient was not seen (rule R1).

Check:
- [ ] The header and HPI say the patient was not seen.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0081    Age: 69    Sex: M
Date of service: 2026-06-21    Visit type: Interprofessional e-consult (chart review; patient not seen)
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 8

REASON FOR E-CONSULT
Chart review requested for chronic disease management; patient not present.

HISTORY OF PRESENT ILLNESS
Chart reviewed for 69-year-old man; patient not seen or examined for this consult. History of type 2 diabetes diagnosed 9 years ago. Glucose log documented at
--- Page 2 of 3 --- FU-0081 --- printed 2026-07-10 ---
last office visit: fasting 129-142 mg/dL.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease, stage 3b
- Obesity
- GERD
- Hyperlipidemia
- Osteo-
arthritis, bilateral knees

PAST SURGICAL HISTORY
- Cholecystect-
omy (2011)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- atorvastatin 40 mg nightly
- acetaminophen 650 mg as needed
Medication list taken from the chart; not reconciled with the patient.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Brother: hyperlipidemia.
Sister: hypothyroidism.
No fami1y history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2002; 27 pack-years.
Walks 5 times per week, about 20 minutes.
Alcohol: 1 to 2 drinks per week.

VITALS
Last recorded in clinic: BP 122/84, weight 127.5 kg (not measured today).

LABS
Date	Test	Result
2026-03-02    eGFR	42 mL/min/1.73m2
2026-06-15   eGFR      38 mL/min/1.73m2
2026-06-15	Hemoglobin A1c     8.4%
2026-06-15    Glucose, fasting	120 mg/dL
2026-06-15  Urine albumin/creatinine	97 mg/g
2026-06-15    Potassium	4.3 mmol/L
2026-06-15    Sodium         137 mmol/L
2026-06-15	LDL cholesterol    82 mg/dL
2026-06-15  Hemoglobin	11.7 g/dL

EXAM
Not performed; patient not seen for this e-consult.

FR0M LAST OFFICE VISIT (2026-03-04)
(For reference only; not today’s assessment.)
Diabetes mellitus, type 2: A1c 9.8% at that visit; continued medications.
CKD stage 3b secondary to type 2 diabetes: eGFR 42 at that visit; continued losartan.
0besity, BMI 38.4: discussed nutrition and activity goals; referred to dietitian.

E-CONSULT ASSESSMENT AND RECOMMENDATIONS
1. Diabetes mellitus, type 2: A1c 8.4% (improved from 9.8%). Rec-
ommend continuing the current regimen.
2. CKD stage 3b secondary to type 2 diabetes: Latest eGFR 38 (stable from 42), UACR 97 mg/g. Recommend continuing 1osartan and dapagliflozin; repeat BMP and UACR in 3 months.
3. Hyper1ipidemia: stable per chart review; no change recommended.
4. Obesity: stable per chart review; no change recommended.
5. GERD: stab1e per chart review; no change recommended.
6. Knee osteoarthritis: stable per chart review; no change recommended.

Recommendations sent to the primary care team. Total time spent on chart review: 15 minutes.
Electronically signed: Synthetic Practitioner, FNP-C 2026-06-21 16:37
```

</details>

## 13. FU-0082 — C2_t2_on_insulin

**Label: 1 (supports E11.22).** Type 2 diabetes on insulin is still type 2. CKD addressed today.

Check:
- [ ] The note says type 2 and lists insulin.
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0082    Age: 83    Sex: F
Date of service: 2026-04-07    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
Established patient, 83-year-old woman, presenting for chronic disease follow-up. Type 2 diabetes for 4 years; started basal insulin 2 years ago when oral agents were no longer enough. Brought meter today; morning values 126-144 mg/dL, no lows. No urinary symptoms. No foot ulcers or numbness reported. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Genitourinary: no dysuria, hematuria or change in urine output.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Cardiovascular: no chest pain, palpitations or orthopnea.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus, insulin-requiring
- Chronic kidney disease, stage 3a
- Osteoarthritis, bilateral knees
- Obesity
- Seasonal allergic rhinitis
- Hyperlipidemia

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Appendectomy (1988)

MEDICATIONS
- insulin glargine 24 units nightly
- metformin 500 mg twice daily (renally dosed)
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- loratadine 10 mg as needed
- atorvastatin 40 mg nightly
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Brother: hyperlipidemia.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Alcohol: none.
Works part time as a cashier.

VITALS
BP 120/69 | HR 81 | Temp 98.6 F | Wt 93.3 kg | BMI 33.8 | SpO2 97%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2025-08-23  eGFR                        48 mL/min/1.73m2
2026-04-04  eGFR                        51 mL/min/1.73m2
2026-04-04  Creatinine                  1.21 mg/dL
2026-04-04  Hemoglobin A1c              7.2%
2026-04-04  Glucose, fasting            130 mg/dL
2026-04-04  Urine albumin/creatinine    167 mg/g
2026-04-04  Potassium                   5.1 mmol/L
2026-04-04  Sodium                      140 mmol/L
2026-04-04  LDL cholesterol             76 mg/dL
2026-04-04  Hemoglobin                  12.8 g/dL

ASSESSMENT AND PLAN
1. T2DM, insulin-requiring: A1c 7.2% today (up from 6.4%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
3. Diabetic chronic kidney disease, stage 3a: eGFR 51 (stable from 48), albuminuria 167 mg/g. Increased losartan to 100 mg daily. Repeat potassium and creatinine in 2 weeks.
4. Obesity, BMI 33.8: discussed nutrition and activity goals; referred to dietitian.
5. Hyperlipidemia: LDL 76 mg/dL. Continue atorvastatin 40 mg.
6. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
7. Dental visit within the past year. Diabetic foot exam completed today.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Patient verbalized understanding of the plan.

Return to clinic in 3 months or sooner as needed.
Total time 42 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Associate, PA-C 2026-04-07 09:28
```

</details>

## 14. FU-0098 — E2_likely_diabetic

**Label: 1 (supports E11.22).** 'Likely diabetic nephropathy' with a CKD stage; the cause is hedged but not another disease. CKD addressed today.

Check:
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0098    Age: 70    Sex: M
Date of service: 2026-09-15    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
70-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 22 years ago. Has been trying to walk 4 times per week. Glucose readings 129-144 mg/dL fasting. Energy fair. No new complaints today. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Genitourinary: no dysuria, hematuria or change in urine output.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Constitutional: denies fever, chills or unintended weight loss.
Skin: no rashes or non-healing wounds.
Neurological: no numbness or tingling in the feet; no headaches.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- omeprazole 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Penicillin (rash).

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- CKD stage 3b
- Seasonal allergic rhinitis
- Obesity
- GERD

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Cataract extraction, left eye (2022)
- Cholecystectomy (2011)

FAMILY HISTORY
Mother: hypertension.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2002; 7 pack-years.
Alcohol: 1 to 2 drinks per week.
Works part time as a consultant.

VITALS
BP 132/80 | HR 75 | Temp 98.6 F | Wt 88.9 kg | BMI 33.7 | SpO2 97%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2026-09-13  eGFR                        42 mL/min/1.73m2
2026-09-13  Creatinine                  1.47 mg/dL
2026-09-13  Hemoglobin A1c              7.0%
2026-09-13  Glucose, fasting            168 mg/dL
2026-09-13  Urine albumin/creatinine    199 mg/g
2026-09-13  Potassium                   4.5 mmol/L
2026-09-13  Sodium                      136 mmol/L
2026-09-13  LDL cholesterol             66 mg/dL
2026-09-13  Hemoglobin                  12.3 g/dL

ASSESSMENT AND PLAN
1. Diabetes mellitus, type 2: A1c 7.0%, improved from 7.8%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Obesity: weight 88.9 kg. Continue lifestyle changes.
3. Chronic kidney disease stage 3b, most likely due to type 2 diabetes: eGFR 42 (no prior for comparison), albuminuria 199 mg/g. Increased losartan to 100 mg daily. Repeat potassium and creatinine in 2 weeks.
4. GERD: symptoms controlled on omeprazole. Continue.
5. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
6. Dental visit within the past year. Colorectal cancer screening up to date.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Reviewed sick-day rules for medications.

Return to clinic in 4 months or sooner as needed.
Total time 34 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Physician, DO 2026-09-15 17:49
```

</details>

## 15. FU-0114 — G2_see_nephrology

**Label: 0 (does not support E11.22).** Borderline: 'see nephrology note' gives no status or action today.

Check:
- [ ] The plan's CKD line only points to nephrology. Do you agree this is not addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0114    Age: 69    Sex: F
Date of service: 2026-03-28    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 9

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
Established patient, 69-year-old woman, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 11 years ago. States adherence to medications is good. Denies hypoglycemic episodes. No urinary symptoms. No foot ulcers or numbness reported. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Respiratory: no cough or dyspnea on exertion.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2025.
Skin: no rashes or non-healing wounds.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Musculoskeletal: chronic knee stiffness, otherwise negative.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on ora1 agents
- Chronic kidney disease, stage 3a
- Seasonal allergic rhinitis
- Essential hypertension
- Hyperlipidemia

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)
- Appendectomy (1988)
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- loratadine 10 mg as needed
- lisinopril 20 mg daily
- atorvast-
atin 40 mg nightly
Med rec done with patient’s pill bottles.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Mother: hypertension.
Father: coronary artery disease, died age 77.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Lives with alone. Retired teacher.
Alcohol: none.

VITALS
BP 128/76 | HR 75 | Temp 98.1 F | Wt 84.4 kg | BMI 28.2 | SpO2 99%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date	Test	Result
2025-08-19	eGFR         49 mL/min/1.73m2
--- Page 2 of 3 --- FU-0114 --- printed 2026-04-13 ---
2026-03-27	eGFR	48 mL/min/1.73m2
2026-03-27    Creatinine   1.29 mg/dL
2026-03-27	Hemoglobin A1c   8.3%
2026-03-27	Glucose, fasting      148 mg/dL
2026-03-27	Urine albumin/creatinine	85 mg/g
2026-03-27    Potassium     4.8 mmol/L
2026-03-27   Sodium 138 mmol/L
2026-03-27    LDL cholesterol 128 mg/dL
2026-03-27	Hemoglobin     13.5 g/dL

FROM LAST OFFICE VISIT (2025-08-20)
(For reference only; not today’s assessment.)
T2DM: A1c 8.9% at that visit; continued medica-
tions.
Chronic kidney disease stage 3a: eGFR 49 at that visit; continued 1isino-
pril.
Allergic rhinitis: seasonal symptoms; continue loratadine PRN.

IMPRESSION AND PLAN
1. T2DM: A1c 8.3% today (improved from 8.9%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Allergic rhinitis: seasona1 symptoms; continue loratadine PRN.
3. Chronic kidney disease stage 3a: Per nephrology; see their note.
4. A1so on problem list: hypertension, hyperlipidemia.
5. Pneumococcal vaccination up to date. Shingles vaccine series completed.

PATlENT EDUCATION
Reviewed carbohydrate counting handout.
Reviewed sick-day rules for medications.

Retum to clinic in 4 months or sooner as needed.
Total time 41 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-03-28 15:18
```

</details>

## 16. FU-0131 — D_gap90_pos

**Label: 1 (supports E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0131    Age: 84    Sex: F
Date of service: 2026-05-17    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 12

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
Established patient, 84-year-old woman, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 9 years ago. Brought meter today; morning values 109-152 mg/dL, no lows. Appetite stable. Denies nausea or abdominal pain. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Respiratory: no cough or dyspnea on exertion.
Cardiovascular: no chest pain, palpitations or orthopnea.
Eyes: no blurred vision; last dilated eye exam 2025.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Genitourinary: no dysuria, hematuria or change in urine output.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Constitutional: denies fever, chills or unintended weight loss.
Skin: no rashes or non-healing wounds.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD, stage 3b
- Essential hypertension
- GERD
- Obesity

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Colonoscopy with polypectomy (2021)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- lisinopril 20 mg daily
- omeprazole 20 mg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Brother: hyperlipidemia.
Father: coronary artery disease, died age 76.
No family history of kidney disease reported.

SOClAL HISTORY
Former smoker, quit 1999; 15 pack-years.
Lives with daughter. Retired bus driver.
Walks 4 times per week, about 20 minutes.

VITALS
BP 130/84 | HR 69 | Temp 98.2 F | Wt 102.6 kg | BMI 38.3 | SpO2 95%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, non-
tender.
Ext: no edema; feet without lesions.

LABS
Date  Test       Result
2026-02-16	eGFR	34 mL/min/1.73m2
2026-02-16    Creatinine         1.82 mg/dL
2026-05-17 eGFR	41 mL/min/1.73m2
2026-05-17 Creatinine	1.51 mg/dL
2026-05-17    Hemoglobin A1c      7.6%
2026-05-17	Glucose, fasting        125 mg/dL
2026-05-17    Urine albumin/creatinine     60 mg/g
2026-05-17  Potassium         5.1 mmol/L
2026-05-17	Sodium         141 mmol/L
2026-05-17	LDL cholesterol	121 mg/dL
2026-05-17	Hemoglobin 12.9 g/dL

lMPRESSION AND PLAN
1. Diabetes mellitus, type 2: A1c 7.6%, improved from 8.3%. Reviewed diet and activity. Continue medications. Retinal exam due.
--- Page 2 of 3 --- FU-0131 --- printed 2026-05-25 ---
2. CKD stage 3b: eGFR 41 today (up from 34). Continue empagliflozin. Recheck BMP and urine albumin-to-creatinine ratio in 3 months.
3. GERD: symptoms controlled on omeprazole. Continue.
4. Obesity: weight 102.6 kg. Continue lif-
estyle changes.
5. HTN: at goa1 on current regimen. Continue lisinopril.
6. Diabetic foot exam completed today. Co1o-
rectal cancer screening up to date.

PATlENT EDUCATI0N
Discussed hypoglycemia recognition and treatment.
Reviewed sick-day rules for medications.

Retum to clinic in 6 months or sooner as needed.
Total time 28 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Practitioner, FNP-C 2026-05-17 17:55
```

</details>

## 17. FU-0135 — A_N3_labs_only

**Label: 0 (does not support E11.22).** Low eGFR values but no CKD diagnosis by the provider.

Check:
- [ ] No CKD diagnosis anywhere; only lab values.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0135    Age: 72    Sex: F
Date of service: 2026-05-15    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 13

CHIEF COMPLAINT
--- Page 2 of 3 --- FU-0135 --- printed 2026-06-04 ---
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
72-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 10 years ago. Reports checking glucose a few times a week; fasting readings mostly 128-137 mg/dL. Sleeping reasonably well. Mood is good. Mild bilateral knee stiffness in the mornings, unchanged.

REVIEW OF SYSTEMS
Eyes: no blurred vision; last dilated eye exam 2023.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Cardiovascular: no chest pain, palpitations or orthopnea.
Genitourinary: no dysuria, hematuria or change in urine output.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Neurological: no numbness or tingling in the feet; no headaches.
Skin: no rashes or non-healing wounds.

MEDlCATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- loratadine 10 mg as needed
- omeprazole 20 mg daily
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Penicillin (rash).

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Seasonal allergic rhinitis
- GERD
- Essential hypertension
- Obesity

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Appendectomy (1988)
- Cataract extraction, left eye (2022)

FAMILY HISTORY
Father: coronary artery disease, died age 63.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Works part time as a librarian.
Lives with spouse. Retired accountant.

VITALS
BP 144/80 | HR 72 | Temp 98.3 F | Wt 92.0 kg | BMI 31.6 | SpO2 97%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date   Test      Result
2025-11-21 eGFR     48 mL/min/1.73m2
2025-11-21   Creatinine	1.29 mg/dL
2026-05-09   eGFR      46 mL/min/1.73m2
2026-05-09 Hemoglobin A1c      9.4%
2026-05-09 Glucose, fasting      113 mg/dL
2026-05-09    Potassium  5.0 mmol/L
2026-05-09  Sodium	139 mmol/L
2026-05-09   LDL cholesterol	61 mg/dL
2026-05-09	Hemoglobin   14.0 g/dL

ASSESSMENT/PLAN
1. Diabetes mellitus, type 2: A1c 9.4%, improved from 9.7%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
3. Obesity, BMI 31.6: discussed nutrition and activity goals; referred to dietitian.
4. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
5. Also on problem list: hypertension.
6. Shingles vaccine series completed. Diabetic foot exam completed today.

PATIENT EDUCATI0N
Encour-
aged 150 minutes of moderate activity weekly.
Reviewed sick-day rules for medications.

Retum to clinic in 6 months or sooner as needed.
Total time 38 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-05-15 13:12
```

</details>

## 18. FU-0136 — C1_dm_untyped

**Label: 1 (supports E11.22).** Diabetes with no type documented: ICD-10-CM defaults to type 2 (E11). CKD addressed today.

Check:
- [ ] No diabetes type anywhere ('type 1', 'type 2', 'T2DM' absent).
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0136    Age: 61    Sex: M
Date of service: 2026-07-18    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 4

CHIEF COMPLAINT
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
61-year-old man presents for scheduled follow-up. History of
--- Page 2 of 3 --- FU-0136 --- printed 2026-08-01 ---
diabetes diagnosed 8 years ago, managed with metformin. Has been trying to walk 2 times per week. Glucose readings 105-151 mg/dL fasting. Energy fair. No new complaints today. No urinary symptoms. No foot ulcers or numbness reported.

REVIEW OF SYSTEMS
Eyes: no blurred vision; last dilated eye exam 2023.
Constitutional: denies fever, chills or unintended weight loss.
Respiratory: no cough or dyspnea on exertion.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Cardiovascular: no chest pain, palpitations or orthopnea.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Skin: no rashes or non-healing wounds.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- DM, on metformin
- CKD stage 3a
- Hypothyroidism
- Osteoarthritis, bilateral knees
- Seasonal allergic rhinitis

PAST SURGlCAL HISTORY
- Appendectomy (1988)
- Colonoscopy with polypectomy (2021)
- Right knee arthroscopy (2015)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- levothy-
roxine 75 mcg daily
- acetaminophen 650 mg as needed
- loratadine 10 mg as needed
Medicati-
ons reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
No family history of kidney disease reported.
Father: coronary artery disease, died age 68.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Works part time as a librarian.
Lives with spouse. Retired accountant.

VITALS
BP 121/87 | HR 76 | Temp 98.5 F | Wt 76.7 kg | BMI 26.1 | SpO2 98%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date	Test	Result
2026-07-16   eGFR    49 mL/min/1.73m2
2026-07-16	Creatinine        1.26 mg/dL
2026-07-16	Hemoglobin A1c       7.7%
2026-07-16	Glucose, fasting    167 mg/dL
2026-07-16	Urine albumin/creatinine	380 mg/g
2026-07-16	Potassium     4.4 mmol/L
2026-07-16  Sodium	136 mmol/L
2026-07-16   LDL cholesterol   81 mg/dL
2026-07-16   Hemoglobin	12.1 g/dL

FROM LAST OFFICE VISIT (2026-01-19)
(For refere-
nce only; not today's assessment.)
Diabetes mellitus: A1c 6.7% at that visit; continued medications.
Chronic kidney disease stage 3a: continued losartan.
Hypothyroid: clinically euthyroid. Continue current dose.

IMPRESSION AND PLAN
1. Diabetes me1litus: A1c 7.7% (up from 6.7%). Medications unchanged; reinforced carbohydrate counting.
2. OA of knees: continue home exercises and acetaminophen PRN.
3. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
4. Allergic rhinitis: seasona1 symptoms; continue loratadine PRN.
5. Chronic kidney disease stage 3a: Labs reviewed with patient, eGFR 49. Continue dapagliflozin; metformin dose appropriate for current eGFR. Recheck in 3 to 4 months.
6. lnfluenza vaccine given this season. Retinal exam due; referral placed.

PATIENT EDUCATI0N
Patient verba1ized understanding of the plan.
Discussed hypoglycemia recognition and treatment.

Retum to clinic in 4 months or sooner as needed.
Total time 38 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-07-18 15:37
```

</details>

## 19. FU-0143 — G1_reviewed_stable

**Label: 1 (supports E11.22).** Borderline: 'renal function reviewed, stable' counts as a current status.

Check:
- [ ] The plan's CKD line is just 'renal function reviewed, stable'. Do you agree this counts as addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0143    Age: 70    Sex: M
Date of service: 2026-08-24    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 13

CHlEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
Established patient, 70-year-old man,
--- Page 2 of 3 --- FU-0143 --- printed 2026-09-01 ---
presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 21 years ago. Brought meter today; morning values 105-161 mg/dL, no lows. Mild bilateral knee stiffness in the mornings, unchanged. Sleeping reasonably well. Mood is good.

REVIEW 0F SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Genitourinary: no dysuria, hematuria or change in urine output.
Skin: no rashes or non-healing wounds.
Cardiovascular: no chest pain, palpitations or orthopnea.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease
- Obesity
- Hyperlipidemia
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Tonsillectomy (childhood)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- atorvasta-
tin 40 mg nightly
- acetaminophen 650 mg as needed
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
NKDA.

FAMILY HISTORY
No family history of kidney disease reported.
Brother: hyperlipidemia.
Sister: hypothyroidism.

SOCIAL HISTORY
Never smoker.
Alcohol: rare.
Walks 3 times per week, about 20 minutes.

VITALS
BP 138/70 | HR 62 | Temp 98.1 F | Wt 119.9 kg | BMI 35.2 | SpO2 97%

LABS
Date    Test      Result
2026-08-23   eGFR     51 mL/min/1.73m2
2026-08-23	Hemoglobin A1c	8.9%
2026-08-23    Glucose, fasting      137 mg/dL
2026-08-23   Urine albumin/creatinine	254 mg/g
2026-08-23 Potassium        4.8 mmol/L
2026-08-23    Sodium	142 mmol/L
2026-08-23    LDL cholesterol     84 mg/dL
2026-08-23	Hemoglobin        12.3 g/dL

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

FROM LAST OFFICE VISIT (2026-03-25)
(For reference only; not today's assessment.)
Type 2 diabetes mellitus: A1c 7.6% at that visit; continued medications.
Chronic kidney disease: continued losartan.
Obesity: weight 119.9 kg. Continue lifestyle changes.

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus: A1c 8.9% today (up from 7.6%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
3. 0besity, BMI 35.2: discussed nutrition and activity goals; referred to dietitian.
4. Chronic kidney disease: Renal function reviewed; stable.
5. OA of knees: continue home exercises and acetaminophen PRN.
6. Pneumococcal vaccination up to date. lnfluenza vaccine given this season.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Patient verbalized understanding of the plan.

Return to clinic in 6 months or sooner as needed.
Total time 40 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-08-24 09:49
```

</details>

## 20. FU-0147 — D_nodate_pos

**Label: 1 (supports E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0147    Age: 66    Sex: M
Date of service: 2026-07-29    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 3

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
66-year-old man here for a 3-month check-in. History of type 2 diabetes diagnosed 7 years ago. Has been trying to walk 2 times per week. Glucose readings 105-170 mg/dL fasting. Outside lab result brought by patient: eGFR 54 (date not recorded). Mild bilateral knee stiffness in the mornings, unchanged. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Cardiovascular: no chest pain, palpitations or orthopnea.
Neurological: no numbness or tingling in the feet; no headaches.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Genitourinary: no dysuria, hematuria or change in urine output.
Skin: no rashes or non-healing wounds.
Eyes: no blurred vision; last dilated eye exam 2023.

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
- loratadine 10 mg as needed
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Penicillin (rash).

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease stage 3a
- GERD
- Hypothyroidism
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)
- Tonsillectomy (childhood)
- Colonoscopy with polypectomy (2021)

FAMILY HISTORY
Father: coronary artery disease, died age 65.
Sister: hypothyroidism.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2008; 18 pack-years.
Alcohol: 1 to 2 drinks per week.
Works part time as a librarian.

VITALS
BP 137/75 | HR 90 | Temp 97.8 F | Wt 86.4 kg | BMI 28.3 | SpO2 96%

LABS
Date  Test                        Result
2026-07-26  eGFR                        46 mL/min/1.73m2
2026-07-26  Creatinine                  1.34 mg/dL
2026-07-26  Hemoglobin A1c              8.3%
2026-07-26  Glucose, fasting            151 mg/dL
2026-07-26  Urine albumin/creatinine    141 mg/g
2026-07-26  Potassium                   4.4 mmol/L
2026-07-26  Sodium                      143 mmol/L
2026-07-26  LDL cholesterol             88 mg/dL
2026-07-26  Hemoglobin                  13.9 g/dL

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

IMPRESSION AND PLAN
1. T2DM: A1c 8.3% (up from 8.1%). Medications unchanged; reinforced carbohydrate counting.
2. CKD, stage 3a: Latest eGFR 46 (no prior for comparison); potassium acceptable. Continue losartan and empagliflozin. BMP in 3 months.
3. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
4. Also on problem list: allergic rhinitis, hypothyroidism.
5. Diabetic foot exam completed today. Dental visit within the past year.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Associate, PA-C 2026-07-29 16:35
```

</details>

## 21. FU-0162 — F1_non_acceptable_provider

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but the visit is by a nurse or dietitian only, not an acceptable provider (rule R1).

Check:
- [ ] Header and signature show RN or RD.
- [ ] Otherwise the chart would support E11.22.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0162    Age: 49    Sex: F
Date of service: 2026-07-13    Visit type: Nurse visit, diabetes education, in person
Clinician: Synthetic Nurse, RN (Diabetes Education)
Location: Synthetic Primary Care Clinic, Room 5

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
Established patient, 49-year-old woman, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 16 years ago. Notes some difficulty with diet recently; fasting sugars 107-161 mg/dL. Sleeping reasonably well. Mood is good. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Respiratory: no cough or dyspnea on exertion.
Eyes: no blurred vision; last dilated eye exam 2025.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Genitourinary: no dysuria, hematuria or change in urine output.
Cardiovascular: no chest pain, palpitations or orthopnea.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Neurological: no numbness or tingling in the feet; no headaches.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease stage 3a
- Seasonal allergic rhinitis
- GERD
- Hypothyroidism
- Hyperlipidemia

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Cataract extraction, left eye (2022)
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
- atorvastatin 40 mg nightly
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Father: coronary artery disease, died age 63.
Sister: hypothyroidism.

SOCIAL HISTORY
Never smoker.
Lives with spouse. Retired machinist.
Walks 3 times per week, about 20 minutes.

VITALS
BP 134/74 | HR 64 | Temp 97.7 F | Wt 74.6 kg | BMI 24.6 | SpO2 99%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2025-12-16  eGFR                        58 mL/min/1.73m2
2025-12-16  Creatinine                  1.06 mg/dL
2026-07-10  eGFR                        56 mL/min/1.73m2
2026-07-10  Creatinine                  1.1 mg/dL
2026-07-10  Hemoglobin A1c              7.2%
2026-07-10  Glucose, fasting            143 mg/dL
2026-07-10  Urine albumin/creatinine    217 mg/g
2026-07-10  Potassium                   4.8 mmol/L
2026-07-10  Sodium                      136 mmol/L
2026-07-10  LDL cholesterol             65 mg/dL
2026-07-10  Hemoglobin                  14.2 g/dL

ASSESSMENT/PLAN
1. Type 2 diabetes mellitus: A1c 7.2% (improved from 7.5%). Reviewed meal plan and carbohydrate counting; medications per provider.
2. Diabetic kidney disease, CKD stage 3a: eGFR 56 reviewed (stable from 58); reinforced low-sodium diet and medication adherence. Provider to review labs.
3. Hypothyroidism: managed by primary care provider.
4. GERD: managed by primary care provider.
5. Also on problem list: allergic rhinitis, hyperlipidemia.
6. Pneumococcal vaccination up to date. Retinal exam due; referral placed.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Reviewed sick-day rules for medications.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Nurse, RN 2026-07-13 11:11
```

</details>

## 22. FU-0166 — B4_per_last_visit

**Label: 0 (does not support E11.22).** CKD line says only 'per last visit / unchanged from <month>'; today's labs are not mentioned.

Check:
- [ ] No eGFR from the last 30 days anywhere.
- [ ] The CKD line has no current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0166    Age: 48    Sex: F
Date of service: 2026-07-02    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 2

CHIEF COMPLAINT
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
48-year-old woman seen today for routine chronic care. History of type 2 diabetes diagnosed 7 years ago. Reports checking glucose daily; fasting readings mostly 118-161 mg/dL. Energy fair. No new comp-
laints today. No polyuria or polydipsia. No visual changes.

REVIEW 0F SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Cardiovascular: no chest pain, palpi-
tations or orthopnea.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Genitourinary: no dysuria, hematuria or change in urine output.
Const-
itutional: denies fever, chills or unintended weight loss.
Respiratory: no cough or dyspnea on exertion.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Skin: no rashes or non-healing wounds.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease, stage 3a
- GERD
- Obesity
- Hypothyroidism

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Appendectomy (1988)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
Medications reviewed with patient and pharmacy list; list above is current.
--- Page 2 of 3 --- FU-0166 --- printed 2026-07-06 ---

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
No family history of kidney disease reported.
Mother: hypertension.
Sister: hypothyroidism.

SOCIAL HISTORY
Never smoker.
Alcohol: rare.
Works part time as a consultant.

VITALS
BP 136/74 | HR 67 | Temp 97.7 F | Wt 87.9 kg | BMI 35.1 | SpO2 97%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date	Test       Result
2025-08-07	eGFR    51 mL/min/1.73m2
2025-08-07	Creatinine   1.21 mg/dL
2026-02-02  eGFR     55 mL/min/1.73m2
2026-07-02	Hemog1obin A1c	6.9%
2026-07-02 Glucose, fasting      120 mg/dL
2026-07-02 LDL cholesterol  128 mg/dL
2026-07-02	Hemoglobin      14.1 g/dL

ASSESSMENT/PLAN
(Assessment copied from note dated 2026-02-06 and updated where noted.)
1. Diabetes mellitus, type 2: A1c 6.9%, up from 5.6%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. CKD stage 3a secondary to type 2 diabetes: Unchanged from 02/2026; per last visit.
3. Hypothyroidism: TSH within range. Continue 1evothyroxine 75 mcg.
4. Obesity: weight 87.9 kg. Continue lifestyle changes.
5. GERD: symptoms controlled on omeprazole. Continue.
6. Retina1 exam due; referral placed. Diabetic foot exam completed today.

PATlENT EDUCATI0N
Reviewed carbohydrate counting handout.
Patient verbalized understanding of the plan.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-07-02 14:43
```

</details>

## 23. FU-0177 — C4_secondary_dm

**Label: 0 (does not support E11.22).** Secondary diabetes (steroid-induced or after pancreatectomy) is not type 2 (rule R3).

Check:
- [ ] The diabetes is described as steroid-induced or due to pancreatectomy.
- [ ] Nowhere says type 2.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0177    Age: 61    Sex: M
Date of service: 2026-05-24    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 9

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
61-year-old man seen today for routine chronic care. Diabetes since total pancreatectomy for chronic pancreatitis in 2018. Reports checking glucose daily; fasting readings mostly 120-162 mg/dL. Appetite stable. Denies nausea or abdominal pain. No urinary symptoms. No foot ulcers or numbness reported.

REVlEW OF SYSTEMS
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Cardiovascular: no chest pain, palpitations or orthopnea.
Constitutional: denies fever, chills or unintended weight loss.
Psychi-
atric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus due to total pancreatectomy
- CKD, stage 3b
- Hypothyroidism
- GERD
- Hyperlipidemia

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Total pancreatectomy (see HPI)

MEDICATIONS
- insulin glargine 14 units nightly
- insulin aspart sliding scale with meals
- pancrelipase with meals
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- levothyroxine 75 mcg daily
- omeprazole 20 mg daily
- atorvastatin 40 mg nightly
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Brother: hyperlipidemia.
No family history of kidney disease reported.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 2003; 30 pack-years.
Lives with alone. Retired bus driver.
Walks 3 times per week, about 20 minutes.

VITALS
BP 136/72 | HR 85 | Temp 97.8 F | Wt 83.8 kg | BMI 24.9 | SpO2 98%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test    Result
2025-11-14    eGFR    42 mL/min/1.73m2
2026-05-19	eGFR     33 mL/min/1.73m2
2026-05-19	Hemoglobin A1c	9.0%
2026-05-19	Glucose, fasting     177 mg/dL
2026-05-19  Urine albumin/creatinine	100 mg/g
2026-05-19   Potassium  4.5 mmol/L
2026-05-19  Sodium     136 mmol/L
2026-05-19   LDL cholesterol      112 mg/dL
2026-05-19    Hemoglobin    13.6 g/dL

ASSESSMENT AND PLAN
1. Diabetes mellitus due to total pancreatectomy: A1c 9.0% (up from 8.4%). Continue current regimen; reviewed glucose log.
2.
--- Page 2 of 3 --- FU-0177 --- printed 2026-06-02 ---
Diabetic chronic kidney disease, stage 3b: eGFR 33, UACR 100 mg/g. 0n dapagliflozin and losartan; counseled on avoiding nephrotoxins. Repeat labs in 3 months.
3. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
4. Problem list reviewed: hypothyroidism, hyperlipidemia.
5. Colorectal cancer screening up to date. Diabetic foot exam completed today.

PATIENT EDUCATI0N
Encouraged 150 minutes of moderate activity weekly.
Reviewed carbohydrate counting handout.

Retum to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Physician, DO 2026-05-24 08:38
```

</details>

## 24. FU-0185 — E3_link_in_prior_visit

**Label: 1 (supports E11.22).** The diabetic cause appears only in a dated prior-visit section; today's plan addresses CKD without another cause.

Check:
- [ ] The prior-visit section links CKD to diabetes; today's plan does not name another cause.
- [ ] Today's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0185    Age: 68    Sex: F
Date of service: 2026-06-18    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 6

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
68-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 20 years ago. Reports checking glucose daily; fasting readings mostly 126-153 mg/dL. Sleeping reasonably well. Mood is good. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Genitourinary: no dysuria, hematuria or change in urine output.
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Eyes: no blurred vision; last dilated eye exam 2023.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.
--- Page 2 of 3 --- FU-0185 --- printed 2026-07-03 ---

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- CKD, stage 3a
- Osteoarthritis, bilateral knees
- Essential hypertension

PAST SURGlCAL HISTORY
- Cholecystectomy (2011)
- Colonoscopy with polypectomy (2021)
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- acetaminophen 650 mg as needed
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
NKDA.

FAMILY HISTORY
No family history of kidney disease reported.
Father: coronary artery disease, died age 62.

SOCIAL HISTORY
Former smoker, quit 2014; 13 pack-years.
Walks 3 times per week, about 20 minutes.
Lives with spouse. Retired accountant.

VITALS
BP 124/92 | HR 92 | Temp 98.0 F | Wt 70.9 kg | BMI 26.1 | Sp02 99%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date    Test	Result
2026-06-17 eGFR	46 mL/min/1.73m2
2026-06-17   Hemoglobin A1c	8.4%
2026-06-17 Glucose, fasting	104 mg/dL
2026-06-17	Urine albumin/creatinine	39 mg/g
2026-06-17	Potassium	4.7 mmol/L
2026-06-17	Sodium 142 mmol/L
2026-06-17	LDL cholesterol	63 mg/dL
2026-06-17	Hemoglobin        12.3 g/dL

PRIOR VISIT SUMMARY (2026-02-06)
(For reference only; not today’s assessment.)
Type 2 diabetes mellitus: A1c 8.1% at that visit; continued medications.
Chronic kidney disease stage 3a due to type 2 diabetes: continued lisinopril.
Knee osteoarthritis: stable. Acetamin-
ophen as needed; avoid NSAIDs.

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus: A1c 8.4%, up from 8.1%. Reviewed diet and activity. Continue medications. Retina1 exam due.
2. OA of knees: continue home exercises and acetaminophen PRN.
3. Chronic kidney disease, stage 3a: eGFR 46, UACR 39 mg/g. On dapagliflozin and lisinopril; counse-
led on avoiding nephrotoxins. Repeat labs in 3 months.
4. HTN: at goal on current regimen. Continue lisinopril.
5. Retinal exam due; referral placed. lnfluenza vaccine given this season.

PATIENT EDUCATI0N
Reviewed carbohydrate counting handout.
Encouraged 150 minutes of moderate activity weekly.

Retum to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-06-18 14:02
```

</details>

## 25. FU-0191 — B3_copy_plus_new

**Label: 1 (supports E11.22).** Copied (stale) CKD line, followed by a new line from today with today's eGFR.

Check:
- [ ] The CKD item has an 'Update today' or 'Addendum' sentence with today's eGFR.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0191    Age: 61    Sex: F
Date of service: 2026-08-10    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 4

CHIEF COMPLAINT
Follow-up visit; medication refills.

HISTORY OF PRESENT ILLNESS
61-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 14 years ago. Brought meter today; morning values 108-163 mg/dL, no lows. Denies chest pain, shortness of breath or leg swelling. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Skin: no rashes or non-healing wounds.
Eyes: no blurred vision; last dilated eye exam 2024.
Neurological: no numbness or tingling in the feet; no headaches.
Respiratory: no cough or dyspnea on exertion.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Constitutional: denies fever, chills or unintended weight loss.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease stage 3a
- Osteoarthritis, bilateral knees
- Obesity
- Hyperlipidemia

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- atorvastatin 40 mg nightly
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
NKDA.

FAMILY HISTORY
No family history of kidney disease reported.
Father: coronary artery disease, died age 63.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 1995; 17 pack-years.
Lives with alone. Retired machinist.
Walks 3 times per week, about 20 minutes.

VITALS
BP 122/80 | HR 86 | Temp 97.7 F | Wt 99.6 kg | BMI 35.2 | SpO2 99%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2026-01-14  eGFR                        58 mL/min/1.73m2
2026-01-14  Creatinine                  1.06 mg/dL
2026-08-10  eGFR                        49 mL/min/1.73m2
2026-08-10  Hemoglobin A1c              7.4%
2026-08-10  Glucose, fasting            157 mg/dL
2026-08-10  Urine albumin/creatinine    102 mg/g
2026-08-10  Potassium                   3.9 mmol/L
2026-08-10  Sodium                      141 mmol/L
2026-08-10  LDL cholesterol             117 mg/dL
2026-08-10  Hemoglobin                  13.3 g/dL

ASSESSMENT AND PLAN
(A/P carried forward from 2026-05-16; reviewed and unchanged.)
1. Type 2 diabetes mellitus: A1c 7.4%, improved from 8.7%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Diabetic kidney disease, CKD stage 3a: Last eGFR 58 on 2026-01-14. Continue current renal regimen. Labs before next visit. Addendum 2026-08-10: eGFR 49 today, down from 58. No change to losartan.
3. Obesity, BMI 35.2: discussed nutrition and activity goals; referred to dietitian.
4. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
5. OA of knees: continue home exercises and acetaminophen PRN.
6. Shingles vaccine series completed. Diabetic foot exam completed today.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 4 months or sooner as needed.
Total time 26 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-08-10 09:49
```

</details>

## 26. FU-0203 — D_gap89_neg

**Label: 0 (does not support E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0203    Age: 79    Sex: F
Date of service: 2026-01-23    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 9

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
79-year-old woman here for a 4-month check-in. History of type 2 diabetes diagnosed 9 years ago. Reports checking glucose twice daily; fasting readings mostly 122-138 mg/dL. Appetite stable. Denies nausea or abdominal pain. Mild bilateral knee stiffness in the mornings, unchanged.

REVIEW OF SYSTEMS
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Respiratory: no cough or dyspnea on exertion.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Neurological: no numbness or tingling in the feet; no headaches.
Eyes: no blurred vision; last dilated eye exam 2024.
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease stage 3b
- Hypothyroidism
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Cholecystectomy (2011)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- losartan 50 mg daily
- levothyroxine 75 mcg daily
- acetaminophen 650 mg as needed
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
NKDA.

FAMILY HISTORY
Mother: hypertension.
Father: coronary artery disease, died age 78.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2014; 28 pack-years.
Walks 5 times per week, about 20 minutes.
Lives with spouse. Retired bus driver.

VITALS
BP 126/79 | HR 85 | Temp 98.0 F | Wt 77.7 kg | BMI 26.0 | SpO2 99%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2025-10-22  eGFR                        32 mL/min/1.73m2
2025-10-22  Creatinine                  1.93 mg/dL
2026-01-19  eGFR                        41 mL/min/1.73m2
2026-01-19  Creatinine                  1.51 mg/dL
2026-01-19  Hemoglobin A1c              8.4%
2026-01-19  Glucose, fasting            157 mg/dL
2026-01-19  Urine albumin/creatinine    49 mg/g
2026-01-19  Potassium                   4.2 mmol/L
2026-01-19  Sodium                      142 mmol/L
2026-01-19  LDL cholesterol             86 mg/dL
2026-01-19  Hemoglobin                  11.9 g/dL

IMPRESSION AND PLAN
1. T2DM: A1c 8.4% today (up from 8.2%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Also on problem list: knee osteoarthritis, hypothyroidism.
3. Shingles vaccine series completed. Influenza vaccine given this season.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Reviewed carbohydrate counting handout.

Return to clinic in 6 months or sooner as needed.
Total time 39 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-01-23 16:19
```

</details>

## 27. FU-0216 — C5_history_of_ckd

**Label: 1 (supports E11.22).** 'History of CKD' in the HPI, and the plan gives CKD a current status and action.

Check:
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0216    Age: 76    Sex: F
Date of service: 2026-03-03    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 14

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
76-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 20 years ago. Home glucose log reviewed, fasting values 128-145 mg/dL with occasional post-meal readings above 200. History of CKD, diagnosed 2018, followed in this clinic. No polyuria or polydipsia. No visual changes. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Constitutional: denies fever, chills or unintended weight loss.
Cardiovascular: no chest pain, palpitations or orthopnea.
Skin: no rashes or non-healing wounds.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Genitourinary: no dysuria, hematuria or change in urine output.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease, stage 3a
- Essential hypertension
- Obesity
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Right knee arthroscopy (2015)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- lisinopril 20 mg daily
- loratadine 10 mg as needed
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Sister: hypothyroidism.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 1999; 18 pack-years.
Alcohol: none.
Works part time as a librarian.

VITALS
BP 121/90 | HR 92 | Temp 98.3 F | Wt 89.5 kg | BMI 36.0 | SpO2 98%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2026-03-02  eGFR                        45 mL/min/1.73m2
2026-03-02  Hemoglobin A1c              8.0%
2026-03-02  Glucose, fasting            136 mg/dL
2026-03-02  Urine albumin/creatinine    321 mg/g
2026-03-02  Potassium                   4.3 mmol/L
2026-03-02  Sodium                      142 mmol/L
2026-03-02  LDL cholesterol             63 mg/dL
2026-03-02  Hemoglobin                  12.2 g/dL

IMPRESSION AND PLAN
1. Type 2 diabetes mellitus: A1c 8.0%, up from 7.4%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. CKD, stage 3a: eGFR 45, UACR 321 mg/g. On dapagliflozin and lisinopril; counseled on avoiding nephrotoxins. Repeat labs in 3 months.
3. Essential hypertension: BP 121/90. Reinforced low-sodium diet; continue lisinopril 20 mg.
4. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
5. Obesity: weight 89.5 kg. Continue lifestyle changes.
6. Diabetic foot exam completed today. Pneumococcal vaccination up to date.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Discussed hypoglycemia recognition and treatment.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Associate, PA-C 2026-03-03 10:12
```

</details>

## 28. FU-0219 — A_P4_link_in_hpi

**Label: 1 (supports E11.22).** CKD addressed today; the diabetic cause is stated only in the HPI.

Check:
- [ ] The HPI attributes the kidney disease to diabetes.
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0219    Age: 79    Sex: M
Date of service: 2026-06-27    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 13

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
Patient is a 79-year-old man returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 17 years ago. States adherence to medications is good. Denies hypoglycemic episodes. Nephrology evaluated his kidney disease in 2020 and attributed it to longstanding diabetes. Mild bilateral knee stiffness in the mornings, unchanged. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Respiratory: no cough or dyspnea on exertion.
Genitourinary: no dysuria, hematuria or change in urine output.
Skin: no rashes or non-healing wounds.
Eyes: no blurred vision; last dilated eye exam 2024.
Cardiovascular: no chest pain, palpitations or orthopnea.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Constitutional: denies fever, chills or unintended weight loss.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease, stage 3b
- Obesity
- Hyperlipidemia
- GERD

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- atorvastatin 40 mg nightly
- omeprazole 20 mg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Mother: hypertension.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 2014; 29 pack-years.
Alcohol: 1 to 2 drinks per week.
Lives with spouse. Retired bus driver.

VITALS
BP 128/84 | HR 68 | Temp 98.4 F | Wt 84.9 kg | BMI 32.0 | SpO2 96%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2025-12-16  eGFR                        32 mL/min/1.73m2
2025-12-16  Creatinine                  1.93 mg/dL
2026-06-18  eGFR                        35 mL/min/1.73m2
2026-06-18  Creatinine                  1.76 mg/dL
2026-06-18  Hemoglobin A1c              8.3%
2026-06-18  Glucose, fasting            121 mg/dL
2026-06-18  Urine albumin/creatinine    180 mg/g
2026-06-18  Potassium                   3.9 mmol/L
2026-06-18  Sodium                      140 mmol/L
2026-06-18  LDL cholesterol             117 mg/dL
2026-06-18  Hemoglobin                  11.8 g/dL

INTERVAL NOTE - PREVIOUS VISIT 2025-12-17
(For reference only; not today's assessment.)
Type 2 diabetes mellitus: A1c 9.3% at that visit; continued medications.
Chronic kidney disease, stage 3b: eGFR 32 at that visit; continued losartan.
Obesity: weight 84.9 kg. Continue lifestyle changes.

IMPRESSION AND PLAN
1. Type 2 diabetes mellitus: A1c 8.3%, improved from 9.3%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hyperlipidemia: LDL 117 mg/dL. Continue atorvastatin 40 mg.
3. GERD: symptoms controlled on omeprazole. Continue.
4. Obesity: weight 84.9 kg. Continue lifestyle changes.
5. Chronic kidney disease, stage 3b: Labs reviewed with patient, eGFR 35. Continue dapagliflozin; metformin dose appropriate for current eGFR. Recheck in 3 to 4 months.
6. Diabetic foot exam completed today. Shingles vaccine series completed.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Reviewed carbohydrate counting handout.

Return to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-06-27 16:23
```

</details>

## 29. FU-0240 — G4_list_entry

**Label: 0 (does not support E11.22).** Borderline: CKD only in a 'chronic conditions reviewed' list, no status or action.

Check:
- [ ] Do you agree this is not addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0240    Age: 81    Sex: M
Date of service: 2026-09-07    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
Patient is a 81-year-old man returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 14 years ago. Home glucose log reviewed, fasting values 122-135 mg/dL with occasional post-meal readings above 200. No polyuria or polydipsia. No visual changes. No urinary symptoms. No foot ulcers or numbness reported.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.
Neurological: no numbness or tingling in the feet; no headaches.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Constitutional: denies fever, chills or unintended weight loss.
Eyes: no blurred vision; last dilated eye exam 2023.
Genitourinary: no dysuria, hematuria or change in urine output.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- CKD, stage 3a
- Seasonal allergic rhinitis
- Hyperlipidemia
- Obesity
- Essential hypertension

PAST SURGICAL HISTORY
- Cholecystectomy (2011)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- loratadine 10 mg as needed
- atorvastatin 40 mg nightly
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Mother: hypertension.
Brother: hyperlipidemia.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2007; 18 pack-years.
Lives with alone. Retired accountant.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 126/73 | HR 83 | Temp 98.3 F | Wt 108.7 kg | BMI 32.0 | SpO2 98%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2026-05-20  eGFR                        48 mL/min/1.73m2
2026-05-20  Creatinine                  1.29 mg/dL
2026-08-28  eGFR                        52 mL/min/1.73m2
2026-08-28  Hemoglobin A1c              6.8%
2026-08-28  Glucose, fasting            165 mg/dL
2026-08-28  Urine albumin/creatinine    260 mg/g
2026-08-28  Potassium                   4.4 mmol/L
2026-08-28  Sodium                      143 mmol/L
2026-08-28  LDL cholesterol             96 mg/dL
2026-08-28  Hemoglobin                  13.4 g/dL

ASSESSMENT AND PLAN
1. Diabetes mellitus, type 2: A1c 6.8% (up from 5.6%). Medications unchanged; reinforced carbohydrate counting.
2. Obesity, BMI 32.0: discussed nutrition and activity goals; referred to dietitian.
3. Hypertension: BP 126/73 today. Continue lisinopril 20 mg daily. Home BP log reviewed.
4. Chronic conditions reviewed: hyperlipidemia, allergic rhinitis, CKD 3a.
5. Dental visit within the past year. Colorectal cancer screening up to date.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Reviewed carbohydrate counting handout.

Return to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-09-07 11:38
```

</details>

## 30. FU-0242 — B3_copy_plus_new

**Label: 1 (supports E11.22).** Copied (stale) CKD line, followed by a new line from today with today's eGFR.

Check:
- [ ] The CKD item has an 'Update today' or 'Addendum' sentence with today's eGFR.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0242    Age: 75    Sex: M
Date of service: 2026-03-17    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
Established patient, 75-year-old man, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 13 years ago. Home glucose log reviewed, fasting values 113-171 mg/dL with occasional post-meal readings above 200. No polyuria or polydipsia. No visual changes. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Eyes: no blurred vision; last dilated eye exam 2023.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Skin: no rashes or non-healing wounds.
Genitourinary: no dysuria, hematuria or change in urine output.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- CKD, stage 3b
- Hyperlipidemia
- Obesity
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- losartan 50 mg daily
- atorvastatin 40 mg nightly
- loratadine 10 mg as needed
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Mother: hypertension.
Father: coronary artery disease, died age 78.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 2013; 30 pack-years.
Walks 4 times per week, about 20 minutes.
Works part time as a consultant.

VITALS
BP 126/68 | HR 65 | Temp 97.8 F | Wt 102.5 kg | BMI 34.0 | SpO2 94%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2025-11-05  eGFR                        38 mL/min/1.73m2
2026-03-17  eGFR                        43 mL/min/1.73m2
2026-03-17  Hemoglobin A1c              9.3%
2026-03-17  Glucose, fasting            185 mg/dL
2026-03-17  Urine albumin/creatinine    46 mg/g
2026-03-17  Potassium                   4.8 mmol/L
2026-03-17  Sodium                      138 mmol/L
2026-03-17  LDL cholesterol             87 mg/dL
2026-03-17  Hemoglobin                  14.5 g/dL

IMPRESSION AND PLAN
(Plan unchanged from visit of 2025-11-02.)
1. T2DM: A1c 9.3%, improved from 10.5%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. CKD stage 3b secondary to type 2 diabetes: Last eGFR 38 on 2025-11-05. Continue current renal regimen. Labs before next visit. Addendum 2026-03-17: eGFR 43 today, stable from 38. No change to losartan.
3. Obesity: weight 102.5 kg. Continue lifestyle changes.
4. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
5. Hyperlipidemia: LDL 87 mg/dL. Continue atorvastatin 40 mg.
6. Colorectal cancer screening up to date. Diabetic foot exam completed today.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Reviewed carbohydrate counting handout.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-03-17 17:15
```

</details>

## 31. FU-0246 — F1_non_acceptable_provider

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but the visit is by a nurse or dietitian only, not an acceptable provider (rule R1).

Check:
- [ ] Header and signature show RN or RD.
- [ ] Otherwise the chart would support E11.22.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0246    Age: 57    Sex: M
Date of service: 2026-04-03    Visit type: Medical nutrition therapy visit, in person
Clinician: Synthetic Dietitian, RD (Medical Nutrition Therapy)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
57-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 13 years ago. States adherence to medications is good. Denies hypoglycemic episodes. Energy fair. No new complaints today. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Musculoskeletal: chronic knee stiffness, otherwise negative.
Genitou-
rinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2025.
Respiratory: no cough or dyspnea on exertion.
Constitutional: denies fever, chills or unintended weight loss.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.

PAST MEDlCAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
--- Page 2 of 3 --- FU-0246 --- printed 2026-04-04 ---
- CKD, stage 3b
- Obesity
- Seasonal allergic rhinitis
- Hyperlipidemia

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- atorvastatin 40 mg nightly
Med rec done with patient’s pill bottles.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Sister: hypothyroidism.
Mother: hypertension.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2004; 8 pack-years.
Lives with spouse. Retired machinist.
Walks 5 times per week, about 20 minutes.

VITALS
BP 147/82 | HR 82 | Temp 98.1 F | Wt 110.3 kg | BMI 37.0 | SpO2 97%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test   Result
2026-03-31	eGFR         31 mL/min/1.73m2
2026-03-31	Creatinine    1.99 mg/dL
2026-03-31	Hemoglobin A1c	6.6%
2026-03-31 Glucose, fasting  118 mg/dL
2026-03-31    Urine albumin/creatinine	177 mg/g
2026-03-31	Potassium     5.1 mmol/L
2026-03-31   Sodium         139 mmol/L
2026-03-31	LDL cholesterol  73 mg/dL
2026-03-31	Hemoglobin	11.6 g/dL

ASSESSMENT/PLAN
1. T2DM: A1c 6.6% (improved from 7.9%). Reviewed meal plan and carbohydrate counting; medications per provider.
2. Chronic kidney disease stage 3b: Kidney labs reviewed with patient: eGFR 31, UACR 177 mg/g. Reviewed renal diet handout; continue empagliflozin as prescribed.
3. Hyperlipidemia: managed by primary care provider.
4. 0besity: managed by primary care provider.
5. Allergic rhinitis: managed by primary care provider.
6. Pneumococca1 vaccination up to date. Diabetic foot exam completed today.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Discussed hypoglycemia recognition and treatment.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Dietitian, RD 2026-04-03 13:16
```

</details>

## 32. FU-0251 — B5_interval_labs

**Label: 1 (supports E11.22).** Today's renal labs are reviewed in the interval history, and the copied plan line refers to them.

Check:
- [ ] The HPI reviews today's labs (eGFR) with the patient.
- [ ] The CKD plan line points to today's results and an action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0251    Age: 72    Sex: F
Date of service: 2026-07-31    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 6

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
72-year-old woman here for a 3-month check-in. History of type 2 diabetes diagnosed 21 years ago. States adherence to medications is good. Denies hypoglycemic episodes. Labs drawn 2026-07-31 were reviewed with the patient today: eGFR 21, UACR 277 mg/g. No urinary symptoms. No foot ulcers or numbness reported. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Eyes: no blurred vision; last dilated eye exam 2025.
Constitutional: denies fever, chills or unintended weight loss.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Respiratory: no cough or dyspnea on exertion.

MEDICATIONS
- insulin glargine 18 units nightly
- empagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
Med rec done with patient's pill bottles.

ALLERGIES
No known drug allergies.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease stage 4
- Seasonal allergic rhinitis
- Obesity

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)

FAMILY HISTORY
Father: coronary artery disease, died age 70.
Sister: hypothyroidism.
Mother: hypertension.

SOCIAL HISTORY
Never smoker.
Lives with spouse. Retired machinist.
Walks 5 times per week, about 20 minutes.

VITALS
BP 125/82 | HR 75 | Temp 97.9 F | Wt 80.3 kg | BMI 32.3 | SpO2 98%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2026-03-10  eGFR                        22 mL/min/1.73m2
2026-03-10  Creatinine                  2.81 mg/dL
2026-07-31  eGFR                        21 mL/min/1.73m2
2026-07-31  Hemoglobin A1c              6.7%
2026-07-31  Glucose, fasting            149 mg/dL
2026-07-31  Urine albumin/creatinine    277 mg/g
2026-07-31  Potassium                   4.5 mmol/L
2026-07-31  Sodium                      137 mmol/L
2026-07-31  LDL cholesterol             98 mg/dL
2026-07-31  Hemoglobin                  14.7 g/dL

ASSESSMENT AND PLAN
(Plan unchanged from visit of 2026-03-31.)
1. Diabetes mellitus, type 2: A1c 6.7% (improved from 7.8%). Medications unchanged; reinforced carbohydrate counting.
2. CKD stage 4: Today's results as above, at baseline; continue losartan and empagliflozin.
3. Obesity, BMI 32.3: discussed nutrition and activity goals; referred to dietitian.
4. Also on problem list: allergic rhinitis.
5. Shingles vaccine series completed. Influenza vaccine given this season.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Reviewed sick-day rules for medications.

Return to clinic in 4 months or sooner as needed.
Total time 44 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Physician, DO 2026-07-31 10:34
```

</details>

## 33. FU-0259 — B2_copy_stale

**Label: 0 (does not support E11.22).** Plan copied from a prior visit; the CKD line refers only to an old eGFR and the old plan; nothing current.

Check:
- [ ] The CKD line's eGFR is dated months before the visit.
- [ ] No eGFR from the last 30 days anywhere in the note.
- [ ] No other CKD status or action today.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0259    Age: 82    Sex: F
Date of service: 2026-01-18    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 5

CHIEF COMPLAINT
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
Established patient, 82-year-old woman, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 18 years ago. Reports checking glucose daily; fasting readings mostly 118-137 mg/dL. Denies chest pain, shortness of breath or leg swelling. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Neurological: no numbness or tingling in the feet; no headaches.
Genitourinary: no dysuria, hematuria or change in urine output.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Skin: no rashes or non-healing wounds.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Eyes: no blurred vision; last dilated eye exam 2025.
Cardiovascular: no chest pain, palpitations or orthopnea.
Respiratory: no cough or dyspnea on exertion.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease, stage 3a
- Essential hypertension
- Hypothyroidism
- GERD
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Tonsillectomy (childhood)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- lisinopril 20 mg daily
- levothyroxine 75 mcg daily
- omeprazole 20 mg daily
- acetaminophen 650 mg as needed
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Brother: hyperlipidemia.
Sister: hypothyroidism.
Father: coronary artery disease, died age 66.

SOCIAL HISTORY
Former smoker, quit 2002; 26 pack-years.
Works part time as a consultant.
Walks 3 times per week, about 20 minutes.

VITALS
BP 139/84 | HR 69 | Temp 98.7 F | Wt 72.0 kg | BMI 29.4 | SpO2 94%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2025-04-05  eGFR                        49 mL/min/1.73m2
2025-09-05  eGFR                        54 mL/min/1.73m2
2026-01-15  Hemoglobin A1c              7.7%
2026-01-15  Glucose, fasting            143 mg/dL
2026-01-15  LDL cholesterol             60 mg/dL
2026-01-15  Hemoglobin                  14.4 g/dL

ASSESSMENT/PLAN
(Plan unchanged from visit of 2025-09-05.)
1. Type 2 diabetes mellitus: A1c 7.7%, improved from 8.4%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
3. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
4. GERD: symptoms controlled on omeprazole. Continue.
5. Chronic kidney disease, stage 3a: eGFR 54 (2025-09-05), stable at that time. Continue regimen as previously outlined.
6. Essential hypertension: BP 139/84. Reinforced low-sodium diet; continue lisinopril 20 mg.
7. Influenza vaccine given this season. Diabetic foot exam completed today.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Associate, PA-C 2026-01-18 13:51
```

</details>

## 34. FU-0262 — C6_ckd_ruled_out

**Label: 0 (does not support E11.22).** CKD removed from the problem list: repeat testing shows normal kidney function.

Check:
- [ ] The plan says the patient does not have CKD / CKD ruled out.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0262    Age: 59    Sex: F
Date of service: 2026-04-13    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
Follow-up visit; medication refills.

HISTORY OF PRESENT ILLNESS
59-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 11 years ago. Has been trying to walk 3 times per week. Glucose readings 125-144 mg/dL fasting. Appetite stable. Denies nausea or abdominal pain. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Cardiovascular: no chest pain, palpitations or orthopnea.
Eyes: no blurred vision; last dilated eye exam 2024.
Genitourinary: no dysuria, hematuria or change in urine output.
Musculoskeletal: chronic knee stiffness, otherwise negative.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease (entered 2024) - see assessment
- Hypothyroidism
- GERD
- Seasonal allergic rhinitis
- Essential hypertension

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- levothyroxine 75 mcg daily
- omeprazole 20 mg daily
- loratadine 10 mg as needed
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Brother: hyperlipidemia.
Sister: hypothyroidism.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Alcohol: 1 to 2 drinks per week.
Walks 2 times per week, about 20 minutes.

VITALS
BP 139/79 | HR 68 | Temp 98.1 F | Wt 80.6 kg | BMI 28.5 | SpO2 98%

LABS
Date  Test                        Result
2025-04-01  eGFR                        58 mL/min/1.73m2
2025-04-01  Creatinine                  1.06 mg/dL
2025-12-11  eGFR                        78 mL/min/1.73m2
2025-12-11  Creatinine                  0.79 mg/dL
2026-04-10  eGFR                        74 mL/min/1.73m2
2026-04-10  Creatinine                  0.83 mg/dL
2026-04-10  Hemoglobin A1c              8.4%
2026-04-10  Glucose, fasting            171 mg/dL
2026-04-10  Potassium                   3.8 mmol/L
2026-04-10  Sodium                      143 mmol/L
2026-04-10  LDL cholesterol             74 mg/dL
2026-04-10  Hemoglobin                  12.8 g/dL

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

ASSESSMENT AND PLAN
1. T2DM: A1c 8.4%, improved from 9.4%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Essential hypertension: BP 139/79. Reinforced low-sodium diet; continue lisinopril 20 mg.
3. Chronic kidney disease on problem list, removed today: eGFR 78 and 74 on repeat testing over 6 months, urine albumin normal; prior eGFR 58 (2025-04-01) was during an acute illness. Does not have chronic kidney disease.
4. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
5. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
6. Hypothyroid: clinically euthyroid. Continue current dose.
7. Colorectal cancer screening up to date. Shingles vaccine series completed.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Reviewed sick-day rules for medications.

Return to clinic in 6 months or sooner as needed.
Total time 44 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Physician, DO 2026-04-13 08:13
```

</details>

## 35. FU-0263 — F3_not_face_to_face

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but it is a chart-review e-consult; the patient was not seen (rule R1).

Check:
- [ ] The header and HPI say the patient was not seen.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0263    Age: 64    Sex: F
Date of service: 2026-07-12    Visit type: Interprofessional e-consult (chart review; patient not seen)
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 10

REASON FOR E-CONSULT
Question from primary care team about diabetes and kidney function management.

HISTORY OF PRESENT ILLNESS
Chart reviewed for 64-year-old woman; patient not seen or examined for this consult. History of type 2 diabetes diagnosed 6 years ago. Glucose log documented at last office visit: fasting 107-159 mg/dL.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- CKD, stage 3b
- Osteoarthritis, bilateral knees
- Hypothyroidism

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- levothyroxine 75 mcg daily
Medication list taken from the chart; not reconciled with the patient.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Sister: hypothyroidism.
Mother: hypertension.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2005; 7 pack-years.
Lives with daughter. Retired teacher.
Walks 5 times per week, about 20 minutes.

VITALS
Last recorded in clinic: BP 131/73, weight 65.4 kg (not measured today).

EXAM
Not performed; patient not seen for this e-consult.

LABS
Date  Test                        Result
2025-11-20  eGFR                        30 mL/min/1.73m2
2026-07-11  eGFR                        36 mL/min/1.73m2
2026-07-11  Hemoglobin A1c              7.2%
2026-07-11  Glucose, fasting            130 mg/dL
2026-07-11  Urine albumin/creatinine    228 mg/g
2026-07-11  Potassium                   4.1 mmol/L
2026-07-11  Sodium                      141 mmol/L
2026-07-11  LDL cholesterol             128 mg/dL
2026-07-11  Hemoglobin                  12.5 g/dL

E-CONSULT ASSESSMENT AND RECOMMENDATIONS
1. Diabetes mellitus, type 2: A1c 7.2% (up from 6.3%). Recommend continuing the current regimen.
2. Diabetic chronic kidney disease, stage 3b: Latest eGFR 36 (up from 30), UACR 228 mg/g. Recommend continuing losartan and empagliflozin; repeat BMP and UACR in 3 months.
3. Knee osteoarthritis: stable per chart review; no change recommended.
4. Hypothyroidism: stable per chart review; no change recommended.

Recommendations sent to the primary care team. Total time spent on chart review: 15 minutes.
Electronically signed: Synthetic Associate, PA-C 2026-07-12 13:50
```

</details>

## 36. FU-0282 — G5_minimal

**Label: 1 (supports E11.22).** Borderline: 'CKD 3a, stable on losartan' as its own line counts as status plus treatment.

Check:
- [ ] Do you agree this minimal line counts as addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0282    Age: 81    Sex: M
Date of service: 2026-09-19    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 2

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
Patient is a 81-year-old man returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 12 years ago. Notes some difficulty with diet recently; fasting sugars 122-168 mg/dL. Energy fair. No new complaints today. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Genitourinary: no dysuria, hematuria or change in urine output.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Eyes: no blurred vision; last dilated eye exam 2025.
Respiratory: no cough or dyspnea on exertion.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Neurological: no numbness or tingling in the feet; no headaches.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- dapagliflozin 10 mg daily
- atorvastatin 40 mg nightly
- levothyroxine 75 mcg daily
- loratadine 10 mg as needed
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Sulfa drugs (hives).

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease, stage 3b
- Hyperlipidemia
- Hypothyroidism
- Seasonal allergic rhinitis
- Essential hypertension

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)
- Right knee arthroscopy (2015)
- Appendectomy (1988)

FAMILY HISTORY
Sister: hypothyroidism.
Mother: hypertension.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Works part time as a cashier.
Alcohol: none.

VITALS
BP 123/69 | HR 72 | Temp 98.2 F | Wt 87.2 kg | BMI 28.2 | SpO2 99%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2026-05-09  eGFR                        32 mL/min/1.73m2
2026-09-15  eGFR                        37 mL/min/1.73m2
2026-09-15  Creatinine                  1.67 mg/dL
2026-09-15  Hemoglobin A1c              7.3%
2026-09-15  Glucose, fasting            159 mg/dL
2026-09-15  Urine albumin/creatinine    239 mg/g
2026-09-15  Potassium                   3.9 mmol/L
2026-09-15  Sodium                      141 mmol/L
2026-09-15  LDL cholesterol             107 mg/dL
2026-09-15  Hemoglobin                  12.2 g/dL

INTERVAL NOTE - PREVIOUS VISIT 2026-05-14
(For reference only; not today's assessment.)
Diabetes mellitus, type 2: A1c 6.0% at that visit; continued medications.
CKD 3b: eGFR 32 at that visit; continued lisinopril.
HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.

IMPRESSION AND PLAN
1. Diabetes mellitus, type 2: A1c 7.3%, up from 6.0%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hyperlipidemia: LDL 107 mg/dL. Continue atorvastatin 40 mg.
3. HTN: at goal on current regimen. Continue lisinopril.
4. Hypothyroid: clinically euthyroid. Continue current dose.
5. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
6. CKD 3b, stable on lisinopril; no changes.
7. Shingles vaccine series completed. Colorectal cancer screening up to date.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Reviewed sick-day rules for medications.

Return to clinic in 6 months or sooner as needed.
Total time 37 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Practitioner, FNP-C 2026-09-19 14:12
```

</details>

## 37. FU-0284 — G3_med_change

**Label: 1 (supports E11.22).** Borderline: metformin reduced because of the eGFR counts as treating the kidney disease, even though CKD is not named in that line.

Check:
- [ ] CKD is on the problem list; the diabetes plan reduces metformin because of eGFR. Do you agree this counts as addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0284    Age: 65    Sex: F
Date of service: 2026-05-28    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
65-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 22 years ago. States adherence to medications is good. Denies hypoglycemic episodes. No polyuria or polydipsia. No visual changes. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Constitutional: denies fever, chills or unintended weight loss.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Cardiovascular: no chest pain, palpitations or orthopnea.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Skin: no rashes or non-healing wounds.
Respiratory: no cough or dyspnea on exertion.
Eyes: no blurred vision; last dilated eye exam 2023.
Neurological: no numbness or tingling in the feet; no headaches.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease, stage 3a
- Seasonal allergic rhinitis
- Hyperlipidemia
- Hypothyroidism
- Obesity

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Cholecystectomy (2011)
- Right knee arthroscopy (2015)

MEDICATIONS
- metformin 1000 mg twice daily (dose being reduced today)
- empagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- atorvastatin 40 mg nightly
- levothyroxine 75 mcg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
No family history of kidney disease reported.
Mother: hypertension.
Father: coronary artery disease, died age 70.

SOCIAL HISTORY
Never smoker.
Walks 4 times per week, about 20 minutes.
Works part time as a librarian.

VITALS
BP 125/83 | HR 89 | Temp 98.7 F | Wt 88.5 kg | BMI 31.8 | SpO2 97%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2026-01-29  eGFR                        45 mL/min/1.73m2
2026-01-29  Creatinine                  1.37 mg/dL
2026-05-21  eGFR                        50 mL/min/1.73m2
2026-05-21  Creatinine                  1.24 mg/dL
2026-05-21  Hemoglobin A1c              9.6%
2026-05-21  Glucose, fasting            172 mg/dL
2026-05-21  Urine albumin/creatinine    340 mg/g
2026-05-21  Potassium                   4.3 mmol/L
2026-05-21  Sodium                      137 mmol/L
2026-05-21  LDL cholesterol             99 mg/dL
2026-05-21  Hemoglobin                  11.3 g/dL

ASSESSMENT/PLAN
1. Diabetes mellitus, type 2: A1c 9.6% (improved from 10.3%). Metformin reduced to 500 mg twice daily because eGFR is now 50 (stable from 45).
2. Hyperlipidemia: LDL 99 mg/dL. Continue atorvastatin 40 mg.
3. Obesity: weight 88.5 kg. Continue lifestyle changes.
4. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
5. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
6. Shingles vaccine series completed. Pneumococcal vaccination up to date.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Discussed hypoglycemia recognition and treatment.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Associate, PA-C 2026-05-28 16:27
```

</details>

## 38. FU-0289 — G2_see_nephrology

**Label: 0 (does not support E11.22).** Borderline: 'see nephrology note' gives no status or action today.

Check:
- [ ] The plan's CKD line only points to nephrology. Do you agree this is not addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0289    Age: 53    Sex: F
Date of service: 2026-05-28    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 8

CHIEF COMPLAINT
Chronic disease management visit.

HISTORY OF PRESENT ILLNESS
Established patient, 53-year-old woman, presenting for chronic disease follow-up. History of type
--- Page 2 of 3 --- FU-0289 --- printed 2026-06-06 ---
2 diabetes diagnosed 20 years ago. Brought meter today; morning values 124-136 mg/dL, no lows. No urinary symptoms. No foot ulcers or numbness reported. Mild bilateral knee stiffness in the mornings, unchanged.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Respiratory: no cough or dyspnea on exertion.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Eyes: no blurred vision; last dilated eye exam 2025.
Skin: no rashes or non-healing wounds.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- CKD, stage 3a
- Osteoart-
hritis, bilateral knees
- Seasonal allergic rhinitis
- Essential hypertension

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Tonsillectomy (childhood)

MEDICAT-
IONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- acetaminophen 650 mg as needed
- loratadine 10 mg as needed
- lisinopril 20 mg daily
Medication reconciliation com-
pleted; no changes other than those noted in the plan.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Father: coronary artery disease, died age 70.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2013; 23 pack-years.
Wa1ks 2 times per week, about 20 minutes.
Alcohol: rare.

VITALS
BP 135/92 | HR 82 | Temp 98.0 F | Wt 56.0 kg | BMI 23.7 | SpO2 99%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date Test	Result
2026-05-21	eGFR	47 mL/min/1.73m2
2026-05-21    Creatinine  1.31 mg/dL
2026-05-21	Hemoglobin A1c        8.8%
2026-05-21	Glucose, fasting 110 mg/dL
2026-05-21	Urine albumin/creatinine 94 mg/g
2026-05-21   Potassium         5.0 mmol/L
2026-05-21   Sodium        141 mmol/L
2026-05-21 LDL cholesterol     85 mg/dL
2026-05-21	Hemoglobin 12.3 g/dL

IMPRESSI0N AND PLAN
1. T2DM: A1c 8.8%, up from 8.1%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Essential hypertension: BP 135/92. Reinforced low-sodium diet; continue lisinopril 20 mg.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. Chronic kidney disease, stage 3a: See nephrology note.
5. 0A of knees: continue home exercises and acetaminophen PRN.
6. Pneumococcal vaccination up to date. Dental visit within the past year.

PATlENT EDUCATION
Patient verbalized understanding of the plan.
Discussed hypoglycemia recognition and treatment.

Return to clinic in 6 months or sooner as needed.
E1ectronically signed: Synthetic Provider, MD 2026-05-28 10:02
```

</details>

## 39. FU-0291 — A_P3_link_no_stage

**Label: 1 (supports E11.22).** Diabetic CKD addressed in today's plan; no stage, which does not affect the label.

Check:
- [ ] No CKD stage appears anywhere.
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0291    Age: 74    Sex: F
Date of service: 2026-01-29    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 13

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
74-year-old woman seen today for routine chronic care. History of type 2 diabetes diagnosed 6 years ago. States adherence to medications is good. Denies
--- Page 2 of 3 --- FU-0291 --- printed 2026-02-16 ---
hypoglycemic episodes. Denies chest pain, shortness of breath or leg swelling. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Respiratory: no cough or dyspnea on exertion.
Neurological: no numbness or tingling in the feet; no headaches.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Eyes: no blurred vision; last dilated eye exam 2023.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Genitourinary: no dysuria, hematuria or change in urine output.
Constitutiona1: denies fever, chills or unintended weight loss.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease
- Essential hypertension
- GERD
- Hyperlipidemia

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)
- Cataract extraction, left eye (2022)
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- dapagliflozin 10 mg daily
- lisinopril 20 mg daily
- omeprazole 20 mg daily
- atorvastatin 40 mg nightly
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
No family history of kidney disease reported.
Father: coronary artery disease, died age 79.
Sister: hypo-
thyroidism.

SOCIAL HISTORY
Former smoker, quit 1998; 7 pack-years.
Works part time as a librarian.
Lives with daughter. Retired teacher.

VITALS
BP 132/81 | HR 70 | Temp 98.7 F | Wt 83.5 kg | BMI 28.0 | SpO2 97%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date    Test	Result
2025-10-21  eGFR        38 mL/min/1.73m2
2025-10-21  Creatinine	1.62 mg/dL
2026-01-26    eGFR	42 mL/min/1.73m2
2026-01-26	Hemoglobin A1c	9.1%
2026-01-26 Glucose, fasting       188 mg/dL
2026-01-26	Urine albumin/creatinine	359 mg/g
2026-01-26   Potassium         4.7 mmol/L
2026-01-26 Sodium 136 mmol/L
2026-01-26  LDL cholesterol	101 mg/dL
2026-01-26	Hemoglobin	11.2 g/dL

IMPRESSION AND PLAN
1. Diabetes mellitus, type 2: A1c 9.1% (improved from 10.1%). Medications unchanged; reinforced carbohydrate counting.
2. Gastroesophageal reflux: stable; disc-
ussed trial of dose reduction at next visit.
3. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
4. Essential hypertension: BP 132/81. Reinforced low-sodium diet; continue lisinopril 20 mg.
5. Diabetic kidney disease: eGFR 42 (stable from 38), albuminuria 359 mg/g. lncreased lisinopril to 40 mg daily. Repeat potassium and creatinine in 2 weeks.
6. Diabetic foot exam completed today. Colorectal cancer screening up to date.

PATIENT EDUCATI0N
Discussed hypoglycemia recognition and treatment.
Patient verbalized understanding of the plan.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-01-29 11:11
```

</details>

## 40. FU-0293 — C3_t1_in_hpi_only

**Label: 0 (does not support E11.22).** Type 1 diabetes (stated in the HPI) even though the plan says just 'diabetes', so not E11.

Check:
- [ ] The HPI says type 1 diabetes.
- [ ] Nowhere says type 2.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0293    Age: 59    Sex: M
Date of service: 2026-03-25    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 4

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
59-year-old man here for a 6-month check-in. Type 1 diabetes since age 27. Has been trying to walk 3 times per week. Glucose readings 111-136 mg/dL fasting. Energy fair. No new complaints today. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Skin: no rashes or non-healing wounds.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2025.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Respiratory: no cough or dyspnea on exertion.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

MEDICATIONS
- insulin pump (lispro) with continuous glucose monitor
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- acetaminophen 650 mg as needed
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
NKDA.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes, insulin pump
- CKD, stage 4
- Seasonal allergic rhinitis
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)

FAMILY HISTORY
No family history of kidney disease reported.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Works part time as a librarian.
Alcohol: none.

VITALS
BP 148/83 | HR 86 | Temp 98.7 F | Wt 73.7 kg | BMI 27.4 | SpO2 96%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2026-03-15  eGFR                        17 mL/min/1.73m2
2026-03-15  Creatinine                  3.63 mg/dL
2026-03-15  Hemoglobin A1c              8.5%
2026-03-15  Glucose, fasting            129 mg/dL
2026-03-15  Urine albumin/creatinine    253 mg/g
2026-03-15  Potassium                   4.4 mmol/L
2026-03-15  Sodium                      140 mmol/L
2026-03-15  LDL cholesterol             89 mg/dL
2026-03-15  Hemoglobin                  13.6 g/dL

ASSESSMENT/PLAN
1. Diabetes mellitus: A1c 8.5%. Continue basal-bolus insulin; reviewed CGM download, time in range 61%. Endocrinology follow-up in 3 months.
2. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
3. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
4. CKD, stage 4: eGFR 17 today (no prior for comparison). Continue losartan. Recheck BMP and urine albumin-to-creatinine ratio in 3 months.
5. Shingles vaccine series completed. Retinal exam due; referral placed.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Reviewed sick-day rules for medications.

Return to clinic in 6 months or sooner as needed.
Total time 33 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Physician, DO 2026-03-25 15:08
```

</details>

