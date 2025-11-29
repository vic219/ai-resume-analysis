"""Implements ATS scoring logic (rule-based)."""
from typing import Dict
WEIGHTS = {
    'skills': 0.40,
    'keywords': 0.20,
    'experience': 0.20,
    'education': 0.10,
    'formatting': 0.10
}
def calculate_score(match_counts: Dict, similarity_scores: Dict) -> float:
    s = 0.0
    s += WEIGHTS['skills'] * match_counts.get('skill_pct', 0)
    s += WEIGHTS['keywords'] * match_counts.get('keyword_pct', 0)
    s += WEIGHTS['experience'] * match_counts.get('exp_score', 0)
    s += WEIGHTS['education'] * match_counts.get('education_match', 0)
    s += WEIGHTS['formatting'] * match_counts.get('formatting_score', 0)
    return round(s * 100, 2)
def formatting_score(raw_text: str) -> float:
    score = 0.5
    if len(raw_text.split()) > 150:
        score += 0.25
    if '\n' in raw_text and ('•' in raw_text or '-' in raw_text):
        score += 0.25
    return min(1.0, score)
