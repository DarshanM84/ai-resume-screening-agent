import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📄 AI Resume Screening Agent")

st.markdown(
    """
    Welcome to the **Rooman AI Resume Screening Agent**.

    This application compares multiple resumes against a Job Description
    and ranks the best candidates using AI.
    """
)

st.divider()

# --------------------------------------------------
# Job Description Upload
# --------------------------------------------------

st.header("📄 Step 1 : Upload Job Description")

job_description = st.file_uploader(
    "Choose a Job Description file",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=False
)

st.divider()

# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

st.header("📑 Step 2 : Upload Candidate Resumes")

uploaded_resumes = st.file_uploader(
    "Upload one or more resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

st.divider()

# --------------------------------------------------
# Demo Option
# --------------------------------------------------

st.header("🧪 Demo Mode")

use_sample_resumes = st.checkbox(
    "Use sample resumes included with the project"
)

st.divider()

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

if st.button("🚀 Analyze Candidates"):

    st.success("Button clicked successfully!")

    if job_description:
        st.write("📄 Job Description uploaded:")
        st.write(job_description.name)

    else:
        st.warning("Please upload a Job Description.")

    if uploaded_resumes:
        st.write(f"📑 {len(uploaded_resumes)} resume(s) uploaded.")

    if use_sample_resumes:
        st.info("Demo Mode Enabled")