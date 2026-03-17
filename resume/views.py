from django.shortcuts import render
from .models import Resume
from .utils import extract_text, extract_skills

def upload_resume(request):

    if request.method == "POST":

        file = request.FILES['resume']

        resume = Resume.objects.create(
            user=request.user,
            file=file
        )

        text = extract_text(resume.file.path)

        skills = extract_skills(text)

        return render(request, "resume_result.html", {"skills": skills})

    return render(request, "upload_resume.html")