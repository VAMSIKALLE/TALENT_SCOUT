# TALENT_SCOUT
Data-driven talent discovery and performance analysis system
# TalentScout — Resume Intake & Role-Fit Analyzer

TalentScout is a Flask-powered web application designed to streamline the recruitment process. It automates candidate resume parsing, compares technical skills against specific job requirements, ranks candidate suitability, and generates downloadable PDF summary reports for hiring teams.

---

## 🚀 Features

* **PDF Resume Parsing**: Extracts candidate information, contact details, experience, and technical skill sets directly from uploaded PDF resumes.
* **Role Match & Ranking Engine**: Evaluates candidate skill sets against specified target roles (e.g., *Python Full Stack*, *Data Scientist*) and calculates percentage compatibility scores.
* **Skill Gap Analysis**: Identifies matched skills alongside missing required skills for each candidate.
* **Filter & Export Scope**: Dynamic filtering to display top candidates (Top 5, Top 10, or All) and export candidate summary reports directly to structured PDFs.
* **Session Management**: Clear workspace option to reset candidates during recruitment sessions.

---

## 🛠️ Project Architecture & Tech Stack

* **Backend Framework**: Python / Flask
* **Frontend UI**: HTML5, CSS3, JavaScript (Fetch API)
* **PDF Processing & Generation**: ReportLab / PyPDF2 / pdfplumber (via `pdf_parser` & `pdf_export`)
* **WSGI Server**: Werkzeug

---

## 📁 Directory Structure

```text
TalentScout/
│
├── app.py                  # Main Flask web application backend
├── pdf_parser.py           # Resume text extraction and skill parsing logic
├── analyzer.py             # Role-fit scoring & candidate ranking algorithm
├── pdf_export.py           # ReportLab PDF summary report generator
├── exceptions.py           # Custom exception definitions (TalentScoutError)
│
├── static/
│   └── style.css           # Modern UI design and responsiveness styles
│
├── templates/
│   └── index.html          # Dynamic single-page dashboard interface
│
├── uploads/                # Temporary storage for uploaded resumes
└── outputs/                # Generated PDF report downloads
