from django.shortcuts import render
from .models import Resume

def upload_resume(request):

    if request.method == "POST":

        file = request.FILES['resume']

        Resume.objects.create(
            user=request.user,
            file=file
        )

        return render(request,"upload_success.html")

    return render(request,"upload_resume.html")
