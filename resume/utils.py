import pdfplumber

def extract_text(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:
            text += page.extract_text()

    return text

skills = {
    "python":90,
    "django":80,
    "sql":70,
    "machine learning":75,
    "data science":70,
    "html":60,
    "css":60,
    "javascript":65,
    "RESt APIS":60,
    "Java":85
}

def extract_skills(text):

    text = text.lower()

    found_skills = {}

    for skill,score in skills.items():
        if skill in text:
            found_skills[skill] = score

    return found_skills