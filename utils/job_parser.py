from utils.candidate_parser import load_skills_database
def extract_job_title(text):
    """
    Assumes the first line contains the job title.
    """

    lines = text.split()

    if len(lines) >= 2:
        return lines[0].title() + " " + lines[1].title()

    return "Unknown Role"


def extract_required_skills(text):

    skills_database = load_skills_database()

    skills = []

    for skill in skills_database:

        if skill in text:

            skills.append(skill.title())

    return sorted(list(set(skills)))


def build_job_profile(text):

    profile = {

        "title": extract_job_title(text),

        "skills": extract_required_skills(text),

        "full_text": text

    }

    return profile