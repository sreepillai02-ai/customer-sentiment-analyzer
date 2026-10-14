# 💬 SocialSense: Customer Feedback Sentiment Analyzer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B.svg)](https://streamlit.io/)
[![NLP](https://img.shields.io/badge/NLP-VADER%20%7C%20TextBlob-green.svg)](https://github.com/cjhutto/vaderSentiment)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

An end-to-end Natural Language Processing (NLP) system designed to analyze **customer feedback and social media comments** (Twitter/X, Reddit, Instagram, Facebook). 

SocialSense uses **VADER Sentiment Analysis** (handling emojis, slang, and capitalization) and **TextBlob Subjectivity** to measure customer happiness, track negative complaints, and compute the **Net Sentiment Score (NSS)**.

---

## 🌟 Key Features

- **⚡ Real-Time Post Analyzer**: Test any tweet or review with a live visual speedometer/gauge.
- **📈 Executive Sentiment Dashboard**: View KPI cards, the Net Sentiment Score (NSS = % Positive - % Negative), and channel comparisons (Twitter vs Reddit vs Instagram).
- **📋 Data Explorer & Export**: Search, filter reviews by platform or sentiment, and export enriched data to CSV.
- **📖 Step-by-Step User Guide**: Plain, beginner-friendly instructions built directly into the web app.
- **🎓 Presentation Slides Included (.pptx & .pdf)**: 10 clean widescreen slides with speaker notes for college/viva presentations.

---

## 🚀 Quickstart: How to Run

### Step 1: Open Your Folder
`C:\Users\sreep\.gemini\antigravity\scratch\social-media-feedback-analyzer`

### Step 2: 1-Click Launch
- **To Run the Website**: Double-click **`run_app.bat`** (opens at `http://localhost:8501`).
- **To Generate the PDF Presentation**: Double-click **`generate_pdf.bat`**.
- **To Generate the PowerPoint Presentation**: Double-click **`generate_ppt.bat`**.
- **To Run Unit Tests**: Double-click **`run_tests.bat`**.

---

## 📁 Repository Structure

```text
social-media-feedback-analyzer/
├── src/
│   ├── preprocessor.py       # Social media text normalization & cleaning
│   ├── sentiment.py          # VADER & TextBlob sentiment engines
│   ├── insights.py           # Net Sentiment Score & business logic
│   └── __init__.py           # Package exports
├── data/
│   └── sample_social_feedback.csv  # 30 realistic sample customer reviews
├── presentation/
│   ├── Social_Media_Sentiment_Topic_Analysis_Presentation.pptx # 10-slide PowerPoint
│   └── Social_Media_Sentiment_Topic_Analysis_Presentation.pdf  # 10-slide PDF
├── tests/
│   └── test_analyzer.py      # Automated unit tests
├── app.py                    # Streamlit interactive web dashboard
├── cli.py                    # Command-line batch runner
├── generate_presentation.py  # PowerPoint deck generator
├── generate_pdf.py           # PDF presentation generator
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore configuration
├── run_app.bat               # 1-click Windows runner for Website
├── run_tests.bat             # 1-click Windows runner for Unit Tests
├── generate_ppt.bat          # 1-click Windows runner for PPTX
└── generate_pdf.bat          # 1-click Windows runner for PDF
```

---

## 🐙 How to Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Customer Feedback Sentiment Analyzer"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
git push -u origin main
```
