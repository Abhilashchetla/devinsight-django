from django.shortcuts import render
from .models import Resume
from .utils import extract_text, extract_skills,calculate_score,find_missing_skills

def upload_resume(request):

    if request.method == "POST":

        file = request.FILES['resume']

        resume = Resume.objects.create(
            user=request.user,
            file=file
        )

        text = extract_text(resume.file.path)

        skills = extract_skills(text)
        score = calculate_score(skills)
        missing_skills = find_missing_skills(skills)

        return render(request, "resume_result.html", {"skills": skills,"score":score,"missing_skills":missing_skills})

    return render(request, "upload_resume.html")