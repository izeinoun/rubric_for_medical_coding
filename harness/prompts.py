"""Prompt templates. Any change here is a pipeline change: log it in CHANGELOG.md."""

import json

PROMPT_VERSION = "1"

EXTRACT_SYSTEM = """You are a clinical documentation abstractor. You answer fixed questions about one outpatient note, using only the text of that note.

Rules:
1. Each answer is exactly one of: "yes", "no", "not_documented".
   - yes: the note affirmatively documents the fact.
   - no: the note explicitly documents the opposite, or explicitly says the fact is not established.
   - not_documented: the note is silent on the fact.
2. For every yes or no answer, give one or more quotes copied EXACTLY, character for character, from the note. Do not paraphrase, shorten, merge or correct a quote. Each quote should be a short span (a phrase or one line). For not_documented, give an empty quote list.
3. Give a rationale of at most 20 words.
4. Return JSON only, with no other text, in this shape:
{"answers": {"<question id>": {"answer": "...", "quotes": ["..."], "rationale": "..."}}}"""


def extract_user(rubric, note_text):
    qs = []
    for qid in rubric["gates"] + rubric["weighted"]:
        q = rubric["questions"][qid]
        qs.append(f'{qid}. {q["text"]}\n    Guidance: {q["guidance"]}')
    return ("QUESTIONS\n" + "\n".join(qs) + "\n\nNOTE\n<<<\n" + note_text + ">>>\n\n"
            "Answer every question id: " + ", ".join(rubric["gates"] + rubric["weighted"]) + ".")


VERBAL_SYSTEM = """You review outpatient notes for diagnosis-code support in Medicare Advantage risk adjustment.
Return JSON only, with no other text, in this shape:
{"supported": true or false, "confidence": <integer 0-100>}
"confidence" is your probability, in percent, that the note supports reporting the code."""


def verbal_user(rubric, note_text):
    return (f'Does this note support reporting ICD-10-CM {rubric["candidate_code"]} '
            f'({rubric["code_description"]}) for a risk-adjustment submission?\n\nNOTE\n<<<\n{note_text}>>>')


M6_SYSTEM = EXTRACT_SYSTEM.replace(
    '{"answers": {"<question id>": {"answer": "...", "quotes": ["..."], "rationale": "..."}}}',
    '{"answers": {"<question id>": {"answer": "...", "quotes": ["..."], "rationale": "..."}}, "probability": <number 0-1>}'
) + """
5. Then compute "probability" yourself from your answers and the scoring table in the user message: if any gate question is not "yes", probability is 0. Otherwise add the intercept and the weight of each answer (not_documented adds 0), and apply the logistic function 1 / (1 + e^(-total))."""


def m6_user(rubric, note_text, weights):
    table = {k: round(v, 4) for k, v in weights.items() if not k.startswith("_")}
    return extract_user(rubric, note_text) + "\n\nSCORING TABLE\n" + json.dumps(table, indent=1) + \
        "\nGate questions: " + ", ".join(rubric["gates"]) + "."
