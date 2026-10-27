# Label review: 40 of the 100 stage-1 charts

For each chart, read the note and decide whether the **label** (does the note support reporting E11.22 for risk adjustment?) is right, using the reason and the checks given. You do not need to check the rubric answers. Record your verdict in `label_review.csv` (agree / disagree, plus a short note), or just list the chart IDs you disagree with.

About 45% of charts have deliberate 'format noise' (letters swapped with digits such as 'C1inician', words broken across lines, a stray page header). That is intended and is not an error.

Label rules: supported (1) only if type 2 diabetes is documented (untyped diabetes defaults to type 2), CKD is an established diagnosis, CKD is addressed at this visit, no non-diabetic cause is given for the CKD, the visit is face-to-face with an MD, DO, NP or PA (R1), and the note is signed with credentials (R2). Secondary diabetes is not type 2 (R3).

## 1. FU-0002 — G4_list_entry

**Label: 0 (does not support E11.22).** Borderline: CKD only in a 'chronic conditions reviewed' list, no status or action.

Check:
- [ ] Do you agree this is not addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0002    Age: 48    Sex: F
Date of service: 2026-04-04    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 6

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
48-year-old woman here for a 6-month check-in. History of type 2 diabetes diagnosed 5 years ago. Brought meter today; morning values 127-162 mg/dL, no lows. Denies chest pain, shortness of breath or leg swelling. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Neurological: no numbness or tingling in the feet; no headaches.
Skin: no rashes or non-healing wounds.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2023.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD stage 3a
- Hypothyroidism
- Osteoarthritis, bilateral knees
- Hyperlipidemia

PAST SURGICAL HISTORY
- Cholecystectomy (2011)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- levothyroxine 75 mcg daily
- acetaminophen 650 mg as needed
- atorvastatin 40 mg nightly
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Mother: hypertension.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Lives with alone. Retired machinist.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 124/73 | HR 81 | Temp 98.0 F | Wt 69.1 kg | BMI 23.7 | SpO2 98%

LABS
Date  Test                        Result
2025-12-17  eGFR                        54 mL/min/1.73m2
2026-03-26  eGFR                        51 mL/min/1.73m2
2026-03-26  Hemoglobin A1c              7.3%
2026-03-26  Glucose, fasting            155 mg/dL
2026-03-26  Urine albumin/creatinine    130 mg/g
2026-03-26  Potassium                   5.0 mmol/L
2026-03-26  Sodium                      142 mmol/L
2026-03-26  LDL cholesterol             85 mg/dL
2026-03-26  Hemoglobin                  12.8 g/dL

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

