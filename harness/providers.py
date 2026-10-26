"""Model providers. Each returns (text, usage) for a system + user prompt.

Keys are read from the environment only: ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY (or GOOGLE_API_KEY).
"""

import json
import os
import random
import time


class ProviderError(Exception):
    pass


def _retry(fn, attempts=5):
    delay = 2.0
    for i in range(attempts):
        try:
            return fn()
        except Exception as e:  # network, rate limit, overload
            if i == attempts - 1:
                raise ProviderError(str(e)) from e
            time.sleep(delay + random.random())
            delay *= 2


class AnthropicProvider:
    def __init__(self, model, max_output_tokens, temperature=None):
        import anthropic
        self.client = anthropic.Anthropic()
        self.model, self.max_tokens = model, max_output_tokens
        # The current Anthropic SDK's messages.create takes no temperature argument; the model default is used.

    def complete(self, system, user, **_):
        def call():
            r = self.client.messages.create(model=self.model, max_tokens=self.max_tokens, system=system,
                                            messages=[{"role": "user", "content": user}])
            text = "".join(b.text for b in r.content if getattr(b, "type", "") == "text")
            return text, {"input_tokens": r.usage.input_tokens, "output_tokens": r.usage.output_tokens}
        return _retry(call)


class OpenAIProvider:
    def __init__(self, model, max_output_tokens, temperature=None):
        import openai
        self.client = openai.OpenAI()
        self.model, self.max_tokens, self.temperature = model, max_output_tokens, temperature

    def complete(self, system, user, **_):
        def call():
            kw = {"temperature": self.temperature} if self.temperature is not None else {}
            r = self.client.responses.create(model=self.model, instructions=system, input=user,
                                             max_output_tokens=self.max_tokens, **kw)
            u = r.usage
            return r.output_text, {"input_tokens": getattr(u, "input_tokens", None),
                                   "output_tokens": getattr(u, "output_tokens", None)}
        return _retry(call)


class GeminiProvider:
    def __init__(self, model, max_output_tokens, temperature=None):
        from google import genai
        from google.genai import types
        self.client, self.types = genai.Client(), types
        self.model, self.max_tokens, self.temperature = model, max_output_tokens, temperature

    def complete(self, system, user, **_):
        def call():
            cfg = self.types.GenerateContentConfig(system_instruction=system, max_output_tokens=self.max_tokens,
                                                   temperature=self.temperature,
                                                   response_mime_type="application/json")
            r = self.client.models.generate_content(model=self.model, contents=user, config=cfg)
            m = r.usage_metadata
            # Thinking tokens are billed as output and count against max_output_tokens; include them.
            out = (getattr(m, "candidates_token_count", None) or 0) + (getattr(m, "thoughts_token_count", None) or 0)
            return r.text or "", {"input_tokens": getattr(m, "prompt_token_count", None), "output_tokens": out}
        return _retry(call)


class MockProvider:
    """Offline stand-in for testing the pipeline. It answers from the answer key with injected errors.
    Its results say nothing about any real model and must never be reported."""

    def __init__(self, model, max_output_tokens, temperature=None, charts=None, seed=0):
        self.charts = charts or {}
        self.rng = random.Random(seed)

    def complete(self, system, user, task=None, chart_id=None, weights=None, **_):
        c = self.charts[chart_id]
        rng = self.rng
        if task == "verbal":
            p = 0.75 if c["label"] else 0.55
            conf = int(min(100, max(0, rng.gauss(p * 100 + 10, 12)) // 5 * 5))
            return json.dumps({"supported": conf >= 50, "confidence": conf}), {"input_tokens": 0, "output_tokens": 0}
        out = {}
        for q, a in c["intended_answers"].items():
            if rng.random() < 0.06:
                a = rng.choice([x for x in ("yes", "no", "not_documented") if x != a])
            spans = c["evidence"].get(q, [])
            quotes = [spans[0]] if (a in ("yes", "no") and spans) else ([c["text"][:30]] if a in ("yes", "no") else [])
            if quotes and rng.random() < 0.04:
                quotes = [quotes[0].upper().replace(" ", "  ") + " (paraphrased)"]
            out[q] = {"answer": a, "quotes": quotes, "rationale": "mock"}
        res = {"answers": out}
        if task == "m6":
            res["probability"] = round(min(1, max(0, (0.9 if c["label"] else 0.2) + rng.gauss(0, 0.1))), 3)
        return json.dumps(res), {"input_tokens": 0, "output_tokens": 0}


def make_provider(spec, cfg, charts=None):
    kind = spec["provider"]
    args = (spec["model"], cfg["max_output_tokens"], cfg.get("temperature"))
    if kind == "anthropic":
        return AnthropicProvider(*args)
    if kind == "openai":
        return OpenAIProvider(*args)
    if kind == "gemini":
        return GeminiProvider(*args)
    if kind == "mock":
        return MockProvider(*args, charts=charts, seed=cfg.get("seed", 0))
    raise ValueError(f"unknown provider {kind}")


KEY_ENV = {"anthropic": ["ANTHROPIC_API_KEY"], "openai": ["OPENAI_API_KEY"],
           "gemini": ["GEMINI_API_KEY", "GOOGLE_API_KEY"], "mock": []}


def key_present(kind):
    envs = KEY_ENV.get(kind, [])
    return not envs or any(os.environ.get(e) for e in envs)
