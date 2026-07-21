import streamlit as st

from utils.parser import extract_text
from utils.preprocessor import clean_text
from utils.candidate_parser import build_candidate_profile
from utils.job_parser import build_job_profile
from utils.scorer import calculate_final_score
from utils.ranker import rank_candidates
from utils.ai_summary import generate_recruiter_summary
# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.main{
background:#0B0F19;
}

.block-container{
padding-top:2rem;
max-width:1200px;
}

h1,h2,h3{
font-family:'Segoe UI';
}

.stButton button{
height:60px;
font-size:20px;
font-weight:700;
border-radius:12px;
background:linear-gradient(90deg,#2563EB,#3B82F6);
color:white;
border:none;
transition:.3s;
}

.stButton button:hover{
transform:translateY(-2px);
box-shadow:0 10px 30px rgba(37,99,235,.45);
}

div[data-testid="stMetric"]{
background:#161B22;
padding:22px;
border-radius:16px;
border:1px solid #2A3441;
}

.stFileUploader{
background:#111827;
padding:25px;
border-radius:15px;
border:2px dashed #2563EB;
}

    /* Hide Streamlit heading anchor */
    [data-testid="stHeaderActionElements"]{
        display:none !important;
    }
            
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Title
# --------------------------------------------------

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

left, right = st.columns([1.3,1])

with left:

    st.markdown("""
    <div style="padding-top:25px;">
    <h1 style="
    font-size:72px;
    font-weight:800;
    color:white;
    line-height:1.05;
    margin-top:0px;
    margin-bottom:8px;
    ">

    🤖 AI Resume Screening Agent

    </h1>

    <h3 style="
    color:#60A5FA;
    font-size:40px;
    font-weight:600;
    margin-top:0px;
    margin-bottom:18px;
    ">

    Intelligent Resume Analysis & Candidate Ranking

    </h3>

    <p style="
    font-size:21px;
    color:#CBD5E1;
    line-height:1.8;
    margin-bottom:30px;
    max-width:700px;
    ">

    Our AI Resume Screening Agent extracts candidate skills,
    understands job requirements using semantic AI,
    generates recruiter insights,
    and intelligently ranks applicants to help recruiters
    hire faster and more accurately.

    </p>

    </div>
    """,
    unsafe_allow_html=True)

    c1,c2 = st.columns(2)

    with c1:
        st.success("✔ AI Skill Matching")
        st.success("🎯 Semantic Resume Analysis")
        st.success("🖥️ ATS-Compatible Screening")

    with c2:
        st.success("🌐 Gemini Recruiter Insights")
        st.success("🕶️ Intelligent Candidate Ranking")
        st.success("🪢 AI Hiring Recommendations")

with right:

    st.image(
        "assets/ai_hero.png",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)
st.divider()

# --------------------------------------------------
# Job Description Upload
# --------------------------------------------------

st.header("💼 Upload Job Description")

job_description = st.file_uploader(
    "Drag & Drop or Browse Job Description",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=False
)

st.divider()

# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

st.header("👥 Upload Candidate Resumes")

uploaded_resumes = st.file_uploader(
    "Drag & Drop Candidate Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

st.divider()

# --------------------------------------------------
# Demo Option
# --------------------------------------------------

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

left, center, right = st.columns([2,2,2])

with center:
    analyze = st.button(
        "🚀 Start AI Screening",
        use_container_width=True
    )

if analyze:

    if job_description:

        jd_text = extract_text(job_description)

        jd_text = clean_text(jd_text)
        job_profile = build_job_profile(jd_text)
        

    else:
        st.warning("Please upload a Job Description.")

    if uploaded_resumes and job_description:

        st.success(
            f"✅ Analysis Complete • {len(uploaded_resumes)} Candidate(s) Ranked Successfully"
        )

        candidate_results = []

        for resume in uploaded_resumes:

            text = extract_text(resume)

            text = clean_text(text)
            profile = build_candidate_profile(text)
            score = calculate_final_score(
                profile,
                job_profile
            )

            candidate_results.append(
                {
                    "profile": profile,
                    "score": score
                }
            )

        ranked_candidates = rank_candidates(candidate_results)

        # -----------------------------
        # Dashboard Statistics
        # -----------------------------

        total_candidates = len(candidate_results)

        best_score = ranked_candidates[0]["score"]["final_score"]

        avg_score = (
            sum(c["score"]["final_score"] for c in candidate_results)
            / total_candidates
        )

        st.markdown("## 📊 Recruitment Summary")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="👥 Candidates",
                value=total_candidates
            )

        with col2:
            st.metric(
                label="🏆 Best Match",
                value=f"{best_score:.1f}%"
            )

        with col3:
            st.metric(
                label="⭐ Average",
                value=f"{avg_score:.1f}%"
            )

        with col4:
            st.metric(
                label="⚡ Processing",
                value="AI Powered"
            )

        st.divider()

        st.header("🏆 Ranked Candidates")

        for rank, candidate in enumerate(ranked_candidates, start=1):

            profile = candidate["profile"]
            score = candidate["score"]

            st.markdown("---")

            st.markdown(
                """
                <div style="
                    background:#161b22;
                    border:1px solid #30363d;
                    border-radius:16px;
                    padding:25px;
                    margin-bottom:30px;
                ">
                """,
                unsafe_allow_html=True
            )

            st.markdown(f"## 🥇 Rank #{rank}")

            st.markdown(
                f"<h2 style='margin-bottom:0px;'>{profile['name']}</h2>",
                unsafe_allow_html=True
            )

            st.caption("AI Screened Candidate")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Overall Match",
                    f"{score['final_score']:.1f}%"
                )
                st.progress(score["final_score"] / 100)

            with col2:
                st.metric(
                    "Skill Match",
                    f"{score['skill_score']:.1f}%"
                )
                st.progress(score["skill_score"] / 100)

            with col3:
                st.metric(
                    "Semantic Match",
                    f"{score['semantic_score']:.1f}%"
                )
                st.progress(score["semantic_score"] / 100)

            # Match Badge
            score_value = score["final_score"]

            if score_value >= 80:
                st.success("⭐ Highly Recommended")

            elif score_value >= 60:
                st.info("✅ Recommended")

            elif score_value >= 40:
                st.warning("⚠ Needs Review")

            else:
                st.error("❌ Requires Manual Review")

            st.write("")

            # -----------------------------
            # AI Recruiter Summary Card
            # -----------------------------

            st.markdown("""
            <div style="
            background:#111827;
            padding:20px;
            border-radius:15px;
            border:1px solid #2d3748;
            margin-top:20px;
            margin-bottom:25px;
            ">
            """, unsafe_allow_html=True)

            st.markdown(
                "<h3 style='color:#4F8BF9;'>🤖 AI Recruiter Summary</h3>",
                unsafe_allow_html=True
            )

            with st.spinner("Generating AI Recommendation..."):

                summary = generate_recruiter_summary(
                    profile,
                    score,
                    job_profile
                )

            st.markdown(summary)

            st.markdown("</div>", unsafe_allow_html=True)

            # -----------------------------
            # Skills
            # -----------------------------

            st.markdown("### 🛠 Skills")

            skills = profile["skills"][:10]

            badges = ""

            for skill in skills:
                badges += (
                    f"<span style='"
                    "background:#238636;"
                    "padding:7px 14px;"
                    "border-radius:20px;"
                    "margin-right:8px;"
                    "margin-bottom:8px;"
                    "display:inline-block;"
                    "color:white;"
                    "font-weight:600;'>"
                    f"{skill}</span>"
                )

            st.markdown(badges, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    <div style="text-align:center;color:#94A3B8;padding:20px;">
        <b>AI Resume Screening Agent</b><br>
        Built using Streamlit • Gemini AI • NLP • Semantic Matching • Python
    </div>
    """,
    unsafe_allow_html=True
)

            


