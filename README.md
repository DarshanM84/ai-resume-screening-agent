# 🤖 AI Resume Screening Agent

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-resume-screening-agent-fn73udascyxegy8ubhrmrn.streamlit.app/)

An AI-powered Resume Screening and Candidate Ranking platform built using **Python, Streamlit, Google Gemini AI, NLP, and Scikit-Learn**.

The application intelligently analyzes resumes against a job description, extracts candidate skills, performs semantic matching, generates recruiter insights using Gemini AI, and ranks applicants based on overall suitability.

---

# ✨ Features

✅ Resume Parsing (PDF/DOCX/TXT)

✅ Job Description Parsing

✅ AI Skill Extraction

✅ Semantic Resume Matching

✅ Recruiter Summary using Gemini AI

✅ Candidate Ranking Dashboard

✅ Match Score Visualization

✅ Multi Resume Screening

---

## 🌐 Live Demo

🚀 **Live Demo**

https://ai-resume-screening-agent-fn73udascyxegy8ubhrmrn.streamlit.app/

---

# 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API
- Scikit-Learn
- TF-IDF Vectorization
- Cosine Similarity
- PyPDF2
- python-docx

---

# 📂 Project Structure

```
AI-Resume-Screening-Agent
│
├── app.py
├── requirements.txt
├── README.md
├── assets/
├── data/
│     sample_jd.txt
├── sample_resumes/
├── output/
├── utils/
└── .env
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/DarshanM84/ai-resume-screening-agent.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a .env file

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the application

```bash
streamlit run app.py
```

If the command is not recognized on your system, you can also use:

```bash
python -m streamlit run app.py
```

---

# 📋 How It Works

1. Upload a Job Description.
2. Upload one or multiple candidate resumes.
3. Click **Analyze & Rank Candidates**.
4. The system:
   - Extracts resume information
   - Matches skills
   - Calculates semantic similarity
   - Generates AI recruiter insights
   - Ranks candidates
5. Recruiters receive a ranked shortlist with detailed AI explanations.

---

# 📸 Screenshots

## Landing Page

![Landing](assets/landing.png)

## Recruitment Dashboard

![score](assets/score.png)

## Candidate Ranking

![ranking](assets/rank.png)

## AI Recruiter Summary

![ai_summary](assets/ai_summary.png)
---

# 📈 Output

The application provides

- Overall Match Score
- Skill Match Score
- Semantic Match Score
- AI Recruiter Summary
- Candidate Ranking
- Skills Overview

---

## 📐 Scoring Method

Each candidate receives an **Overall Match Score** based on two components:

| Component | Weight | Description |
|-----------|--------|-------------|
| Skill Match | **70%** | Measures how many required job skills are found in the candidate's resume. |
| Semantic Match | **30%** | Uses NLP-based similarity to compare the candidate's resume with the job description. |

### Formula

```text
Overall Match Score =
(0.70 × Skill Match) +
(0.30 × Semantic Match)
```

### Recommendation Logic

| Overall Match | Recommendation |
|---------------|---------------|
| ≥ 60% | ✅ Recommended |
| < 60% | ⚠️ Consider |

Candidates are ranked in descending order based on the Overall Match Score.

---

# 🔮 Possible Enhancements

- Sentence Transformer Embeddings
- FAISS Vector Search
- Resume Comparison Dashboard
- ATS Resume Score
- Recruiter Chat Assistant

---

# 👨‍💻 Author

Darshan M

GitHub:
https://github.com/DarshanM84

LinkedIn:
https://linkedin.com/in/darshan-m2004