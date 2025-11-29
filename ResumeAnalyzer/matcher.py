"""Skill & keyword matching module."""
from typing import List, Tuple
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_sm')

def normalize_list(lst: List[str]) -> List[str]:
    return [l.strip().lower() for l in lst if l]

def extract_keywords_from_text(text: str, top_k: int = 40) -> List[str]:
    doc = nlp(text)
    chunks = [c.text.strip().lower() for c in doc.noun_chunks]
    tokens = [t.lemma_.lower() for t in doc if t.is_alpha and not t.is_stop]
    combined = ' '.join(chunks + tokens)
    vectorizer = TfidfVectorizer(max_features=top_k)
    vecs = vectorizer.fit_transform([combined])
    return vectorizer.get_feature_names_out().tolist()

def match_skills(resume_skills: List[str], jd_skills: List[str]) -> Tuple[List[str], List[str]]:
    rs = normalize_list(resume_skills)
    js = normalize_list(jd_skills)
    matched = [s for s in rs if any(s == j or s in j or j in s for j in js)]
    missing = [j for j in js if not any(j == s or j in s or s in j for s in rs)]
    return list(dict.fromkeys(matched)), list(dict.fromkeys(missing))

def jd_similarity_score(resume_text: str, jd_text: str) -> float:
    v = TfidfVectorizer(stop_words='english')
    mat = v.fit_transform([resume_text, jd_text])
    score = cosine_similarity(mat[0:1], mat[1:2])[0][0]
    return float(score)
