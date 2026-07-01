# GitInsight – AI-Powered GitHub Repository Intelligence Platform

GitInsight is a full-stack web application that helps developers, recruiters, students, and open-source contributors understand GitHub repositories through AI-generated insights. It integrates GitHub OAuth, GitHub REST APIs, and Large Language Models (LLMs) to analyze repository metadata, documentation, and project structure.

---

## Features

* GitHub OAuth 2.0 Authentication
* Search any public GitHub user
* Browse user repositories
* AI-powered repository analysis
* Project summary generation
* Technology stack identification
* Repository health assessment
* Documentation quality evaluation
* Project strengths and weaknesses
* Actionable recommendations for improvement

---

## Tech Stack

### Backend

* FastAPI
* Python
* REST APIs

### Frontend

* Streamlit

### Database

* PostgreSQL
* SQLAlchemy

### AI

* Google Gemini
* Prompt Engineering

### External APIs

* GitHub REST API
* GitHub OAuth 2.0

---

## Project Structure

```text
GitInsight/
│
├── backend/
│   ├── routers/
│   ├── services/
│   ├── database/
│   ├── schemas/
│   ├── models.py
│   └── main.py
│
├── frontend/
│   ├── app.py
│   └── pages/
│
├── .env
├── requirements.txt
└── README.md
```

---

## Workflow

```text
User Login
      │
      ▼
GitHub OAuth Authentication
      │
      ▼
Search GitHub User
      │
      ▼
Select Repository
      │
      ▼
Fetch Repository Metadata
      │
      ▼
Collect
 • README
 • Languages
 • Repository Statistics
 • File Structure
      │
      ▼
Generate AI Analysis
      │
      ▼
Display Insights in Streamlit
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/GitInsight.git
cd GitInsight
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the backend directory.

```env
GITHUB_CLIENT_ID=YOUR_CLIENT_ID
GITHUB_CLIENT_SECRET=YOUR_CLIENT_SECRET
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
DATABASE_URL=postgresql://username:password@localhost/gitinsight
```

### 5. Run the FastAPI backend

```bash
uvicorn main:app --reload
```

### 6. Run the Streamlit frontend

```bash
streamlit run app.py
```

---

## AI Analysis Includes

* Project Summary
* Project Purpose
* Technology Stack
* Repository Health Score
* Documentation Review
* Strengths
* Weaknesses
* Improvement Recommendations

---

## Future Enhancements

* Repository comparison
* Historical health tracking
* PDF report generation
* CSV export
* Repository caching with PostgreSQL
* Private repository analysis via GitHub OAuth
* Dashboard analytics
* CI/CD integration analysis

---

## Screenshots

Add screenshots of:

* Login Page
* Repository Selection
* AI Analysis Report

---

## License

This project is licensed under the MIT License.
