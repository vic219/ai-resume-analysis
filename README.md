# AI Resume Analysis (ATS-Style Resume Scorer)

An **AI-powered Resume Analyzer** that simulates how an ATS (Applicant Tracking System) might evaluate a resume against a specific job description.

This project:
- Extracts key information from a resume (skills, education, experience, contact info)
- Matches the resume against a **job description (JD)**
- Calculates an **ATS-style score (0–100)**
- Shows **matched** and **missing** skills/keywords
- Generates **actionable suggestions** to improve the resume

---

##  Features

-  **Resume parsing**
  - Reads resume text (TXT or PDF with `pdfplumber`)
  - Extracts name, email, phone, education, experience, skills, and certifications

-  **NLP-based analysis**
  - Uses spaCy to clean and process text
  - Extracts skills and important keywords
  - Pulls keywords from the job description

- **ATS-style matching**
  - Rule-based skill & keyword matching between resume and JD
  - TF‑IDF + cosine similarity score between resume and JD content
  - Simple signals for experience, education, and formatting

-  **Scoring & feedback**
  - Final **ATS score (0–100)** based on weighted components
  - Lists **matched skills** and **missing skills**
  - Highlights **strengths** and **weaknesses**
  - Provides **clear suggestions** to improve the resume

---

##  Tech Stack

- **Language:** Python 3
- **NLP:** spaCy (`en_core_web_sm`)
- **PDF Parsing:** pdfplumber (optional, for PDF resumes)
- **ML Utilities:** scikit-learn (TF‑IDF vectorizer & cosine similarity)
- **Notebook:** Jupyter / Google Colab

---

##  Project Structure

```text
ai-resume-analysis/
└── ResumeAnalyzer/
    ├── parser.py             # Resume parsing (text/PDF → structured fields)
    ├── matcher.py            # Skill & keyword matching, JD similarity
    ├── scoring.py            # ATS-style weighted scoring (0–100)
    ├── feedback.py           # Generates strengths, weaknesses, suggestions
    ├── utils.py              # Helpers (email/phone extraction, normalization, etc.)
    ├── run_analyzer.py       # CLI entry point – runs analysis and outputs JSON report
    ├── ResumeAnalyzer.ipynb  # Notebook demo (Colab-friendly)
    └── samples/              # Sample resumes & job descriptions
        ├── resume1.txt
        ├── resume2.txt
        ├── resume3.txt
        ├── jd_software_engineer.txt
        └── jd_data_scientist.txt
