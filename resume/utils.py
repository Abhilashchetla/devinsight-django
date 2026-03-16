import pdfplumber

def extract_text(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:
            text += page.extract_text()

    return text

skills = [
    "python",
    "django",
    "sql",
    "machine learning",
    "data science",
    "html",
    "css",
    "javascript"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills