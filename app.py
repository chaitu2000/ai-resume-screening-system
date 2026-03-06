import io
import pandas as pd
import streamlit as st
from utils import extract_keywords, score_resume

st.set_page_config(page_title="AI Resume Screening System", layout="wide")
st.title("AI Resume Screening System")
st.caption("Score resumes against a job description using simple NLP-based keyword matching.")

default_jd = '''
Data Engineering Intern
Required skills: Python, SQL, Databricks, PySpark, Azure, ETL, Spark, Data Factory
'''

jd = st.text_area("Paste job description", value=default_jd, height=200)
uploaded_files = st.file_uploader("Upload one or more resumes (.txt)", type=["txt"], accept_multiple_files=True)

if st.button("Analyze Resumes"):
    if not uploaded_files:
        st.warning("Please upload at least one resume text file.")
    else:
        jd_keywords = extract_keywords(jd)
        results = []
        for file in uploaded_files:
            text = io.StringIO(file.getvalue().decode("utf-8")).read()
            score, matches = score_resume(text, jd_keywords)
            results.append({
                "resume_name": file.name,
                "score": score,
                "matched_keywords": ", ".join(matches),
            })
        df = pd.DataFrame(results).sort_values(by="score", ascending=False)
        st.subheader("Ranked Results")
        st.dataframe(df, use_container_width=True)
        st.subheader("Job Description Keywords")
        st.write(", ".join(sorted(jd_keywords)))
