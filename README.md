# AI Resume Analyzer (ATS-Style Scoring System)

## Project Overview
This project is an **AI-powered Resume Analyzer** designed to function like an **Applicant Tracking System (ATS)**. It parses resumes, matches skills against job descriptions, calculates an ATS score, and provides actionable feedback to improve resumes.

**Key Features:**
- Extracts candidate details: name, contact info, education, skills, experience, certifications.
- Matches skills and keywords with job descriptions.
- Calculates an **ATS score (0–100)** based on skills, experience, education, and formatting.
- Provides **feedback and suggestions** for improving resumes.
- Outputs a **structured report** showing matched/missing skills and improvement tips.

## Tech Stack
- **Python 3.10+**
- **NLP Libraries:** spaCy, NLTK
- **PDF Processing:** pdfplumber, PyPDF2
- **Machine Learning / Scoring:** scikit-learn (optional)
- **Development:** Jupyter Notebook, modular `.py` scripts

## Installation
1. Clone this repository:
```bash
git clone <repo-url>
cd AI-Resume-Analyzer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install required packages

 pdfplumber
 PyPDF2
 scikit-learn
 pandas
 regex
 nbformat
 spacy --prefer-binary

4. Download spaCy English model:
```bash
python -m spacy download en_core_web_sm
```

## Project Structure
```
AI-Resume-Analyzer/
│
├── parser.py                 # Resume parsing functions
├── matcher.py                # Keyword & skill matching functions
├── scoring.py                # ATS score calculation
├── feedback.py               # Feedback generation
├── Samples/                  # Sample resumes (fake data)
│   ├── resume1.txt
│   ├── resume2.txt
│   └── resume3.txt
├── jd_software_engineer.txt  # Sample job description
├── notebook.ipynb            # Jupyter notebook demo
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

## Usage
1. Open `notebook.ipynb`.
2. Run the cells to parse resumes, match skills, calculate scores, and generate feedback.

**Example code:**
```python
from parser import parse_resume
from matcher import extract_keywords_from_text, match_skills, jd_similarity_score
from scoring import calculate_score, formatting_score
from feedback import generate_feedback

parsed = parse_resume('Samples/resume3.txt')
with open('jd_software_engineer.txt','r',encoding='utf-8') as f:
    jd_text = f.read()

jd_keywords = extract_keywords_from_text(jd_text, top_k=60)
matched, missing = match_skills(parsed.get('skills', []), jd_keywords)
skill_pct = len(matched)/len(jd_keywords) if jd_keywords else 0
keyword_sim = jd_similarity_score(parsed.get('raw_text',''), jd_text)
exp_score = 0.6 if parsed.get('experience') else 0.2
education_match = 1 if parsed.get('education') else 0
fmt = formatting_score(parsed.get('raw_text',''))
match_counts = {'skill_pct': skill_pct, 'keyword_pct': keyword_sim,
                'exp_score': exp_score, 'education_match': education_match,
                'formatting_score': fmt}
final_score = calculate_score(match_counts, {})
fb = generate_feedback(parsed, matched, missing, jd_keywords)

print('ATS Score:', final_score)
print('Matched Skills:', matched)
print('Missing Skills (top 10):', missing[:10])
print('Suggestions:', fb['suggestions'])
```

## Outputs
- **ATS Score (0–100)**
- **Matched and Missing Skills**
- **Experience & Education Match**
- **Formatting Score**
- **Improvement Suggestions**

Optional: JSON or TXT export of results.

## Notes
- Sample resumes and job descriptions are included for testing.
- For production, replace them with actual resumes and JDs.
- spaCy is required for entity extraction. If not installed, run:
```bash

