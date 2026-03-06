import re
from collections import Counter

STOPWORDS = {
    "and", "or", "the", "a", "an", "to", "for", "with", "of", "in", "on",
    "is", "are", "be", "as", "using", "build", "required", "skills",
    "experience", "knowledge", "intern", "role", "job", "data", "engineering"
}


def normalize_text(text: str) -> list[str]:
    tokens = re.findall(r"[a-zA-Z0-9\+#\.]+", text.lower())
    return [token for token in tokens if token not in STOPWORDS and len(token) > 1]


def extract_keywords(text: str) -> set[str]:
    tokens = normalize_text(text)
    counts = Counter(tokens)
    return {token for token, count in counts.items() if count >= 1}


def score_resume(resume_text: str, jd_keywords: set[str]) -> tuple[float, list[str]]:
    resume_tokens = set(normalize_text(resume_text))
    matches = sorted(resume_tokens.intersection(jd_keywords))
    score = round((len(matches) / max(len(jd_keywords), 1)) * 100, 2)
    return score, matches
