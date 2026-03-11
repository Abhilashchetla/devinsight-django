from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def signup(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, "signup.html", {"error": "Passwords do not match"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request,"signup.html")

def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request,"login.html")


def dashboard(request):
    return render(request, "dashboard.html")

def logout_view(request):
    logout(request)
    return redirect('login')