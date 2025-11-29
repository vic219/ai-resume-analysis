"""Generates actionable suggestions based on parsed data and matches."""
from typing import List, Dict
def generate_feedback(parsed: Dict, matched: List[str], missing: List[str], jd_keywords: List[str]) -> Dict:
    suggestions = []
    if missing:
        suggestions.append(f"Add or emphasize these skills/keywords: {', '.join(missing[:10])}.")
    suggestions.append("Make the top 3-4 lines a tailored summary that includes the role + 2-3 top skills from the JD.")
    if len(parsed.get('raw_text','').split()) < 200:
        suggestions.append("Expand bullet points under each job to include metrics and impact (e.g., reduced latency by 30%).")
    if not parsed.get('certifications'):
        suggestions.append("If you have relevant certifications (e.g., AWS, GCP), list them in a Certifications section.")
    if parsed.get('skills') and isinstance(parsed.get('skills'), list) and len(parsed['skills'])<5:
        suggestions.append("List technical skills as a separate comma-separated or column layout for easy parsing by ATS.")
    missing_keywords = [k for k in jd_keywords if k not in parsed.get('raw_text','').lower()]
    if missing_keywords:
        suggestions.append(f"Include important JD keywords such as: {', '.join(missing_keywords[:8])}.")
    return {
        'suggestions': suggestions,
        'strengths': [s for s in matched[:10]],
        'weaknesses': missing[:10]
    }
