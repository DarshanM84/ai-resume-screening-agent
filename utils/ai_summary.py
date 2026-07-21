from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_recruiter_summary(profile, score, job_profile):
    """
    Generate an AI recruiter summary using Gemini.
    """

    prompt = f"""
You are an experienced Technical Recruiter.

Job Description:
{job_profile}

Candidate Profile:
{profile}

Candidate Scores:
Overall Match: {score["final_score"]:.1f}%
Skill Match: {score["skill_score"]:.1f}%
Semantic Match: {score["semantic_score"]:.1f}%

Write a recruiter summary with the following sections:

1. Overall Evaluation
2. Strengths
3. Missing Skills
4. Interview Recommendation

Keep the response professional.
Limit to about 120 words.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}"


# Test the file independently
if __name__ == "__main__":

    demo_profile = {
        "name": "Darshan M",
        "skills": ["Python", "Flask", "SQL"]
    }

    demo_score = {
        "final_score": 82.4,
        "skill_score": 90,
        "semantic_score": 75
    }

    demo_job = {
        "skills": ["Python", "Flask", "SQL", "REST API"]
    }

    print(generate_recruiter_summary(
        demo_profile,
        demo_score,
        demo_job
    ))