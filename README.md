# AI Resume Screening System

A recruiter-friendly NLP project that scores resumes against a job description using weighted keyword matching.

## Why this project matters
This project shows:
- practical NLP preprocessing
- job-description matching
- user-facing app development
- explainable scoring output

## Tech Stack
- Python
- Streamlit
- pandas
- regex / NLP basics

## Features
- paste a job description
- upload one or more resumes
- extract important keywords
- calculate match score
- display ranked results

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Overview of the project
- Built an NLP-based resume screening application that ranks resumes against job descriptions using weighted keyword matching.
- Developed a Streamlit interface for uploading resumes, extracting skills, and generating explainable ranking results.
- Applied practical text preprocessing and scoring logic to demonstrate machine learning product thinking.


## Architecture

![Architecture](docs/resume_screening_architecture.png)

## Example Output

![Resume Screening Output](docs/resume_screening_output.png)

## Features

- Resume upload and parsing
- Job description keyword extraction
- TF-IDF based similarity scoring
- Resume ranking based on relevance

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLP / TF-IDF