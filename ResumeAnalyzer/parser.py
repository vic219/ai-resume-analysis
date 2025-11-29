"""Resume parsing: accepts text or PDF path and returns parsed sections."""
from typing import Dict, List
import pdfplumber
import re
import spacy
from utils import extract_email, extract_phone, normalize_text

nlp = spacy.load("en_core_web_sm")

def read_pdf_text(path: str) -> str:
    text = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text.append(page_text)
    return "\n".join(text)

def read_text_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def parse_resume(path: str) -> Dict:
    raw = ""
    if path.lower().endswith('.pdf'):
        raw = read_pdf_text(path)
    else:
        raw = read_text_file(path)
    raw = normalize_text(raw)
    email = extract_email(raw)
    phone = extract_phone(raw)
    doc = nlp(raw)
    name = None
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            if ent.start_char < 200:
                name = ent.text
                break
    sections = {'education': [], 'skills': [], 'experience': [], 'certifications': []}
    lines = [l.strip() for l in raw.split('\n') if l.strip()]
    cur = 'other'
    for line in lines:
        low = line.lower()
        if any(k in low for k in ['education', 'degree', 'university', 'b.sc', 'bachelor', 'master', 'bs', 'ms', 'phd']):
            cur = 'education'
            sections['education'].append(line)
            continue
        if 'skill' in low or 'technologies' in low or 'technical skills' in low:
            cur = 'skills'
            sections['skills'].append(line)
            continue
        if any(k in low for k in ['experience', 'professional experience', 'work experience', 'employment']):
            cur = 'experience'
            sections['experience'].append(line)
            continue
        if any(k in low for k in ['certificat', 'certificate', 'certified']):
            cur = 'certifications'
            sections['certifications'].append(line)
            continue
        if cur in sections and cur != 'other':
            sections[cur].append(line)
    skills = []
    if sections['skills']:
        raw_skills = ' '.join(sections['skills'])
        for token in re.split('[,|/;\\•\n]', raw_skills):
            t = token.strip()
            if t:
                skills.append(t)
    else:
        tokens = [t.text for t in doc if not t.is_stop and t.is_alpha]
        tech_terms = set(['python','java','c++','c','javascript','react','node','django','flask','sql','aws','azure','docker','kubernetes','git','html','css','tensorflow','pytorch','nlp','spacy'])
        skills = [t for t in tokens if t.lower() in tech_terms]
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'education': sections['education'],
        'skills': list(dict.fromkeys([s for s in skills if s])),
        'experience': sections['experience'],
        'certifications': sections['certifications'],
        'raw_text': raw
    }

if __name__ == '__main__':
    import sys
    print(parse_resume(sys.argv[1]))