INTERVAL NOTE - PREVIOUS VISIT 2025-12-21
(For reference only; not today's assessment.)
T2DM: A1c 6.5% at that visit; continued medications.
CKD stage 3a: eGFR 54 at that visit; continued losartan.
Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.

ASSESSMENT AND PLAN
1. T2DM: A1c 7.3%, up from 6.5%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
3. OA of knees: continue home exercises and acetaminophen PRN.
4. Chronic conditions reviewed: hyperlipidemia, CKD 3a.
5. Retinal exam due; referral placed. Dental visit within the past year.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Reviewed carbohydrate counting handout.

Return to clinic in 6 months or sooner as needed.
Total time 34 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Practitioner, FNP-C 2026-04-04 08:25
```

</details>

## 2. FU-0013 — G5_minimal

**Label: 1 (supports E11.22).** Borderline: 'CKD 3a, stable on losartan' as its own line counts as status plus treatment.

Check:
- [ ] Do you agree this minimal line counts as addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0013    Age: 61    Sex: M
Date of service: 2026-03-16    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 2

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
61-year-old man here for a
--- Page 2 of 3 --- FU-0013 --- printed 2026-03-24 ---
4-month check-in. History of type 2 diabetes diagnosed 14 years ago. States adherence to medications is good. Denies hypoglycemic episodes. Appetite stable. Denies nausea or abdominal pain. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Constitutional: denies fever, chills or unintended weight loss.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Cardiovascular: no chest pain, palpitations or orthopnea.
Skin: no rashes or non-healing wounds.
Eyes: no blurred vision; last dilated eye exam 2023.
Respiratory: no cough or dyspnea on exertion.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease, stage 3a
- Hyperlipidemia
- Obesity
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Appendectomy (1988)
- Right knee arthroscopy (2015)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- atorvastatin 40 mg nightly
- loratadine 10 mg as needed
Med rec done with patient’s pill bottles.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
Sister: hypothyroidism.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2010; 18 pack-years.
Works part time as a consultant.
Lives with alone. Retired teacher.

VITALS
BP 141/92 | HR 75 | Temp 98.6 F | Wt 110.0 kg | BMI 37.0 | SpO2 97%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date	Test	Result
2025-08-19   eGFR	58 mL/min/1.73m2
2025-08-19    Creatinine      1.06 mg/dL
2026-03-14	eGFR    45 mL/min/1.73m2
2026-03-14 Creatinine	1.37 mg/dL
2026-03-14    Hemoglobin A1c	9.3%
2026-03-14	Glucose, fasting  140 mg/dL
2026-03-14    Urine albumin/creatinine 69 mg/g
2026-03-14	Potassium 4.9 mmol/L
2026-03-14  Sodium	138 mmo1/L
2026-03-14	LDL cholesterol 103 mg/dL
2026-03-14  Hemoglobin         13.7 g/dL

PRIOR VISIT SUMMARY (2025-08-22)
(For reference only; not today’s assessment.)
T2DM: A1c 10.1% at that visit; continued medications.
CKD 3a: eGFR 58 at that visit; continued losartan.
Hyperlipidemia: LDL 103 mg/dL. Continue atorvastatin 40 mg.

ASSESSMENT/PLAN
1. T2DM: A1c 9.3% (improved from 10.1%). Medications unchanged; reinforced carbohydrate counting.
2. CKD 3a, stab1e on losartan.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. Obesity, BMl 37.0: discussed nutrition and activity goals; referred to dietitian.
5. Hyperlipidemia: LDL 103 mg/dL. Continue atorvastatin 40 mg.
6. Diabetic foot exam completed today. lnf1uenza vaccine given this season.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Patient verbalized understanding of the plan.

Return to clinic in 3 months or sooner as needed.
Total time 31 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Phy-
sician, DO 2026-03-16 09:21
```

</details>

## 3. FU-0019 — C3_t1_in_hpi_only

**Label: 0 (does not support E11.22).** Type 1 diabetes (stated in the HPI) even though the plan says just 'diabetes', so not E11.

Check:
- [ ] The HPI says type 1 diabetes.
- [ ] Nowhere says type 2.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0019    Age: 54    Sex: M
Date of service: 2026-02-07    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
Established patient, 54-year-old man, presenting for chronic disease follow-up. Type 1 diabetes since age 12. Reports checking glucose
--- Page 2 of 3 --- FU-0019 --- printed 2026-02-18 ---
daily; fasting readings mostly 117-173 mg/dL. Denies chest pain, shortness of breath or leg swelling. Mild bilateral knee stiffness in the momings, unchanged.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Skin: no rashes or non-healing wounds.
Respiratory: no cough or dyspnea on exertion.
Genitourinary: no dysuria, hematuria or change in urine output.
Cardiovascular: no chest pain, palpitations or orthopnea.
Constitutional: denies fever, chills or unintended weight loss.
Eyes: no blurred vision; last dilated eye exam 2024.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus, on insulin
- CKD stage 3a
- Obesity
- Osteoarthritis, bilateral knees
- Hyperlipidemia
- GERD

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Right knee arthroscopy (2015)
- Tonsillectomy (childhood)

MEDICATIONS
- insulin pump (lispro) with continuous glucose monitor
- empagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- atorvastatin 40 mg nightly
- omeprazole 20 mg daily
Medicat-
ions reviewed with patient and pharmacy list; list above is current.

ALLE-
RGIES
Penicillin (rash).

FAMILY HISTORY
Sister: hypothyroidism.
Mother: hypertension.

SOCIAL HISTORY
Former smoker, quit 2002; 15 pack-years.
Walks 5 times per week, about 20 minutes.
Lives with spouse. Retired teacher.

VITALS
BP 141/84 | HR 73 | Temp 98.3 F | Wt 124.6 kg | BMI 36.2 | SpO2 98%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date    Test      Result
2026-01-28 eGFR     56 mL/min/1.73m2
2026-01-28    Hemoglobin A1c	8.7%
2026-01-28 Glucose, fasting	120 mg/dL
2026-01-28	Urine albumin/creatinine   126 mg/g
2026-01-28   Potassium 4.6 mmol/L
2026-01-28   Sodium	138 mmol/L
2026-01-28   LDL cholesterol 62 mg/dL
2026-01-28	Hemoglobin	13.2 g/dL

ASSESSMENT AND PLAN
1. Diabetes mellitus: A1c 8.7%. Continue basal-bolus insulin; reviewed CGM download, time in range 61%. Endocrinology follow-up in 3 months.
2. Chronic kidney disease stage 3a due to diabetes: eGFR 56 today (no prior for comparison). Continue losartan. Recheck BMP and urine albumin-to-creatinine ratio in 3 months.
3. 0besity: weight 124.6 kg. Continue lifestyle changes.
4. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
5. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
6. OA of knees: continue home exercises and acetaminophen PRN.
7. Diabetic foot exam completed today. Shingles vaccine series completed.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Patient verbalized understanding of the plan.

Retum to clinic in 3 months or sooner as needed.
Total time 43 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-02-07 14:03
```

</details>

## 4. FU-0031 — B2_copy_stale

**Label: 0 (does not support E11.22).** Plan copied from a prior visit; the CKD line refers only to an old eGFR and the old plan; nothing current.

Check:
- [ ] The CKD line's eGFR is dated months before the visit.
- [ ] No eGFR from the last 30 days anywhere in the note.
- [ ] No other CKD status or action today.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0031    Age: 80    Sex: F
Date of service: 2026-09-27    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
80-year-old woman seen today for routine chronic care. History of type 2 diabetes diagnosed 18 years ago. Home glucose log reviewed, fasting values 113-136 mg/dL with occasional post-meal readings above 200. No polyuria or polydipsia. No visual changes. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Constitutional: denies fever, chills or unintended weight loss.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Eyes: no blurred vision; last dilated eye exam 2025.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Skin: no rashes or non-healing wounds.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD, stage 3a
- Osteoarthritis, bilateral knees
- GERD

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Appendectomy (1988)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- omeprazole 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
No family history of kidney disease reported.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 2011; 29 pack-years.
Lives with spouse. Retired machinist.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 127/80 | HR 85 | Temp 97.9 F | Wt 66.1 kg | BMI 28.5 | SpO2 96%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2026-02-21  eGFR                        48 mL/min/1.73m2
2026-06-07  eGFR                        51 mL/min/1.73m2
2026-09-23  Hemoglobin A1c              6.7%
2026-09-23  Glucose, fasting            138 mg/dL
2026-09-23  LDL cholesterol             70 mg/dL
2026-09-23  Hemoglobin                  14.3 g/dL

IMPRESSION AND PLAN
(Plan unchanged from visit of 2026-06-09.)
1. Diabetes mellitus, type 2: A1c 6.7% today (improved from 7.4%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Chronic kidney disease stage 3a due to type 2 diabetes: eGFR 51 (2026-06-07), stable at that time. Continue regimen as previously outlined.
3. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
4. OA of knees: continue home exercises and acetaminophen PRN.
5. Retinal exam due; referral placed. Diabetic foot exam completed today.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Reviewed carbohydrate counting handout.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-09-27 14:25
```

</details>

## 5. FU-0040 — D_creat_only_neg

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

## 6. FU-0046 — E2_likely_diabetic

**Label: 1 (supports E11.22).** 'Likely diabetic nephropathy' with a CKD stage; the cause is hedged but not another disease. CKD addressed today.

Check:
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0046    Age: 57    Sex: M
Date of service: 2026-01-29    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 13

CHIEF COMPLAINT
Follow-up visit; medication refills.

HISTORY OF PRESENT ILLNESS
Established patient, 57-year-old man, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 20 years ago. Home glucose log reviewed, fasting values 114-140 mg/dL with occasional post-meal readings above 200. Mild bilateral knee stiffness in the mornings, unchanged. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Respiratory: no cough or dyspnea on exertion.
Constitutional: denies fever, chills or unintended weight loss.
Eyes: no blurred vision; last dilated eye exam 2023.
Genitourinary: no dysuria, hematuria or change in urine output.
Skin: no rashes or non-healing wounds.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- acetaminophen 650 mg as needed
Med rec done with patient's pill bottles.

ALLERGIES
Penicillin (rash).

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease, stage 3a
- Seasonal allergic rhinitis
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Cholecystectomy (2011)
- Appendectomy (1988)

FAMILY HISTORY
Brother: hyperlipidemia.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2006; 5 pack-years.
Works part time as a consultant.
Walks 2 times per week, about 20 minutes.

VITALS
BP 139/88 | HR 71 | Temp 98.4 F | Wt 90.7 kg | BMI 27.5 | SpO2 95%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date  Test                        Result
2025-10-11  eGFR                        51 mL/min/1.73m2
2025-10-11  Creatinine                  1.21 mg/dL
2026-01-21  eGFR                        55 mL/min/1.73m2
2026-01-21  Creatinine                  1.12 mg/dL
2026-01-21  Hemoglobin A1c              7.1%
2026-01-21  Glucose, fasting            124 mg/dL
2026-01-21  Urine albumin/creatinine    362 mg/g
2026-01-21  Potassium                   4.4 mmol/L
2026-01-21  Sodium                      143 mmol/L
2026-01-21  LDL cholesterol             103 mg/dL
2026-01-21  Hemoglobin                  11.9 g/dL

INTERVAL NOTE - PREVIOUS VISIT 2025-10-17
(For reference only; not today's assessment.)
T2DM: A1c 6.3% at that visit; continued medications.
Chronic kidney disease stage 3a, most likely due to type 2 diabetes: eGFR 51 at that visit; continued losartan.
Allergic rhinitis: seasonal symptoms; continue loratadine PRN.

ASSESSMENT/PLAN
1. T2DM: A1c 7.1%, up from 6.3%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Chronic kidney disease stage 3a, most likely due to type 2 diabetes: eGFR 55, UACR 362 mg/g. On empagliflozin and losartan; counseled on avoiding nephrotoxins. Repeat labs in 3 months.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. OA of knees: continue home exercises and acetaminophen PRN.
5. Influenza vaccine given this season. Retinal exam due; referral placed.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Patient verbalized understanding of the plan.

Return to clinic in 6 months or sooner as needed.
Total time 26 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Associate, PA-C 2026-01-29 12:44
```

</details>

## 7. FU-0049 — E1_dm_and_htn

**Label: 1 (supports E11.22).** CKD due to diabetes and hypertension; diabetes is a stated cause. CKD addressed today.

Check:
- [ ] The plan states both diabetes and hypertension as causes.
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0049    Age: 50    Sex: F
Date of service: 2026-02-28    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 9

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
50-year-old woman seen today for routine chronic care. History of type 2 diabetes diagnosed 16 years ago. Brought meter today; morning values 111-138 mg/dL, no lows. No urinary symptoms. No foot ulcers or numbness reported. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Skin: no rashes or non-healing wounds.
Respiratory: no cough or dyspnea on exertion.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Cardiovascular: no chest pain, palpitations or orthopnea.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Eyes: no blurred vision; last dilated eye exam 2024.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease, stage 3b
- Osteoarthritis, bilateral knees
- Hypothyroidism
- Obesity
- Seasonal allergic rhinitis
- Essential hypertension

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- dapagliflozin 10 mg daily
- acetaminophen 650 mg as needed
- levothyroxine 75 mcg daily
- loratadine 10 mg as needed
- lisinopril 20 mg daily
Med rec done with patient's pill bottles.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Father: coronary artery disease, died age 67.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Alcohol: none.
Walks 5 times per week, about 20 minutes.

VITALS
BP 145/75 | HR 75 | Temp 98.6 F | Wt 97.0 kg | BMI 33.0 | SpO2 97%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date  Test                        Result
2025-11-15  eGFR                        31 mL/min/1.73m2
2026-02-24  eGFR                        35 mL/min/1.73m2
2026-02-24  Hemoglobin A1c              9.1%
2026-02-24  Glucose, fasting            178 mg/dL
2026-02-24  Urine albumin/creatinine    88 mg/g
2026-02-24  Potassium                   4.8 mmol/L
2026-02-24  Sodium                      140 mmol/L
2026-02-24  LDL cholesterol             129 mg/dL
2026-02-24  Hemoglobin                  11.8 g/dL

ASSESSMENT AND PLAN
1. T2DM: A1c 9.1%, up from 8.0%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Obesity, BMI 33.0: discussed nutrition and activity goals; referred to dietitian.
3. Hypothyroid: clinically euthyroid. Continue current dose.
4. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
5. Essential hypertension: BP 145/75. Reinforced low-sodium diet; continue lisinopril 20 mg.
6. CKD stage 3b due to type 2 diabetes and hypertension: Renal function reviewed: eGFR 35 (stable from 31). Continue lisinopril and dapagliflozin. Avoid NSAIDs. Nephrology follow-up as scheduled.
7. OA of knees: continue home exercises and acetaminophen PRN.
8. Retinal exam due; referral placed. Influenza vaccine given this season.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 6 months or sooner as needed.
Total time 32 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-02-28 12:14
```

</details>

## 8. FU-0054 — A_N1a_problem_list_only

**Label: 0 (does not support E11.22).** CKD appears only on the problem list; the assessment and plan does not address it.

Check:
- [ ] No CKD line in the assessment and plan (a prior-visit section, if any, is not today's plan).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0054    Age: 75    Sex: M
Date of service: 2026-07-19    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 3

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
Patient is a 75-year-old man returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 16 years ago. Has been trying to walk 3 times per week. Glucose readings 115-147 mg/dL fasting. Mild bilateral knee stiffness in the mornings, unchanged. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Cardiovascular: no chest pain, palpitations or orthopnea.
Neurological: no numbness or tingling in the feet; no headaches.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2024.
Constitutional: denies fever, chills or unintended weight loss.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Respiratory: no cough or dyspnea on exertion.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD, stage 3a
- Hyperlipidemia
- Osteoarthritis, bilateral knees
- Seasonal allergic rhinitis
- Essential hypertension

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)
- Cholecystectomy (2011)

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- atorvastatin 40 mg nightly
- acetaminophen 650 mg as needed
- loratadine 10 mg as needed
- lisinopril 20 mg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
NKDA.

FAMILY HISTORY
Brother: hyperlipidemia.
Father: coronary artery disease, died age 67.
Mother: hypertension.

SOCIAL HISTORY
Never smoker.
Works part time as a cashier.
Walks 4 times per week, about 20 minutes.

VITALS
BP 121/88 | HR 82 | Temp 98.6 F | Wt 93.7 kg | BMI 27.7 | SpO2 96%

LABS
Date  Test                        Result
2025-12-09  eGFR                        50 mL/min/1.73m2
2025-12-09  Creatinine                  1.24 mg/dL
2026-07-11  eGFR                        49 mL/min/1.73m2
2026-07-11  Creatinine                  1.26 mg/dL
2026-07-11  Hemoglobin A1c              7.1%
2026-07-11  Glucose, fasting            154 mg/dL
2026-07-11  Urine albumin/creatinine    222 mg/g
2026-07-11  Potassium                   4.4 mmol/L
2026-07-11  Sodium                      139 mmol/L
2026-07-11  LDL cholesterol             64 mg/dL
2026-07-11  Hemoglobin                  13.9 g/dL

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

ASSESSMENT AND PLAN
1. Diabetes mellitus, type 2: A1c 7.1% today (up from 6.0%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
3. Essential hypertension: BP 121/88. Reinforced low-sodium diet; continue lisinopril 20 mg.
4. Hyperlipidemia: LDL 64 mg/dL. Continue atorvastatin 40 mg.
5. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
6. Shingles vaccine series completed. Diabetic foot exam completed today.

PATIENT EDUCATION
Reviewed carbohydrate counting handout.
Reviewed sick-day rules for medications.

Return to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-07-19 12:43
```

</details>

## 9. FU-0058 — C2_t2_on_insulin

**Label: 1 (supports E11.22).** Type 2 diabetes on insulin is still type 2. CKD addressed today.

Check:
- [ ] The note says type 2 and lists insulin.
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0058    Age: 68    Sex: F
Date of service: 2026-04-05    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 11

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
68-year-old woman seen today for routine chronic care. Type 2 diabetes for 11 years; started basal insulin 4 years ago when oral agents were no longer enough. Home glucose log reviewed, fasting values 117-156 mg/dL with occasional post-meal readings above 200. No urinary symptoms. No foot ulcers or numbness reported. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Neurological: no numbness or tingling in the feet; no headaches.
Eyes: no blurred vision; last dilated eye exam 2023.
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus, insulin-requiring
- Chronic kidney disease stage 3a
- Hypothyroidism
- Essential hypertension
- Seasonal allergic rhinitis
- Hyperlipidemia

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)

MEDICATIONS
- insulin glargine 24 units nightly
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- levothyroxine 75 mcg daily
- lisinopril 20 mg daily
- loratadine 10 mg as needed
- atorvastatin 40 mg nightly
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Brother: hyperlipidemia.
No family history of kidney disease reported.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 2006; 12 pack-years.
Works part time as a cashier.
Alcohol: none.

VITALS
BP 127/86 | HR 80 | Temp 98.4 F | Wt 73.5 kg | BMI 26.9 | SpO2 97%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2025-08-17  eGFR                        53 mL/min/1.73m2
2025-08-17  Creatinine                  1.17 mg/dL
2026-03-30  eGFR                        47 mL/min/1.73m2
2026-03-30  Creatinine                  1.31 mg/dL
2026-03-30  Hemoglobin A1c              9.5%
2026-03-30  Glucose, fasting            178 mg/dL
2026-03-30  Urine albumin/creatinine    274 mg/g
2026-03-30  Potassium                   5.0 mmol/L
2026-03-30  Sodium                      137 mmol/L
2026-03-30  LDL cholesterol             108 mg/dL
2026-03-30  Hemoglobin                  13.2 g/dL

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus on insulin: A1c 9.5% today (improved from 10.6%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
3. Hypertension: BP 127/86 today. Continue lisinopril 20 mg daily. Home BP log reviewed.
4. CKD stage 3a: Renal function reviewed: eGFR 47 (down from 53). Continue lisinopril and empagliflozin. Avoid NSAIDs. Nephrology follow-up as scheduled.
5. Hypothyroid: clinically euthyroid. Continue current dose.
6. Hyperlipidemia: LDL 108 mg/dL. Continue atorvastatin 40 mg.
7. Shingles vaccine series completed. Diabetic foot exam completed today.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Reviewed carbohydrate counting handout.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-04-05 10:39
```

</details>

## 10. FU-0087 — D_eq60

**Label: 0 (does not support E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0087    Age: 72    Sex: M
Date of service: 2026-03-04    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 12

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
72-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 9 years ago. Reports checking glucose a few times a week; fasting readings mostly 128-158 mg/dL. Energy fair. No new complaints today. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Neurological: no numbness or tingling in the feet; no headaches.
Skin: no rashes or non-healing wounds.
Constitutional: denies fever, chills or unintended weight loss.
Genitourinary: no dysuria, hematuria or change in urine output.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease, stage 3a
- Seasonal allergic rhinitis
- GERD
- Hypothyroidism
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Cholecystectomy (2011)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
- acetaminophen 650 mg as needed
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
No family history of kidney disease reported.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Walks 5 times per week, about 20 minutes.
Lives with spouse. Retired machinist.

VITALS
BP 127/74 | HR 74 | Temp 98.0 F | Wt 95.2 kg | BMI 27.0 | SpO2 98%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2025-09-25  eGFR                        54 mL/min/1.73m2
2026-02-22  eGFR                        60 mL/min/1.73m2
2026-02-22  Creatinine                  1.03 mg/dL
2026-02-22  Hemoglobin A1c              9.2%
2026-02-22  Glucose, fasting            111 mg/dL
2026-02-22  Urine albumin/creatinine    416 mg/g
2026-02-22  Potassium                   3.9 mmol/L
2026-02-22  Sodium                      136 mmol/L
2026-02-22  LDL cholesterol             93 mg/dL
2026-02-22  Hemoglobin                  14.5 g/dL

ASSESSMENT/PLAN
1. Diabetes mellitus, type 2: A1c 9.2%, up from 7.9%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
3. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
4. GERD: symptoms controlled on omeprazole. Continue.
5. OA of knees: continue home exercises and acetaminophen PRN.
6. Dental visit within the past year. Influenza vaccine given this season.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-03-04 12:26
```

</details>

## 11. FU-0093 — B2_copy_stale

**Label: 0 (does not support E11.22).** Plan copied from a prior visit; the CKD line refers only to an old eGFR and the old plan; nothing current.

Check:
- [ ] The CKD line's eGFR is dated months before the visit.
- [ ] No eGFR from the last 30 days anywhere in the note.
- [ ] No other CKD status or action today.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0093    Age: 54    Sex: M
Date of service: 2026-07-18    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Associate, PA-C (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
Established patient, 54-year-old man, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 19 years ago. Reports checking glucose a few times a week; fasting readings mostly 126-162 mg/dL. Denies chest pain, shortness of breath or leg swelling. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Genitourinary: no dysuria, hematuria or change in urine output.
Respiratory: no cough or dyspnea on exertion.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Cardiovascular: no chest pain, palpitations or orthopnea.
Constitutional: denies fever, chills or unintended weight loss.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Skin: no rashes or non-healing wounds.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- CKD, stage 3a
- GERD
- Hypothyroidism
- Seasonal allergic rhinitis
- Obesity

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
- loratadine 10 mg as needed
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
NKDA.

FAMILY HISTORY
Father: coronary artery disease, died age 63.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Walks 3 times per week, about 20 minutes.
Works part time as a cashier.

VITALS
BP 118/91 | HR 92 | Temp 98.5 F | Wt 120.8 kg | BMI 37.9 | SpO2 96%

LABS
Date  Test                        Result
2025-12-07  eGFR                        58 mL/min/1.73m2
2025-12-07  Creatinine                  1.06 mg/dL
2026-03-26  eGFR                        49 mL/min/1.73m2
2026-07-16  Hemoglobin A1c              9.6%
2026-07-16  Glucose, fasting            160 mg/dL
2026-07-16  LDL cholesterol             125 mg/dL
2026-07-16  Hemoglobin                  11.5 g/dL

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

ASSESSMENT/PLAN
(Assessment copied from note dated 2026-03-29 and updated where noted.)
1. Diabetes mellitus, type 2: A1c 9.6%, up from 8.2%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. GERD: symptoms controlled on omeprazole. Continue.
3. CKD stage 3a secondary to type 2 diabetes: Last eGFR 49 on 2026-03-26. Continue current renal regimen. Labs before next visit.
4. Obesity, BMI 37.9: discussed nutrition and activity goals; referred to dietitian.
5. Hypothyroid: clinically euthyroid. Continue current dose.
6. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
7. Pneumococcal vaccination up to date. Shingles vaccine series completed.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Reviewed sick-day rules for medications.

Return to clinic in 3 months or sooner as needed.
Total time 42 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Associate, PA-C 2026-07-18 15:53
```

</details>

## 12. FU-0104 — D_gt60

**Label: 0 (does not support E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0104    Age: 61    Sex: F
Date of service: 2026-06-11    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
Patient is a 61-year-old woman returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 21 years ago. Brought meter today; morning values 109-163 mg/dL, no lows. Sleeping reasonably well. Mood is good. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Neurological: no numbness or tingling in the feet; no headaches.
Cardiovascular: no chest pain, palpitations or orthopnea.
Constitutional: denies fever, chills or unintended weight loss.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2023.
Respiratory: no cough or dyspnea on exertion.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Skin: no rashes or non-healing wounds.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease stage 3a
- Obesity
- Osteoarthritis, bilateral knees
- GERD
- Hyperlipidemia

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Appendectomy (1988)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- omeprazole 20 mg daily
- atorvastatin 40 mg nightly
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Father: coronary artery disease, died age 80.
Brother: hyperlipidemia.

SOCIAL HISTORY
Never smoker.
Walks 3 times per week, about 20 minutes.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 135/70 | HR 62 | Temp 97.8 F | Wt 82.9 kg | BMI 32.8 | SpO2 96%

LABS
Date  Test                        Result
2025-11-11  eGFR                        53 mL/min/1.73m2
2025-11-11  Creatinine                  1.17 mg/dL
2026-06-09  eGFR                        >60 mL/min/1.73m2
2026-06-09  Creatinine                  1.01 mg/dL
2026-06-09  Hemoglobin A1c              8.2%
2026-06-09  Glucose, fasting            174 mg/dL
2026-06-09  Urine albumin/creatinine    118 mg/g
2026-06-09  Potassium                   3.9 mmol/L
2026-06-09  Sodium                      140 mmol/L
2026-06-09  LDL cholesterol             79 mg/dL
2026-06-09  Hemoglobin                  13.7 g/dL

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

ASSESSMENT/PLAN
1. T2DM: A1c 8.2% today (improved from 8.6%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
3. Hyperlipidemia: LDL 79 mg/dL. Continue atorvastatin 40 mg.
4. Problem list reviewed: obesity, knee osteoarthritis.
5. Shingles vaccine series completed. Pneumococcal vaccination up to date.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Discussed hypoglycemia recognition and treatment.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-06-11 13:17
```

</details>

## 13. FU-0105 — C4_secondary_dm

**Label: 0 (does not support E11.22).** Secondary diabetes (steroid-induced or after pancreatectomy) is not type 2 (rule R3).

Check:
- [ ] The diabetes is described as steroid-induced or due to pancreatectomy.
- [ ] Nowhere says type 2.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0105    Age: 84    Sex: M
Date of service: 2026-09-10    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 2

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
84-year-old man presents for scheduled follow-up. Steroid-induced diabetes since starting long-term prednisone for polymyalgia rheumatica in 2020. Has been trying to walk 2 times per week. Glucose readings 106-165 mg/dL fasting. No urinary symptoms. No foot ulcers or numbness reported. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Neurological: no numbness or tingling in the feet; no headaches.
Eyes: no blurred vision; last dilated eye exam 2024.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Genitourinary: no dysuria, hematuria or change in urine output.
Constitutional: denies fever, chills or unintended weight loss.

PAST MEDICAL HISTORY / PROBLEM LIST
- Steroid-induced diabetes mellitus
- Chronic kidney disease, stage 4
- Osteoarthritis, bilateral knees
- Hyperlipidemia
- Polymyalgia rheumatica, on long-term prednisone

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- prednisone 10 mg daily (polymyalgia rheumatica)
- glipizide 5 mg daily
- empagliflozin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- atorvastatin 40 mg nightly
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
Brother: hyperlipidemia.
Sister: hypothyroidism.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Alcohol: rare.
Lives with alone. Retired accountant.

VITALS
BP 136/86 | HR 64 | Temp 98.2 F | Wt 82.5 kg | BMI 24.0 | SpO2 95%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2026-09-06  eGFR                        22 mL/min/1.73m2
2026-09-06  Creatinine                  2.81 mg/dL
2026-09-06  Hemoglobin A1c              8.5%
2026-09-06  Glucose, fasting            135 mg/dL
2026-09-06  Urine albumin/creatinine    99 mg/g
2026-09-06  Potassium                   4.7 mmol/L
2026-09-06  Sodium                      138 mmol/L
2026-09-06  LDL cholesterol             88 mg/dL
2026-09-06  Hemoglobin                  12.7 g/dL

PRIOR VISIT SUMMARY (2026-05-23)
(For reference only; not today's assessment.)
Steroid-induced diabetes mellitus: A1c 7.4% at that visit; continued medications.
Chronic kidney disease stage 4: continued losartan.
Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.

ASSESSMENT/PLAN
1. Steroid-induced diabetes mellitus: A1c 8.5% (up from 7.4%). Continue current regimen; reviewed glucose log.
2. Chronic kidney disease stage 4: eGFR 22 (no prior for comparison). Metformin discontinued given renal function. Continue empagliflozin. Referred to nephrology for co-management.
3. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
4. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
5. Influenza vaccine given this season. Shingles vaccine series completed.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Patient verbalized understanding of the plan.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Practitioner, FNP-C 2026-09-10 14:40
```

</details>

## 14. FU-0107 — A_P4_link_in_hpi

**Label: 1 (supports E11.22).** CKD addressed today; the diabetic cause is stated only in the HPI.

Check:
- [ ] The HPI attributes the kidney disease to diabetes.
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0107    Age: 81    Sex: M
Date of service: 2026-03-21    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 10

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
Patient is a 81-year-old man returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 16 years ago. Notes some difficulty with diet recently; fasting sugars 128-175 mg/dL. Kidney function decline has been attributed to his diabetes; no other renal disease identified on workup. Denies chest pain, shortness of breath or leg swelling. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Neurological: no numbness or tingling in the feet; no headaches.
Respiratory: no cough or dyspnea on exertion.
Cardiovascular: no chest pain, palpitations or orthopnea.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Constitutional: denies fever, chills or unintended weight loss.
Eyes: no blurred vision; last dilated eye exam 2023.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Genitourinary: no dysuria, hematuria or change in urine output.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease stage 3a
- Hyperlipidemia
- Hypothyroidism
- Obesity

PAST SURGICAL HISTORY
- Appendectomy (1988)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- atorvastatin 40 mg nightly
- levothyroxine 75 mcg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
No family history of kidney disease reported.
Father: coronary artery disease, died age 67.

SOCIAL HISTORY
Never smoker.
Lives with alone. Retired accountant.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 143/82 | HR 80 | Temp 98.6 F | Wt 108.1 kg | BMI 38.0 | SpO2 96%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2025-11-08  eGFR                        53 mL/min/1.73m2
2025-11-08  Creatinine                  1.17 mg/dL
2026-03-11  eGFR                        49 mL/min/1.73m2
2026-03-11  Hemoglobin A1c              8.6%
2026-03-11  Glucose, fasting            181 mg/dL
2026-03-11  Urine albumin/creatinine    67 mg/g
2026-03-11  Potassium                   5.0 mmol/L
2026-03-11  Sodium                      136 mmol/L
2026-03-11  LDL cholesterol             61 mg/dL
2026-03-11  Hemoglobin                  11.6 g/dL

INTERVAL NOTE - PREVIOUS VISIT 2025-11-11
(For reference only; not today's assessment.)
Diabetes mellitus, type 2: A1c 8.4% at that visit; continued medications.
Chronic kidney disease stage 3a: eGFR 53 at that visit; continued losartan.
HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.

ASSESSMENT/PLAN
1. Diabetes mellitus, type 2: A1c 8.6% today (up from 8.4%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Chronic kidney disease stage 3a: eGFR 49 (stable from 53), albuminuria 67 mg/g. Increased losartan to 100 mg daily. Repeat potassium and creatinine in 2 weeks.
3. Obesity: weight 108.1 kg. Continue lifestyle changes.
4. Hypothyroid: clinically euthyroid. Continue current dose.
5. Hyperlipidemia: LDL 61 mg/dL. Continue atorvastatin 40 mg.
6. Pneumococcal vaccination up to date. Retinal exam due; referral placed.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Reviewed sick-day rules for medications.

Return to clinic in 3 months or sooner as needed.
Total time 44 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-03-21 13:17
```

</details>

## 15. FU-0112 — A_N4_type1

**Label: 0 (does not support E11.22).** Type 1 diabetes, so not E11 (type 2).

Check:
- [ ] The note says type 1 diabetes.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0112    Age: 68    Sex: F
Date of service: 2026-07-08    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Physician, DO (Family Medicine)
Location: Synthetic Primary Care Clinic, Room 5

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
68-year-old woman
--- Page 2 of 3 --- FU-0112 --- printed 2026-07-22 ---
here for a 6-month check-in. Type 1 diabetes since age 20. States adherence to medications is good. Denies hypoglycemic episodes. Sleeping reasonably well. Mood is good. No urinary symptoms. No foot ulcers or numbness reported.

REVIEW OF SYSTEMS
Respiratory: no cough or dyspnea on exertion.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Eyes: no blurred vision; last dilated eye exam 2025.
Constitutional: denies fever, chills or unintended weight loss.
Cardiovascular: no chest pain, palpitations or orthopnea.
Endocrine: no polyuria, polydipsia or heat or cold intol-
erance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 1 diabetes mellitus
- Chronic kidney disease, stage 3b
- Obesity
- Hyperlipidemia

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)

MEDICATIONS
- insulin glargine 22 units nightly and insulin lispro with meals; continuous glucose monitor
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- atorvastatin 40 mg nightly
Med rec done with patient’s pill bottles.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
Brother: hyperlipidemia.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2002; 9 pack-years.
Lives with alone. Retired machinist.
Alcohol: rare.

VITALS
BP 133/85 | HR 80 | Temp 97.8 F | Wt 86.6 kg | BMI 35.4 | SpO2 94%

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

LABS
Date   Test   Result
2026-01-29   eGFR	34 mL/min/1.73m2
2026-01-29  Creatinine 1.82 mg/dL
2026-07-06	eGFR         35 mL/min/1.73m2
2026-07-06	Hemoglobin A1c        9.0%
2026-07-06	Glucose, fasting 183 mg/dL
2026-07-06    Urine albumin/creatinine  293 mg/g
2026-07-06  Potassium        4.2 mmol/L
2026-07-06	Sodium	140 mmol/L
2026-07-06   LDL cholesterol      86 mg/dL
2026-07-06 Hemoglobin     14.0 g/dL

ASSESS-
MENT/PLAN
1. Type 1 diabetes mellitus: A1c 9.0%. Continue basal-bolus insulin; reviewed CGM download, time in range 61%. Endocrinology follow-up in 3 months.
2. CKD stage 3b secondary to type 1 diabetes: Renal function reviewed: eGFR 35, UACR 293 mg/g. Continue losartan; avoid NSAlDs. Nephrology follow-up as scheduled.
3. Obesity, BMI 35.4: discussed nutrition and activity goals; referred to dietitian.
4. Hyperlipidemia: LDL 86 mg/dL. Continue atorvastatin 40 mg.
5. lnfluenza vaccine given this season. Diabetic foot exam comp1eted today.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Encouraged 150 minutes of moderate activity weekly.

Retum to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Physician, DO 2026-07-08 14:03
```

</details>

## 16. FU-0124 — F1_non_acceptable_provider

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but the visit is by a nurse or dietitian only, not an acceptable provider (rule R1).

Check:
- [ ] Header and signature show RN or RD.
- [ ] Otherwise the chart would support E11.22.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0124    Age: 77    Sex: M
Date of service: 2026-04-08    Visit type: Nurse visit, diabetes education, in person
Clinician: Synthetic Nurse, RN (Diabetes Education)
Location: Synthetic Primary Care Clinic, Room 13

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
77-year-old man seen today for routine chronic care. History of type 2 diabetes diagnosed 16 years ago. States adherence to medications is good. Denies hypoglycemic episodes. Appetite stable. Denies nausea or abdominal pain. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Genitourinary: no dysuria, hematuria or change in urine output.
Constitutional: denies fever, chills or unintended weight loss.
Cardiovascular: no chest pain, palpitations or orthopnea.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.
Skin: no rashes or non-healing wounds.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- CKD, stage 3b
- Essential hypertension
- Hyperlipidemia
- Hypothyroidism
- Osteoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- empagliflozin 10 mg daily
- lisinopril 20 mg daily
- atorvastatin 40 mg nightly
- levothyroxine 75 mcg daily
- acetaminophen 650 mg as needed
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Sister: hypothyroidism.
Mother: hypertension.

SOCIAL HISTORY
Former smoker, quit 2002; 30 pack-years.
Alcohol: 1 to 2 drinks per week.
Works part time as a cashier.

VITALS
BP 130/85 | HR 69 | Temp 98.6 F | Wt 73.8 kg | BMI 24.6 | SpO2 95%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date  Test                        Result
2025-12-15  eGFR                        30 mL/min/1.73m2
2025-12-15  Creatinine                  2.06 mg/dL
2026-04-01  eGFR                        36 mL/min/1.73m2
2026-04-01  Creatinine                  1.72 mg/dL
2026-04-01  Hemoglobin A1c              9.0%
2026-04-01  Glucose, fasting            147 mg/dL
2026-04-01  Urine albumin/creatinine    332 mg/g
2026-04-01  Potassium                   4.4 mmol/L
2026-04-01  Sodium                      143 mmol/L
2026-04-01  LDL cholesterol             105 mg/dL
2026-04-01  Hemoglobin                  13.2 g/dL

IMPRESSION AND PLAN
1. Type 2 diabetes mellitus: A1c 9.0% (improved from 9.9%). Reviewed meal plan and carbohydrate counting; medications per provider.
2. Knee osteoarthritis: managed by primary care provider.
3. Chronic kidney disease stage 3b due to type 2 diabetes: eGFR 36 reviewed (up from 30); reinforced low-sodium diet and medication adherence. Provider to review labs.
4. Hyperlipidemia: managed by primary care provider.
5. Hypothyroidism: managed by primary care provider.
6. Hypertension: managed by primary care provider.
7. Diabetic foot exam completed today. Pneumococcal vaccination up to date.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Nurse, RN 2026-04-08 17:18
```

</details>

## 17. FU-0126 — A_N5_uncertain_dx

**Label: 0 (does not support E11.22).** CKD only possible or not yet established.

Check:
- [ ] The CKD wording is 'possible', 'rule out' or 'not yet established'.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0126    Age: 55    Sex: F
Date of service: 2026-05-17    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 6

CHIEF COMPLAINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
55-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 18 years ago. Home glucose log reviewed, fasting values 107-141 mg/dL with occasional post-meal readings above 200. Denies chest pain, shortness of breath or leg swelling. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Cardiovascular: no chest pain, palpitations or orthopnea.
Genitourinary: no dysuria, hematuria or change in urine output.
Neurological: no numbness or tingling in the feet; no headaches.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Skin: no rashes or non-healing wounds.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Hyperlipidemia
- Seasonal allergic rhinitis
- Osteoarthritis, bilateral knees
- Hypothyroidism

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Right knee arthroscopy (2015)

MEDICATIONS
- metformin 1000 mg twice daily
- atorvastatin 40 mg nightly
- loratadine 10 mg as needed
- acetaminophen 650 mg as needed
- levothyroxine 75 mcg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
Brother: hyperlipidemia.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 1995; 25 pack-years.
Walks 5 times per week, about 20 minutes.
Lives with alone. Retired machinist.

VITALS
BP 137/82 | HR 92 | Temp 98.0 F | Wt 56.5 kg | BMI 24.2 | SpO2 94%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2026-01-19  eGFR                        66 mL/min/1.73m2
2026-05-11  eGFR                        55 mL/min/1.73m2
2026-05-11  Hemoglobin A1c              9.3%
2026-05-11  Glucose, fasting            172 mg/dL
2026-05-11  Potassium                   3.8 mmol/L
2026-05-11  Sodium                      139 mmol/L
2026-05-11  LDL cholesterol             122 mg/dL
2026-05-11  Hemoglobin                  14.2 g/dL

ASSESSMENT/PLAN
1. Diabetes mellitus, type 2: A1c 9.3% (up from 8.9%). Medications unchanged; reinforced carbohydrate counting.
2. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
3. Possible chronic kidney disease: eGFR 55 (was 66). Will recheck renal panel in 90 days; diagnosis deferred until repeat testing.
4. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
5. Hypothyroid: clinically euthyroid. Continue current dose.
6. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
7. Shingles vaccine series completed. Diabetic foot exam completed today.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Reviewed sick-day rules for medications.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-05-17 17:10
```

</details>

## 18. FU-0129 — B4_per_last_visit

**Label: 0 (does not support E11.22).** CKD line says only 'per last visit / unchanged from <month>'; today's labs are not mentioned.

Check:
- [ ] No eGFR from the last 30 days anywhere.
- [ ] The CKD line has no current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0129    Age: 70    Sex: M
Date of service: 2026-05-10    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 10

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
70-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 10 years ago. Home glucose log reviewed, fasting values 109-145 mg/dL with occasional post-meal readings above 200. Energy fair. No new complaints today. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Neurological: no numbness or tingling in the feet; no headaches.
Skin: no rashes or non-healing wounds.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Genitourinary: no dysuria, hematuria or change in urine output.
Respiratory: no cough or dyspnea on exertion.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease, stage 3a
- Hypothyroidism
- Obesity
- Hyperlipidemia
- Essential hypertension

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- levothyroxine 75 mcg daily
- atorvastatin 40 mg nightly
- lisinopril 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Mother: hypertension.
Brother: hyperlipidemia.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 1995; 19 pack-years.
Works part time as a consultant.
Walks 4 times per week, about 20 minutes.

VITALS
BP 124/73 | HR 89 | Temp 98.7 F | Wt 91.5 kg | BMI 34.0 | SpO2 97%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2025-09-17  eGFR                        55 mL/min/1.73m2
2025-09-17  Creatinine                  1.12 mg/dL
2026-02-11  eGFR                        47 mL/min/1.73m2
2026-02-11  Creatinine                  1.31 mg/dL
2026-05-08  Hemoglobin A1c              8.8%
2026-05-08  Glucose, fasting            139 mg/dL
2026-05-08  LDL cholesterol             88 mg/dL
2026-05-08  Hemoglobin                  12.9 g/dL

ASSESSMENT/PLAN
(Assessment copied from note dated 2026-02-17 and updated where noted.)
1. T2DM: A1c 8.8%, up from 8.0%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Obesity: weight 91.5 kg. Continue lifestyle changes.
3. Hyperlipidemia: LDL 88 mg/dL. Continue atorvastatin 40 mg.
4. HTN: at goal on current regimen. Continue lisinopril.
5. CKD, stage 3a: Per last visit, stable; unchanged from 02/2026.
6. Hypothyroid: clinically euthyroid. Continue current dose.
7. Shingles vaccine series completed. Retinal exam due; referral placed.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Patient verbalized understanding of the plan.

Return to clinic in 3 months or sooner as needed.
Total time 40 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-05-10 16:56
```

</details>

## 19. FU-0135 — A_N3_labs_only

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

## 20. FU-0136 — C1_dm_untyped

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

## 21. FU-0139 — F3_not_face_to_face

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but it is a chart-review e-consult; the patient was not seen (rule R1).

Check:
- [ ] The header and HPI say the patient was not seen.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0139    Age: 65    Sex: F
Date of service: 2026-04-22    Visit type: Interprofessional e-consult (chart review; patient not seen)
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 11

REASON FOR E-CONSULT
Question from primary care team about diabetes and kidney function management.

HISTORY OF PRESENT ILLNESS
Chart reviewed for 65-year-old woman; patient not seen or examined for this consult. History of type 2 diabetes diagnosed 15 years ago. Glucose log documented at last office visit: fasting 106-153 mg/dL.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- CKD stage 3a
- GERD
- Essential hypertension
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Cholecystectomy (2011)
- Colonoscopy with polypectomy (2021)

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- omeprazole 20 mg daily
- lisinopril 20 mg daily
- loratadine 10 mg as needed
Medication list taken from the chart; not reconciled with the patient.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Father: coronary artery disease, died age 71.
No family history of kidney disease reported.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2009; 20 pack-years.
Works part time as a cashier.
Walks 2 times per week, about 20 minutes.

VITALS
Last recorded in clinic: BP 139/90, weight 66.9 kg (not measured today).

EXAM
Not performed; patient not seen for this e-consult.

LABS
Date  Test                        Result
2026-01-09  eGFR                        59 mL/min/1.73m2
2026-01-09  Creatinine                  1.05 mg/dL
2026-04-20  eGFR                        50 mL/min/1.73m2
2026-04-20  Hemoglobin A1c              8.3%
2026-04-20  Glucose, fasting            135 mg/dL
2026-04-20  Urine albumin/creatinine    125 mg/g
2026-04-20  Potassium                   4.6 mmol/L
2026-04-20  Sodium                      141 mmol/L
2026-04-20  LDL cholesterol             115 mg/dL
2026-04-20  Hemoglobin                  13.8 g/dL

E-CONSULT ASSESSMENT AND RECOMMENDATIONS
1. Type 2 diabetes mellitus: A1c 8.3% (up from 7.5%). Recommend continuing the current regimen.
2. Allergic rhinitis: stable per chart review; no change recommended.
3. CKD stage 3a: Latest eGFR 50 (down from 59), UACR 125 mg/g. Recommend continuing lisinopril and empagliflozin; repeat BMP and UACR in 3 months.
4. Hypertension: stable per chart review; no change recommended.
5. GERD: stable per chart review; no change recommended.

Recommendations sent to the primary care team. Total time spent on chart review: 15 minutes.
Electronically signed: Synthetic Provider, MD 2026-04-22 11:14
```

</details>

## 22. FU-0143 — G1_reviewed_stable

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

## 23. FU-0149 — F3_not_face_to_face

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but it is a chart-review e-consult; the patient was not seen (rule R1).

Check:
- [ ] The header and HPI say the patient was not seen.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0149    Age: 73    Sex: F
Date of service: 2026-02-26    Visit type: Interprofessional e-consult (chart review; patient not seen)
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 8

REASON FOR E-CONSULT
Question from primary care team about diabetes and kidney function management.

HISTORY OF PRESENT ILLNESS
Chart reviewed for 73-year-old woman; patient not seen or examined for this consult. History of type 2 diabetes diagnosed 10 years ago. Glucose log documented at last office visit: fasting 130-152 mg/dL.

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- acetaminophen 650 mg as needed
- loratadine 10 mg as needed
Medication list taken from the chart; not reconciled with the patient.

ALLERGIES
NKDA.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease stage 3a
- GERD
- Obesity
- Osteoarthritis, bilateral knees
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)

FAMILY HISTORY
Father: coronary artery disease, died age 64.
Mother: hypertension.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2011; 22 pack-years.
Alcohol: none.
Walks 4 times per week, about 20 minutes.

VITALS
Last recorded in clinic: BP 135/85, weight 102.5 kg (not measured today).

LABS
Date  Test                        Result
2025-10-14  eGFR                        50 mL/min/1.73m2
2025-10-14  Creatinine                  1.24 mg/dL
2026-02-24  eGFR                        54 mL/min/1.73m2
2026-02-24  Creatinine                  1.14 mg/dL
2026-02-24  Hemoglobin A1c              8.4%
2026-02-24  Glucose, fasting            135 mg/dL
2026-02-24  Urine albumin/creatinine    359 mg/g
2026-02-24  Potassium                   4.6 mmol/L
2026-02-24  Sodium                      137 mmol/L
2026-02-24  LDL cholesterol             79 mg/dL
2026-02-24  Hemoglobin                  13.3 g/dL

EXAM
Not performed; patient not seen for this e-consult.

E-CONSULT ASSESSMENT AND RECOMMENDATIONS
1. Diabetes mellitus, type 2: A1c 8.4% (improved from 9.4%). Recommend continuing the current regimen.
2. Obesity: stable per chart review; no change recommended.
3. Allergic rhinitis: stable per chart review; no change recommended.
4. Diabetic kidney disease, CKD stage 3a: Latest eGFR 54 (stable from 50), UACR 359 mg/g. Recommend continuing losartan and dapagliflozin; repeat BMP and UACR in 3 months.
5. GERD: stable per chart review; no change recommended.
6. Knee osteoarthritis: stable per chart review; no change recommended.

Recommendations sent to the primary care team. Total time spent on chart review: 15 minutes.
Electronically signed: Synthetic Practitioner, FNP-C 2026-02-26 09:51
```

</details>

## 24. FU-0155 — C5_history_of_ckd

**Label: 1 (supports E11.22).** 'History of CKD' in the HPI, and the plan gives CKD a current status and action.

Check:
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0155    Age: 77    Sex: M
Date of service: 2026-07-08    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
77-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 20 years ago. Notes some difficulty with diet recently; fasting sugars 115-141 mg/dL. History of CKD, diagnosed 2016, followed in this clinic. Denies chest pain, shortness of breath or leg swelling. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Constitutional: denies fever, chills or unintended weight loss.
Eyes: no blurred vision; last dilated eye exam 2025.
Skin: no rashes or non-healing wounds.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Neurological: no numbness or tingling in the feet; no headaches.
Respiratory: no cough or dyspnea on exertion.
Cardiovascular: no chest pain, palpitations or orthopnea.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- acetaminophen 650 mg as needed
- lisinopril 20 mg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Codeine (nausea).

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease, stage 3b
- Osteoarthritis, bilateral knees
- Essential hypertension

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)

FAMILY HISTORY
Mother: hypertension.
No family history of kidney disease reported.
Sister: hypothyroidism.

SOCIAL HISTORY
Never smoker.
Walks 4 times per week, about 20 minutes.
Lives with spouse. Retired bus driver.

VITALS
BP 127/79 | HR 63 | Temp 98.1 F | Wt 95.0 kg | BMI 27.7 | SpO2 95%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2025-11-10  eGFR                        44 mL/min/1.73m2
2025-11-10  Creatinine                  1.4 mg/dL
2026-07-01  eGFR                        38 mL/min/1.73m2
2026-07-01  Creatinine                  1.62 mg/dL
2026-07-01  Hemoglobin A1c              9.5%
2026-07-01  Glucose, fasting            160 mg/dL
2026-07-01  Urine albumin/creatinine    213 mg/g
2026-07-01  Potassium                   4.3 mmol/L
2026-07-01  Sodium                      137 mmol/L
2026-07-01  LDL cholesterol             98 mg/dL
2026-07-01  Hemoglobin                  12.5 g/dL

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus: A1c 9.5% today (improved from 10.8%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
3. Hypertension: BP 127/79 today. Continue lisinopril 20 mg daily. Home BP log reviewed.
4. Chronic kidney disease, stage 3b: Labs reviewed with patient, eGFR 38. Continue empagliflozin; metformin dose appropriate for current eGFR. Recheck in 3 to 4 months.
5. Influenza vaccine given this season. Pneumococcal vaccination up to date.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Encouraged 150 minutes of moderate activity weekly.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-07-08 15:40
```

</details>

## 25. FU-0160 — G3_med_change

**Label: 1 (supports E11.22).** Borderline: metformin reduced because of the eGFR counts as treating the kidney disease, even though CKD is not named in that line.

Check:
- [ ] CKD is on the problem list; the diabetes plan reduces metformin because of eGFR. Do you agree this counts as addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0160    Age: 83    Sex: M
Date of service: 2026-05-08    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 5

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
Established patient, 83-year-old man, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 20 years ago. Reports checking glucose a few times a week; fasting readings
--- Page 2 of 3 --- FU-0160 --- printed 2026-05-14 ---
mostly 127-139 mg/dL. Mild bilateral knee sti-
ffness in the mornings, unchanged. Energy fair. No new complaints today.

REVIEW OF SYSTEMS
Constitutional: denies fever, chills or unintended weight loss.
Respiratory: no cough or dyspnea on exertion.
Genitourinary: no dysuria, hematuria or change in urine output.
Cardiovascular: no chest pain, palpitations or orthopnea.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

MEDlCATIONS
- metformin 1000 mg twice daily (dose being reduced today)
- dapagliflozin 10 mg daily
- acetaminophen 650 mg as needed
- lisinopril 20 mg daily
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGlES
NKDA.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease, stage 3b
- Osteoarthritis, bilateral knees
- Essential hypertension
- GERD
- Hypothyroidism

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)

FAMILY HISTORY
Mother: hypertension.
Father: coronary artery disease, died age 71.
Sister: hypothyroidism.

SOCIAL HISTORY
Never smoker.
Works part time as a consultant.
Alcohol: none.

VITALS
BP 120/90 | HR 79 | Temp 98.0 F | Wt 72.9 kg | BMI 24.1 | SpO2 99%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date Test       Result
2026-05-07    eGFR   40 mL/min/1.73m2
2026-05-07	Hemogl-
obin A1c         7.4%
2026-05-07  Glucose, fasting    176 mg/dL
2026-05-07 Urine albumin/creatinine	401 mg/g
2026-05-07    Potassium       4.6 mmol/L
2026-05-07	Sodium	142 mmol/L
2026-05-07	LDL cholesterol   60 mg/dL
2026-05-07 Hemoglobin	12.0 g/dL

IMPRESSI0N AND PLAN
1. Diabetes mellitus, type 2: A1c 7.4% (up from 6.9%). Metformin reduced to 500 mg twice daily because eGFR is now 40 (no prior for comparison).
2. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
3. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
4. Ess-
ential hypertension: BP 120/90. Reinforced low-sodium diet; continue 1isinopril 20 mg.
5. GERD: symptoms controlled on omeprazole. Continue.
6. Pneumococcal vaccination up to date. Diabetic foot exam completed today.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Discussed hypoglycemia recognition and treatment.

Retum to c1inic in 6 months or sooner as needed.
Total time 45 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-05-08 08:36
```

</details>

## 26. FU-0180 — F2_unsigned

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but the note is unsigned or signed without credentials (rule R2).

Check:
- [ ] The note is marked not signed, or the signature has no MD/DO/NP/PA credential.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0180    Age: 66    Sex: M
Date of service: 2026-09-03    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 3

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HISTORY OF PRESENT ILLNESS
66-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 16 years ago. Home glucose log reviewed, fasting values 107-166 mg/dL with occasional post-meal readings above 200. Denies chest pain, shortness of breath or leg swelling. No urinary symptoms. No foot ulcers or numbness reported.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Genitourinary: no dysuria, hematuria or change in urine output.
Constitutional: denies fever, chills or unintended weight loss.
Eyes: no blurred vision; last dilated eye exam 2023.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Skin: no rashes or non-healing wounds.
Cardiovascular: no chest pain, palpitations or orthopnea.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease stage 3a
- GERD
- Osteoarthritis, bilateral knees
- Hypothyroidism
- Obesity

PAST SURGICAL HISTORY
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- acetaminophen 650 mg as needed
- levothyroxine 75 mcg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Sulfa drugs (hives).

FAMILY HISTORY
Brother: hyperlipidemia.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Lives with spouse. Retired bus driver.
Works part time as a librarian.

VITALS
BP 120/89 | HR 67 | Temp 98.7 F | Wt 93.8 kg | BMI 30.6 | SpO2 98%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date  Test                        Result
2026-04-29  eGFR                        54 mL/min/1.73m2
2026-09-03  eGFR                        46 mL/min/1.73m2
2026-09-03  Hemoglobin A1c              7.7%
2026-09-03  Glucose, fasting            148 mg/dL
2026-09-03  Urine albumin/creatinine    415 mg/g
2026-09-03  Potassium                   4.2 mmol/L
2026-09-03  Sodium                      139 mmol/L
2026-09-03  LDL cholesterol             109 mg/dL
2026-09-03  Hemoglobin                  14.2 g/dL

IMPRESSION AND PLAN
1. Diabetes mellitus, type 2: A1c 7.7% today (improved from 9.1%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
3. Obesity: weight 93.8 kg. Continue lifestyle changes.
4. CKD, stage 3a: Renal function reviewed: eGFR 46 (down from 54). Continue losartan and dapagliflozin. Avoid NSAIDs. Nephrology follow-up as scheduled.
5. OA of knees: continue home exercises and acetaminophen PRN.
6. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
7. Pneumococcal vaccination up to date. Influenza vaccine given this season.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Reviewed carbohydrate counting handout.

Return to clinic in 3 months or sooner as needed.
*** NOTE NOT SIGNED - pending clinician signature ***
```

</details>

## 27. FU-0197 — F2_unsigned

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but the note is unsigned or signed without credentials (rule R2).

Check:
- [ ] The note is marked not signed, or the signature has no MD/DO/NP/PA credential.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0197    Age: 63    Sex: M
Date of service: 2026-09-17    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 3

CHIEF COMPLAINT
Follow-up visit; medication refills.

HISTORY OF PRESENT ILLNESS
Patient is a
--- Page 2 of 3 --- FU-0197 --- printed 2026-09-27 ---
63-year-old man returning for follow-up of chronic conditions. History of type 2 diabetes diagnosed 15 years ago. Notes some difficulty with diet recently; fasting sugars 113-160 mg/dL. Denies chest pain, shortness of breath or leg swelling. Sleeping reasonably well. Mood is good.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Skin: no rashes or non-healing wounds.
Constitutional: denies fever, chills or unintended weight loss.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Respiratory: no cough or dyspnea on exertion.
Eyes: no blurred vision; last dilated eye exam 2025.

PAST MEDICAL HIST0RY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD, stage 3b
- Seasonal allergic rhinitis
- GERD

PAST SURGICAL HISTORY
- Cholecystectomy (2011)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- loratadine 10 mg as needed
- omeprazole 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
NKDA.

FAMILY HISTORY
Father: coronary artery disease, died age 75.
No family history of kidney disease reported.
Sister: hypothyroidism.

SOCIAL HISTORY
Never smoker.
A1cohol: 1 to 2 drinks per week.
Works part time as a consultant.

VITALS
BP 126/92 | HR 90 | Temp 98.8 F | Wt 85.4 kg | BMI 25.7 | SpO2 94%

EXAM
General: well app-
earing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date	Test       Result
2026-09-11 eGFR    30 mL/min/1.73m2
2026-09-11 Hemoglobin A1c       7.7%
2026-09-11   Glucose, fasting	168 mg/dL
2026-09-11	Urine albumin/creatinine        102 mg/g
2026-09-11    Potassium        5.0 mmol/L
2026-09-11	Sodium  137 mmol/L
2026-09-11 LDL cholesterol     113 mg/dL
2026-09-11	Hemoglobin	14.7 g/dL

IMPRESSION AND PLAN
1. Type 2 diabetes mellitus: A1c 7.7% today (up from 7.1%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
3. CKD stage 3b: eGFR 30 (no prior for comparison), a1buminuria 102 mg/g. lncreased losartan to 100 mg daily. Repeat potassium and creatinine in 2 weeks.
4. Problem list reviewed: GERD.
5. Diabetic foot exam completed today. Shingles vaccine series completed.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Patient verbalized understanding of the plan.

Retum to clinic in 6 months or sooner as needed.
Total time 34 minutes, more than half in counseling and care coord-
ination.
*** NOTE NOT SIGNED - pending clinician sig-
nature ***
```

</details>

## 28. FU-0225 — B3_copy_plus_new

**Label: 1 (supports E11.22).** Copied (stale) CKD line, followed by a new line from today with today's eGFR.

Check:
- [ ] The CKD item has an 'Update today' or 'Addendum' sentence with today's eGFR.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0225    Age: 57    Sex: F
Date of service: 2026-06-03    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 13

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
57-year-old woman here for a 4-month check-in. History of type 2 diabetes diagnosed 14 years ago. Has been trying to walk 2 times per week. Glucose readings 121-140 mg/dL fasting. Appetite stable. Denies nausea or abdominal pain. No urinary symptoms. No foot ulcers or numbness reported.

REVIEW OF SYSTEMS
Respiratory: no cough or dyspnea on exertion.
Eyes: no blurred vision; last dilated eye exam 2023.
Skin: no rashes or non-healing wounds.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Cardiovascular: no chest pain, palpitations or orthopnea.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.

PAST MEDICAL HISTORY / PROBLEM LIST
- T2DM, on oral agents
- Chronic kidney disease, stage 3b
- Hypothyroidism
- Hyperlipidemia
- Obesity
- GERD

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Appendectomy (1988)
- Tonsillectomy (childhood)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- levothyroxine 75 mcg daily
- atorvastatin 40 mg nightly
- omeprazole 20 mg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Mother: hypertension.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 1995; 18 pack-years.
Works part time as a librarian.
Walks 2 times per week, about 20 minutes.

VITALS
BP 140/91 | HR 65 | Temp 98.6 F | Wt 89.2 kg | BMI 34.9 | SpO2 98%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date  Test                        Result
2025-11-30  eGFR                        32 mL/min/1.73m2
2025-11-30  Creatinine                  1.93 mg/dL
2026-06-03  eGFR                        31 mL/min/1.73m2
2026-06-03  Creatinine                  1.99 mg/dL
2026-06-03  Hemoglobin A1c              7.9%
2026-06-03  Glucose, fasting            124 mg/dL
2026-06-03  Urine albumin/creatinine    406 mg/g
2026-06-03  Potassium                   4.3 mmol/L
2026-06-03  Sodium                      142 mmol/L
2026-06-03  LDL cholesterol             78 mg/dL
2026-06-03  Hemoglobin                  14.0 g/dL

ASSESSMENT AND PLAN
(Assessment copied from note dated 2026-02-04 and updated where noted.)
1. Diabetes mellitus, type 2: A1c 7.9%, improved from 8.9%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
3. GERD: symptoms controlled on omeprazole. Continue.
4. Obesity: weight 89.2 kg. Continue lifestyle changes.
5. CKD stage 3b secondary to type 2 diabetes: Last eGFR 32 on 2025-11-30. Continue current renal regimen. Labs before next visit. Addendum 2026-06-03: eGFR 31 today, stable from 32. No change to losartan.
6. Also on problem list: hyperlipidemia.
7. Dental visit within the past year. Retinal exam due; referral placed.

PATIENT EDUCATION
Reviewed sick-day rules for medications.
Reviewed carbohydrate counting handout.

Return to clinic in 3 months or sooner as needed.
Total time 42 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Practitioner, FNP-C 2026-06-03 09:12
```

</details>

## 29. FU-0251 — B5_interval_labs

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

## 30. FU-0256 — E3_link_in_prior_visit

**Label: 1 (supports E11.22).** The diabetic cause appears only in a dated prior-visit section; today's plan addresses CKD without another cause.

Check:
- [ ] The prior-visit section links CKD to diabetes; today's plan does not name another cause.
- [ ] Today's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0256    Age: 72    Sex: M
Date of service: 2026-04-13    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 6

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
72-year-old man here for a 3-month check-in. History of type 2 diabetes diagnosed 6 years ago. Reports checking glucose daily; fasting readings mostly 105-137 mg/dL. Energy fair. No new complaints today. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Cardiovascular: no chest pain, palpitations or orthopnea.
Eyes: no blurred vision; last dilated eye exam 2024.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Musculoskeletal: chronic knee stiffness, otherwise negative.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease stage 3b
- Hyperlipidemia
- Seasonal allergic rhinitis

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Right knee arthroscopy (2015)

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- losartan 50 mg daily
- atorvastatin 40 mg nightly
- loratadine 10 mg as needed
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
No family history of kidney disease reported.
Sister: hypothyroidism.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2002; 11 pack-years.
Works part time as a consultant.
Lives with alone. Retired bus driver.

VITALS
BP 125/86 | HR 75 | Temp 98.4 F | Wt 81.1 kg | BMI 27.3 | SpO2 97%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2025-10-18  eGFR                        33 mL/min/1.73m2
2025-10-18  Creatinine                  1.87 mg/dL
2026-04-10  eGFR                        36 mL/min/1.73m2
2026-04-10  Creatinine                  1.72 mg/dL
2026-04-10  Hemoglobin A1c              9.0%
2026-04-10  Glucose, fasting            185 mg/dL
2026-04-10  Urine albumin/creatinine    229 mg/g
2026-04-10  Potassium                   3.9 mmol/L
2026-04-10  Sodium                      139 mmol/L
2026-04-10  LDL cholesterol             95 mg/dL
2026-04-10  Hemoglobin                  14.4 g/dL

PRIOR VISIT SUMMARY (2025-10-24)
(For reference only; not today's assessment.)
Diabetes mellitus, type 2: A1c 9.7% at that visit; continued medications.
Diabetic chronic kidney disease, stage 3b: eGFR 33 at that visit; continued losartan.
HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.

ASSESSMENT/PLAN
1. Diabetes mellitus, type 2: A1c 9.0%, improved from 9.7%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Chronic kidney disease stage 3b: eGFR 36 (stable from 33), albuminuria 229 mg/g. Increased losartan to 100 mg daily. Repeat potassium and creatinine in 2 weeks.
3. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
4. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
5. Pneumococcal vaccination up to date. Dental visit within the past year.

PATIENT EDUCATION
Discussed hypoglycemia recognition and treatment.
Patient verbalized understanding of the plan.

Return to clinic in 6 months or sooner as needed.
Total time 42 minutes, more than half in counseling and care coordination.
Electronically signed: Synthetic Provider, MD 2026-04-13 16:44
```

</details>

## 31. FU-0260 — D_gap91_neg

**Label: 0 (does not support E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0260    Age: 67    Sex: F
Date of service: 2026-03-19    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 4

CHIEF COMPLAINT
Follow-up of diabetes and chronic conditions.

HlSTORY OF PRESENT ILLNESS
67-year-old woman here for a 6-month check-in. History of type 2 diabetes diagnosed 11 years ago. Reports checking
--- Page 2 of 3 --- FU-0260 --- printed 2026-03-28 ---
glucose a few times a week; fasting readings mostly 117-152 mg/dL. Energy fair. No new complaints today. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Eyes: no blurred vision; last dilated eye exam 2024.
Skin: no rashes or non-healing wounds.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Neurological: no numbness or tingling in the feet; no headaches.
Constitutional: denies fever, chills or unintended weight loss.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflo-
zin 10 mg daily
- losartan 50 mg daily
- acetaminophen 650 mg as needed
- loratadine 10 mg as needed
- atorvastatin 40 mg nightly
Med rec done with patient’s pill bottles.

ALLERGIES
NKDA.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease stage 3a
- Osteoarthritis, bilateral knees
- Obesity
- Seasonal allergic rhinitis
- Hyperlipidemia

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Tonsillectomy (childhood)
- Appendectomy (1988)

FAMILY HISTORY
Sister: hypothyroidism.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Walks 3 times per week, about 20 minutes.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 138/81 | HR 67 | Temp 98.7 F | Wt 114.5 kg | BMI 37.9 | SpO2 96%

LABS
Date	Test	Result
2025-12-14 eGFR   54 mL/min/1.73m2
2025-12-14  Cre-
atinine	1.14 mg/dL
2026-03-15 eGFR       51 mL/min/1.73m2
2026-03-15  Hemoglobin A1c   6.6%
2026-03-15	Glucose, fasting   131 mg/dL
2026-03-15    Urine albumin/creatinine  191 mg/g
2026-03-15  Potassium	4.6 mmol/L
2026-03-15    Sodium 141 mmol/L
2026-03-15	LDL cholesterol       115 mg/dL
2026-03-15 Hemoglobin     13.3 g/dL

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

ASSESSMENT AND PLAN
1. Type 2 diabetes mellitus: A1c 6.6% (up from 6.0%). Medications unchanged; reinforced carbohydrate counting.
2. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
3. Allergic rhinitis: seasonal symptoms; continue 1oratadine PRN.
4. 0besity, BMI 37.9: discussed nutrition and activity goa1s; referred to dietitian.
5. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
6. Retinal exam due; referral placed. Influenza vaccine given this season.

PATIENT EDUCATION
Reviewed sick-day ru1es for medications.
Reviewed carbohydrate counting handout.

Retum to c1inic in 3 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-03-19 08:11
```

</details>

## 32. FU-0265 — C6_ckd_ruled_out

**Label: 0 (does not support E11.22).** CKD removed from the problem list: repeat testing shows normal kidney function.

Check:
- [ ] The plan says the patient does not have CKD / CKD ruled out.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0265    Age: 59    Sex: M
Date of service: 2026-02-03    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 10

CHIEF COMPLAINT
3-month follow-up, review of labs.

HISTORY OF PRESENT ILLNESS
59-year-old man here for a 4-month check-in. History of type 2 diabetes diagnosed 18 years ago. Reports checking glucose a few times a week; fasting readings mostly 117-167 mg/dL. Sleeping reasonably well. Mood is good. Appetite stable. Denies nausea or abdominal pain.

REVIEW OF SYSTEMS
Cardiovascular: no chest pain, palpitations or orthopnea.
Neurological: no numbness or tingling in the feet; no headaches.
Respiratory: no cough or dyspnea on exertion.
Skin: no rashes or non-healing wounds.
Genit-
ourinary: no dysuria, hematuria or change in urine output.
Constitutional: denies fever, chills or unintended weight loss.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Psychi-
atric: mood stable; sleeping 6 to 7 hours a night.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

MEDICATIONS
- metformin 1000 mg twice daily
- lisinopril 20 mg daily
- acetaminophen 650 mg as needed
- levothyroxine 75 mcg daily
Medication reconciliation completed; no changes other than those noted in the plan.

ALLERGIES
No known drug allergies.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease (entered 2024) – see assessment
- Essential hypertension
- Osteoarthritis, bilateral knees
- Hypothyroidism
- Obesity

PAST SURGlCAL HISTORY
- Right knee arthroscopy (2015)

FAMILY HISTORY
Sister: hypothyroidism.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2014; 25 pack-years.
Lives with alone. Retired accountant.
Walks 3 times per week, about 20 minutes.

VITALS
BP 144/84 | HR 82 | Temp 97.7 F | Wt 103.8 kg | BMI 36.0 | SpO2 96%

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

LABS
Date   Test	Result
2025-02-10 eGFR	52 mL/min/1.73m2
2025-09-27   eGFR	75 mL/min/1.73m2
2025-09-27	Creatinine	0.82 mg/dL
2026-02-02  eGFR    80 mL/min/1.73m2
2026-02-02    Creatinine	0.77 mg/dL
2026-02-02 Hemoglobin A1c         7.2%
2026-02-02	Glucose, fasting       165 mg/dL
2026-02-02    Potassium      4.9 mmol/L
2026-02-02	Sodium  140 mmol/L
2026-02-02	LDL cholesterol	68 mg/dL
2026-02-02    Hemoglobin    11.3 g/dL

ASSESSMENT/PLAN
1. T2DM: A1c 7.2% today (up from 6.6%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. 0besity: weight 103.8 kg. Continue lifestyle changes.
3. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
4. Hypertension: BP 144/84 today. Continue lisinopril 20 mg daily. Home BP log reviewed.
5. Chronic kidney disease on
--- Page 2 of 3 --- FU-0265 --- printed 2026-02-05 ---
problem list, removed today: eGFR 75 and 80 on repeat testing over 6 months, urine albumin normal; prior eGFR 52 (2025-02-10) was during an acute illness. Chronic kidney disease ruled out.
6. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAlDs.
7. Retinal exam due; referral placed. Influenza vaccine given this season.

PATIENT EDUCA-
TI0N
Reviewed carbohydrate counting handout.
Encouraged 150 minutes of moderate activity week1y.

Retum to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-02-03 08:27
```

</details>

## 33. FU-0266 — C1_dm_untyped

**Label: 1 (supports E11.22).** Diabetes with no type documented: ICD-10-CM defaults to type 2 (E11). CKD addressed today.

Check:
- [ ] No diabetes type anywhere ('type 1', 'type 2', 'T2DM' absent).
- [ ] The plan's CKD line has a current status or action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0266    Age: 58    Sex: M
Date of service: 2026-03-24    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 4

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
Established patient, 58-year-old man, presenting for chronic disease follow-up. History of diabetes diagnosed 21 years ago, managed with metformin. Reports checking glucose daily; fasting readings mostly 116-169 mg/dL. Denies chest pain, shortness of breath or leg swelling. Energy fair. No
--- Page 2 of 3 --- FU-0266 --- printed 2026-03-26 ---
new complaints today.

REVIEW OF SYSTEMS
Musculoskeletal: chronic knee stiffness, otherwise negative.
Cardiovascular: no chest pain, palpitations or orthopnea.
Skin: no rashes or non-healing wounds.
Eyes: no blurred vision; last dilated eye exam 2025.
Constitutional: denies fever, chills or unintended weight loss.
Genitourinary: no dysuria, hematuria or change in urine output.
Respiratory: no cough or dyspnea on exertion.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- DM, on metformin
- Chronic kidney disease stage 3a
- GERD
- Hypothyroidism
- Hyperlipidemia
- 0steoarthritis, bilateral knees

PAST SURGICAL HISTORY
- Colonoscopy with polypectomy (2021)
- Right knee arthroscopy (2015)
- Cholecystectomy (2011)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
- atorvastatin 40 mg nightly
- acetaminophen 650 mg as needed
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
Penicillin (rash).

FAMILY HISTORY
Father: coronary artery disease, died age 63.
Mother: hypertension.
Brother: hyperlipidemia.

SOCIAL HISTORY
Former smoker, quit 2011; 22 pack-years.
Works part time as a 1ibrarian.
Lives with spouse. Retired machinist.

VITALS
BP 125/91 | HR 91 | Temp 98.3 F | Wt 83.9 kg | BMI 29.4 | SpO2 98%

LABS
Date	Test	Result
2025-10-16  eGFR     47 mL/min/1.73m2
2025-10-16	Creatinine     1.31 mg/dL
2026-03-23    eGFR        46 mL/min/1.73m2
2026-03-23 Hemoglobin A1c	8.1%
2026-03-23 Glucose, fasting         186 mg/dL
2026-03-23	Urine albumin/creatinine	367 mg/g
2026-03-23	Potassium	4.4 mmol/L
2026-03-23	Sodium  136 mmol/L
2026-03-23	LDL cholesterol        101 mg/dL
2026-03-23  Hemoglobin	13.9 g/dL

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

IMPRESSI0N AND PLAN
1. DM: A1c 8.1%, improved from 9.3%. Reviewed diet and activity. Continue medications. Retina1 exam due.
2. Diabetic chronic kidney disease, stage 3a: eGFR 46, UACR 367 mg/g. On empagliflozin and losartan; counseled on avoiding nephrotoxins. Repeat labs in 3 months.
3. HLD: tolerating statin. Continue atorvastatin; recheck lipids in 12 months.
4. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
5. Knee osteoarthritis: stable. Acetaminophen as needed; avoid NSAIDs.
6. GERD: symptoms controlled on omeprazole. Continue.
7. Diabetic foot exam comple-
ted today. Retinal exam due; referral placed.

PATIENT EDUCATION
Patient verba1ized understanding of the plan.
Reviewed sick-day rules for medications.

Retum to clinic in 4 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-03-24 12:42
```

</details>

## 34. FU-0270 — D_sentence_pos

**Label: 1 (supports E11.22).** Lab edge case for Q2; the label comes from the rest of the chart (CKD addressed today -> 1; CKD on the problem list only -> 0).

Check:
- [ ] Label 1 only if the plan has a CKD line with a current status or action.
- [ ] The eGFR detail matches the scenario (exact 60, '>60', the day gap, undated result, creatinine only, or results in a sentence).

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0270    Age: 84    Sex: M
Date of service: 2026-02-13    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 4

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
Established patient, 84-year-old man, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 7 years ago. Reports checking glucose daily; fasting readings mostly 111-139 mg/dL. Recent kidney labs: eGFR was 55 on 2025-07-06 and 56 on 2026-02-13. No polyuria or polydipsia. No visual changes. Mild bilateral knee stiffness in the mornings, unchanged.

REVIEW OF SYSTEMS
Musculoskeletal: chronic knee stiffness, otherwise negative.
Cardiovascular: no chest pain, palpitations or orthopnea.
Constitutional: denies fever, chills or unintended weight loss.
Neurological: no numbness or tingling in the feet; no headaches.
Genitourinary: no dysuria, hematuria or change in urine output.
Skin: no rashes or non-healing wounds.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease stage 3a
- Obesity
- GERD
- Hypothyroidism

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

FAMILY HISTORY
No family history of kidney disease reported.
Sister: hypothyroidism.

SOCIAL HISTORY
Former smoker, quit 1996; 11 pack-years.
Lives with alone. Retired bus driver.
Alcohol: 1 to 2 drinks per week.

VITALS
BP 124/79 | HR 87 | Temp 98.3 F | Wt 101.8 kg | BMI 34.5 | SpO2 94%

EXAM
General: well appearing, no acute distress.
CV: regular rate and rhythm, no murmur.
Lungs: clear bilaterally.
Ext: no edema.

LABS
Date  Test                        Result
2025-07-06  Creatinine                  1.12 mg/dL
2026-02-13  Hemoglobin A1c              7.9%
2026-02-13  Glucose, fasting            187 mg/dL
2026-02-13  Urine albumin/creatinine    299 mg/g
2026-02-13  Potassium                   4.9 mmol/L
2026-02-13  Sodium                      141 mmol/L
2026-02-13  LDL cholesterol             101 mg/dL
2026-02-13  Hemoglobin                  14.3 g/dL

IMPRESSION AND PLAN
1. Diabetes mellitus, type 2: A1c 7.9% today (improved from 8.6%). Continue current regimen. Foot exam done; annual eye exam reminder given.
2. GERD: symptoms controlled on omeprazole. Continue.
3. Hypothyroid: clinically euthyroid. Continue current dose.
4. Obesity: weight 101.8 kg. Continue lifestyle changes.
5. CKD stage 3a: Labs reviewed with patient, eGFR 56. Continue dapagliflozin; metformin dose appropriate for current eGFR. Recheck in 3 to 4 months.
6. Diabetic foot exam completed today. Dental visit within the past year.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Reviewed carbohydrate counting handout.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Practitioner, FNP-C 2026-02-13 09:37
```

</details>

## 35. FU-0288 — F3_not_face_to_face

**Label: 0 (does not support E11.22).** Stress test: everything looks supported, but it is a chart-review e-consult; the patient was not seen (rule R1).

Check:
- [ ] The header and HPI say the patient was not seen.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0288    Age: 77    Sex: M
Date of service: 2026-04-16    Visit type: Interprofessional e-consult (chart review; patient not seen)
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 14

REASON FOR E-CONSULT
Chart review requested for chronic disease management; patient not present.

HISTORY OF PRESENT ILLNESS
Chart reviewed for 77-year-old man; patient not seen or examined for this consult. History of type 2 diabetes diagnosed 10 years ago. Glucose log documented at last office visit: fasting 129-160 mg/dL.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD stage 3a
- Obesity
- Seasonal allergic rhinitis
- Essential hypertension

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Tonsillectomy (childhood)
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 1000 mg twice daily
- dapagliflozin 10 mg daily
- loratadine 10 mg as needed
- lisinopril 20 mg daily
Medication list taken from the chart; not reconciled with the patient.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Sister: hypothyroidism.
Brother: hyperlipidemia.
Father: coronary artery disease, died age 79.

SOCIAL HISTORY
Never smoker.
Walks 2 times per week, about 20 minutes.
Works part time as a consultant.

VITALS
Last recorded in clinic: BP 130/89, weight 109.2 kg (not measured today).

LABS
Date  Test                        Result
2025-10-05  eGFR                        56 mL/min/1.73m2
2025-10-05  Creatinine                  1.1 mg/dL
2026-04-09  eGFR                        58 mL/min/1.73m2
2026-04-09  Creatinine                  1.06 mg/dL
2026-04-09  Hemoglobin A1c              7.1%
2026-04-09  Glucose, fasting            170 mg/dL
2026-04-09  Urine albumin/creatinine    273 mg/g
2026-04-09  Potassium                   5.0 mmol/L
2026-04-09  Sodium                      139 mmol/L
2026-04-09  LDL cholesterol             125 mg/dL
2026-04-09  Hemoglobin                  13.8 g/dL

EXAM
Not performed; patient not seen for this e-consult.

E-CONSULT ASSESSMENT AND RECOMMENDATIONS
1. Type 2 diabetes mellitus: A1c 7.1% (improved from 7.9%). Recommend continuing the current regimen.
2. Chronic kidney disease, stage 3a: Latest eGFR 58 (stable from 56), UACR 273 mg/g. Recommend continuing lisinopril and dapagliflozin; repeat BMP and UACR in 3 months.
3. Obesity: stable per chart review; no change recommended.
4. Allergic rhinitis: stable per chart review; no change recommended.
5. Hypertension: stable per chart review; no change recommended.

Recommendations sent to the primary care team. Total time spent on chart review: 15 minutes.
Electronically signed: Synthetic Practitioner, FNP-C 2026-04-16 09:18
```

</details>

## 36. FU-0290 — G5_minimal

**Label: 1 (supports E11.22).** Borderline: 'CKD 3a, stable on losartan' as its own line counts as status plus treatment.

Check:
- [ ] Do you agree this minimal line counts as addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0290    Age: 76    Sex: F
Date of service: 2026-02-08    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synthetic Primary Care Clinic, Room 9

CHIEF COMPLAINT
Routine diabetes follow-up.

HISTORY OF PRESENT ILLNESS
76-year-old woman seen today for routine chronic care. History of type 2 diabetes diagnosed 8 years ago. Reports checking glucose daily; fasting readings mostly 130-150 mg/dL. Mild bilateral knee stiffness in the mornings, unchanged. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Constitutional: denies fever, chills or unintended weight loss.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Psychiatric: mood stable; sleeping 6 to 7 hours a night.
Respiratory: no cough or dyspnea on exertion.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Neurological: no numbness or tingling in the feet; no headaches.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease stage 3a
- Essential hypertension
- GERD

PAST SURGICAL HISTORY
- Cataract extraction, left eye (2022)

MEDICATIONS
- metformin 1000 mg twice daily
- semaglutide 0.5 mg weekly
- empagliflozin 10 mg daily
- lisinopril 20 mg daily
- omeprazole 20 mg daily
Med rec done with patient's pill bottles.

ALLERGIES
Codeine (nausea).

FAMILY HISTORY
Sister: hypothyroidism.
Father: coronary artery disease, died age 74.

SOCIAL HISTORY
Never smoker.
Lives with daughter. Retired machinist.
Walks 3 times per week, about 20 minutes.

VITALS
BP 135/87 | HR 82 | Temp 98.5 F | Wt 57.2 kg | BMI 24.3 | SpO2 96%

LABS
Date  Test                        Result
2025-08-26  eGFR                        47 mL/min/1.73m2
2025-08-26  Creatinine                  1.31 mg/dL
2026-02-04  eGFR                        51 mL/min/1.73m2
2026-02-04  Creatinine                  1.21 mg/dL
2026-02-04  Hemoglobin A1c              8.1%
2026-02-04  Glucose, fasting            165 mg/dL
2026-02-04  Urine albumin/creatinine    300 mg/g
2026-02-04  Potassium                   4.1 mmol/L
2026-02-04  Sodium                      143 mmol/L
2026-02-04  LDL cholesterol             75 mg/dL
2026-02-04  Hemoglobin                  13.4 g/dL

EXAM
General: comfortable.
Cardiac: regular, no gallop.
Pulmonary: no wheezes or crackles.
Skin: warm and dry.
Ext: no pedal edema.

PRIOR VISIT SUMMARY (2025-08-27)
(For reference only; not today's assessment.)
T2DM: A1c 7.2% at that visit; continued medications.
CKD 3a: eGFR 47 at that visit; continued lisinopril.
HTN: at goal on current regimen. Continue lisinopril.

ASSESSMENT AND PLAN
1. T2DM: A1c 8.1% (up from 7.2%). Medications unchanged; reinforced carbohydrate counting.
2. GERD: symptoms controlled on omeprazole. Continue.
3. CKD 3a, stable on lisinopril; no changes.
4. Essential hypertension: BP 135/87. Reinforced low-sodium diet; continue lisinopril 20 mg.
5. Dental visit within the past year. Pneumococcal vaccination up to date.

PATIENT EDUCATION
Encouraged 150 minutes of moderate activity weekly.
Patient verbalized understanding of the plan.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Provider, MD 2026-02-08 16:56
```

</details>

## 37. FU-0291 — A_P3_link_no_stage

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

## 38. FU-0295 — G2_see_nephrology

**Label: 0 (does not support E11.22).** Borderline: 'see nephrology note' gives no status or action today.

Check:
- [ ] The plan's CKD line only points to nephrology. Do you agree this is not addressed?

<details><summary>Note text</summary>

```
SYNTHETIC RECORD - FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0295    Age: 58    Sex: M
Date of service: 2026-08-31    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 5

CHIEF COMPLAINT
Here to go over recent blood work.

HISTORY OF PRESENT ILLNESS
58-year-old man presents for scheduled follow-up. History of type 2 diabetes diagnosed 13 years ago. States adherence to medications is good. Denies hypoglycemic episodes. Appetite stable. Denies nausea or abdominal pain. No polyuria or polydipsia. No visual changes.

REVIEW OF SYSTEMS
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Cardiovascular: no chest pain, palpitations or orthopnea.
Eyes: no blurred vision; last dilated eye exam 2023.
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Genitourinary: no dysuria, hematuria or change in urine output.

MEDICATIONS
- metformin 500 mg twice daily (renally dosed)
- dapagliflozin 10 mg daily
- losartan 50 mg daily
- atorvastatin 40 mg nightly
- omeprazole 20 mg daily
- levothyroxine 75 mcg daily
Med rec done with patient's pill bottles.

ALLERGIES
No known drug allergies.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- CKD stage 3b
- Obesity
- Hyperlipidemia
- GERD
- Hypothyroidism

PAST SURGICAL HISTORY
- Right knee arthroscopy (2015)

FAMILY HISTORY
Father: coronary artery disease, died age 80.
Brother: hyperlipidemia.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Lives with alone. Retired accountant.
Works part time as a librarian.

VITALS
BP 132/69 | HR 62 | Temp 98.7 F | Wt 96.9 kg | BMI 36.6 | SpO2 98%

LABS
Date  Test                        Result
2026-04-03  eGFR                        43 mL/min/1.73m2
2026-04-03  Creatinine                  1.44 mg/dL
2026-08-22  eGFR                        30 mL/min/1.73m2
2026-08-22  Creatinine                  2.06 mg/dL
2026-08-22  Hemoglobin A1c              7.3%
2026-08-22  Glucose, fasting            129 mg/dL
2026-08-22  Urine albumin/creatinine    295 mg/g
2026-08-22  Potassium                   4.6 mmol/L
2026-08-22  Sodium                      138 mmol/L
2026-08-22  LDL cholesterol             113 mg/dL
2026-08-22  Hemoglobin                  12.0 g/dL

EXAM
Gen: NAD.
CV: RRR, normal S1/S2.
Resp: clear to auscultation.
Abd: soft, nontender.
Ext: no edema; feet without lesions.

ASSESSMENT/PLAN
1. Diabetes mellitus, type 2: A1c 7.3%, improved from 8.7%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. CKD stage 3b: Per nephrology; see their note.
3. Obesity: weight 96.9 kg. Continue lifestyle changes.
4. Hyperlipidemia: LDL 113 mg/dL. Continue atorvastatin 40 mg.
5. GERD: symptoms controlled on omeprazole. Continue.
6. Hypothyroidism: TSH within range. Continue levothyroxine 75 mcg.
7. Influenza vaccine given this season. Colorectal cancer screening up to date.

PATIENT EDUCATION
Patient verbalized understanding of the plan.
Discussed hypoglycemia recognition and treatment.

Return to clinic in 3 months or sooner as needed.
Electronically signed: Synthetic Practitioner, FNP-C 2026-08-31 11:03
```

</details>

## 39. FU-0298 — B1_copy_current

**Label: 1 (supports E11.22).** Copied plan, but the CKD line cites today's eGFR with today's date and a current action.

Check:
- [ ] Copy-forward marker present.
- [ ] CKD line: today's eGFR (dated the visit day) and an action.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0298    Age: 60    Sex: M
Date of service: 2026-01-27    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Provider, MD (Internal Medicine)
Location: Synt-
hetic Primary Care Clinic, Room 7

CHIEF COMPLAINT
Chronic disease manage-
ment visit.

HISTORY OF PRESENT ILLNESS
Established patient, 60-year-old man, presenting for chronic disease follow-up. History of type 2 diabetes diagnosed 7 years ago. Reports checking glucose daily; fasting readings mostly 129-150 mg/dL. Mild bilateral knee stiffness in the mornings, unchanged. Denies chest pain, shortness of breath or leg swelling.

REVIEW OF SYSTEMS
Endocrine: no polyuria, polydipsia or heat or cold intolerance.
Neurological: no numbness or tingling in the feet; no headaches.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Skin: no rashes or non-healing wounds.
Constitutional: denies fever, chills or unintended weight loss.
Musculoskeletal: chronic knee stiffness, otherwise negative.
Eyes: no blurred vision; last dilated eye exam 2023.

MEDlCATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- lisinopril 20 mg daily
- loratadine 10 mg as needed
- omeprazole 20 mg daily
Medications reviewed with patient and pharmacy list; list above is current.

ALLERGIES
No known drug allergies.

PAST MEDICAL HISTORY / PROBLEM LIST
- Diabetes mellitus type 2
- Chronic kidney disease, stage 3a
- Essential hypertension
- Seasonal allergic rhinitis
- GERD

PAST SURGICAL HISTORY
- Cholecystectomy (2011)
- Tonsillectomy (childhood)

FAMILY HISTORY
Mother: hypertension.
Sister: hypothyroidism.
No family history of kidney disease reported.

SOCIAL HISTORY
Never smoker.
Walks 2 times per week, about 20 minutes.
Works part time as a librarian.

VITALS
BP 135/91 | HR 81 | Temp 98.7 F | Wt 91.9 kg | BMI 29.4 | SpO2 94%

LABS
Date    Test    Result
2025-09-12	eGFR       46 mL/min/1.73m2
2025-09-12	Creatinine      1.34 mg/dL
2026-01-27 eGFR	50 mL/min/1.73m2
2026-01-27  Hemog1obin A1c	7.3%
2026-01-27  Glucose, fasting  113 mg/dL
2026-01-27	Urine albumin/creatinine     277 mg/g
2026-01-27 Potassium	4.3 mmol/L
2026-01-27 Sodium       140 mmol/L
2026-01-27 LDL cholesterol	73 mg/dL
2026-01-27 Hemoglobin    12.0 g/dL

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

ASSESSMENT/PLAN
(Plan unchanged from visit of 2025-08-09.)
1. T2DM: A1c 7.3%, up from 7.1%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. HTN: at goal on current regimen. Continue lisinopril.
3. Gastroesophageal reflux: stable; discussed trial of dose reduction at next visit.
4. Chronic kidney disease stage 3a due to type 2 diabetes: eGFR 50 today (2026-01-27), stable from 46. Continue empagliflozin; recheck BMP in 3 months.
5. Allergic rhinitis: seasonal symptoms; continue loratadine PRN.
6. Diabetic foot exam completed today. Pneumococcal vaccination up to date.

PATlENT EDUCATION
Reviewed sick-day ru1es for medications.
Patient verbalized understanding of the plan.

Return to clinic in 4 months or sooner as needed.
Total time 37 minutes, more than half in counseling and care coordination.
--- Page 2 of 3 --- FU-0298 --- printed 2026-02-03 ---
Electronically signed: Synthetic Provider, MD 2026-01-27 13:29
```

</details>

## 40. FU-0300 — B2_copy_stale

**Label: 0 (does not support E11.22).** Plan copied from a prior visit; the CKD line refers only to an old eGFR and the old plan; nothing current.

Check:
- [ ] The CKD line's eGFR is dated months before the visit.
- [ ] No eGFR from the last 30 days anywhere in the note.
- [ ] No other CKD status or action today.

<details><summary>Note text</summary>

```
SYNTHETIC RECORD – FICTIONAL PATIENT, FOR RESEARCH TESTING ONLY
Patient ID: FU-0300    Age: 66    Sex: F
Date of service: 2026-07-03    Visit type: Office visit, established patient, face-to-face
Clinician: Synthetic Practitioner, FNP-C (Primary Care)
Location: Synthetic Primary Care Clinic, Room 5

CHIEF COMPL-
AINT
Diabetes check and lab review.

HISTORY OF PRESENT ILLNESS
66-year-old woman presents for scheduled follow-up. History of type 2 diabetes diagnosed 13 years ago. Home glucose log reviewed, fasting values 118-141 mg/dL with occasional post-meal readings above 200. Mild bilateral knee stiffness in the mornings, unchanged. No polyuria or
--- Page 2 of 3 --- FU-0300 --- printed 2026-07-20 ---
polydipsia. No visual changes.

REVIEW OF SYSTEMS
Skin: no rashes or non-healing wounds.
Neurological: no numbness or tingling in the feet; no headaches.
Gastrointestinal: no nausea, vomiting, diarrhea or constipation.
Constitutional: denies fever, chills or unintended weight loss.
Cardio-
vascular: no chest pain, palpitations or orthopnea.
End-
ocrine: no polyuria, polydipsia or heat or cold intolerance.
Genitourinary: no dysuria, hematuria or change in urine output.
Eyes: no blurred vision; last dilated eye exam 2024.
Musculoskeletal: chronic knee stiffness, otherwise negative.

MEDICATIONS
- metformin 1000 mg twice daily
- empagliflozin 10 mg daily
- losartan 50 mg daily
- levothyroxine 75 mcg daily
- omeprazole 20 mg daily
Med rec done with patient’s pill bottles.

ALLERGIES
NKDA.

PAST MEDICAL HISTORY / PROBLEM LIST
- Type 2 diabetes mellitus
- Chronic kidney disease, stage 3a
- Hypothyroidism
- GERD

PAST SURGICAL HISTORY
- Appendectomy (1988)
- Cataract extraction, left eye (2022)

FAMILY HISTORY
Brother: hyperlipidemia.
Father: coronary artery disease, died age 72.
No family history of kidney disease reported.

SOCIAL HISTORY
Former smoker, quit 2010; 21 pack-years.
Walks 2 times per week, about 20 minutes.
Alcohol: none.

VITALS
BP 139/88 | HR 63 | Temp 97.7 F | Wt 70.4 kg | BMI 23.7 | SpO2 94%

EXAM
General: alert, oriented, NAD.
Heart: RRR.
Lungs: CTAB.
Extremities: trace bilateral ankle edema.
Feet: monofilament sensation intact, pulses 2+.

LABS
Date	Test         Result
2025-12-21	eGFR	48 mL/min/1.73m2
2026-04-10   eGFR	45 mL/min/1.73m2
2026-04-10	Creatinine	1.37 mg/dL
2026-07-03 Hemoglobin A1c	8.8%
2026-07-03  Glucose, fasting	135 mg/dL
2026-07-03	LDL cholesterol	73 mg/dL
2026-07-03 Hemoglobin   11.2 g/dL

ASSESSMENT/PLAN
(Assessment copied from note dated 2026-04-11 and updated where noted.)
1. T2DM: A1c 8.8%, improved from 10.2%. Reviewed diet and activity. Continue medications. Retinal exam due.
2. Hypothyroid: clinically euthyroid. Continue current dose.
3. Chronic kidney disease stage 3a: eGFR 45 (2026-04-10), stab1e at that time. Continue regimen as previous1y outlined.
4. Also on problem list: GERD.
5. Shingles vaccine series completed. Colorectal cancer screening up to date.

PATIENT EDUCATI0N
Reviewed sick-day rules for medications.
Discussed hypoglycemia recognition and treatment.

Return to clinic in 6 months or sooner as needed.
Electronically signed: Synthetic Practitioner, FNP-C 2026-07-03 10:26
```

</details>

