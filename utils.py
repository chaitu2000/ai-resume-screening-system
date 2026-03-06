import re
from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def normalize_text(text: str) -> List[str]:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    tokens = text.split()
    return tokens


def extract_keywords(text: str) -> List[str]:
    tokens = normalize_text(text)
    unique_tokens = sorted(set(tokens))
    return unique_tokens


def score_resume(resume_text: str, jd_keywords: List[str]) -> Tuple[float, List[str]]:
    resume_tokens = normalize_text(resume_text)
    resume_text_normalized = " ".join(resume_tokens)
    jd_text = " ".join(jd_keywords)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text_normalized, jd_text])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    matched_keywords = [kw for kw in jd_keywords if kw in resume_tokens]

    return round(float(score) * 100, 2), matched_keywords