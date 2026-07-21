import re

from pathlib import Path


def load_skills_database():
    """
    Load skills from the text file.
    """

    skills_file = Path("data/skills_database.txt")

    with open(skills_file, "r", encoding="utf-8") as file:
        skills = [line.strip().lower() for line in file if line.strip()]

    return skills

def extract_name(text):
    """
    Extract candidate name.
    Assumes the first non-empty line is the name.
    """

    lines = text.split()

    if len(lines) >= 2:
        return lines[0].title() + " " + lines[1].title()

    return "Unknown"


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    skills_database = load_skills_database()
    
    found_skills = []

    for skill in skills_database:

        if skill in text:

            found_skills.append(skill.title())

    return sorted(list(set(found_skills)))


def build_candidate_profile(text):

    profile = {

        "name": extract_name(text),

        "skills": extract_skills(text),

        "full_text": text

    }

    return profile