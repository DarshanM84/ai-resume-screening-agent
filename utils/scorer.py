from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_similarity(candidate_text, job_text):
    """
    Compute semantic similarity using TF-IDF.
    """

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [candidate_text, job_text]
    )

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    return float(similarity)


def skill_score(candidate_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    matched = len(
        set(candidate_skills).intersection(set(job_skills))
    )

    return matched / len(job_skills)


def calculate_final_score(candidate_profile, job_profile):

    semantic = semantic_similarity(
        candidate_profile["full_text"],
        job_profile["full_text"]
    )

    skills = skill_score(
        candidate_profile["skills"],
        job_profile["skills"]
    )

    final = semantic * 0.25 + skills * 0.75

    return {
        "semantic_score": round(semantic * 100, 2),
        "skill_score": round(skills * 100, 2),
        "final_score": round(final * 100, 2),
    }