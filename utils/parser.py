import fitz
from docx import Document


def read_pdf(uploaded_file):
    """
    Read text from a PDF file.
    """

    text = ""

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text


def read_docx(uploaded_file):
    """
    Read text from a DOCX file.
    """

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def read_txt(uploaded_file):
    """
    Read text from a TXT file.
    """

    return uploaded_file.read().decode("utf-8")


def extract_text(uploaded_file):
    """
    Automatically detect the file type
    and return extracted text.
    """

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return read_pdf(uploaded_file)

    elif filename.endswith(".docx"):
        return read_docx(uploaded_file)

    elif filename.endswith(".txt"):
        return read_txt(uploaded_file)

    else:
        return ""