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

def calculate_score(found_skills):

    total_possible = len(skills) * 10
    score = len(found_skills) * 10

    return int((score / total_possible) * 100)

required_skills = [
    "python",
    "django",
    "sql",
    "docker",
    "aws",
    "javascript"
    "Java"
]
def find_missing_skills(found_skills):

    missing = []

    for skill in required_skills:
        if skill not in found_skills:
            missing.append(skill)

    return missing