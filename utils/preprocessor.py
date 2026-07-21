import re


def clean_text(text):
    """
    Clean extracted resume or job description text.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove unwanted symbols
    text = re.sub(r"[^\w\s]", " ", text)

    # Remove extra spaces again
    text = re.sub(r"\s+", " ", text)

    return text.strip()