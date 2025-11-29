"""Command-line entry: parse resume, parse job, match, score, and produce JSON report."""
import argparse, json
from parser import parse_resume
from matcher import match_skills, extract_keywords_from_text, jd_similarity_score
from scoring import calculate_score, formatting_score
from feedback import generate_feedback
def read_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--resume', required=True)
    p.add_argument('--job', required=True)
    p.add_argument('--out', default='report.json')
    args = p.parse_args()
    parsed = parse_resume(args.resume)
    jd_text = read_text(args.job)
    jd_keywords = extract_keywords_from_text(jd_text, top_k=60)
    matched, missing = match_skills(parsed.get('skills', []), jd_keywords)
    skill_pct = 0.0
    if len(jd_keywords) > 0:
        skill_pct = len(matched) / len(jd_keywords)
    keyword_sim = jd_similarity_score(parsed.get('raw_text',''), jd_text)
    exp_score = 0.6 if parsed.get('experience') else 0.2
    education_match = 1.0 if parsed.get('education') else 0.0
    fmt = formatting_score(parsed.get('raw_text',''))
    match_counts = {
        'skill_pct': skill_pct,
        'keyword_pct': keyword_sim,
        'exp_score': exp_score,
        'education_match': education_match,
        'formatting_score': fmt
    }
    final_score = calculate_score(match_counts, {})
    fb = generate_feedback(parsed, matched, missing, jd_keywords)
    report = {
        'ats_score': final_score,
        'matched_skills': matched,
        'missing_skills': missing,
        'strengths': fb['strengths'],
        'weaknesses': fb['weaknesses'],
        'suggestions': fb['suggestions'],
        'parsed': {k: parsed[k] for k in ['name','email','phone','education','skills','experience','certifications']}
    }
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    print(f"Report written to {args.out}")
