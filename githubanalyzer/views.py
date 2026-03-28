import requests
from django.shortcuts import render

def github_analysis(request):

    if request.method == "POST":

        username = request.POST['username']

        if not username:
            return render(request, "github.html", {
                "error": "Please enter a GitHub username"
            })

        url = f"https://api.github.com/users/{username}/repos"
        
        response = requests.get(url)

        if response.status_code != 200:
            return render(request, "github.html", {
                "error": "Invalid GitHub username"
            })

        repos = response.json()

        # ✅ FIX: check first
        if not isinstance(repos, list):
            return render(request, "github.html", {
                "error": "Something went wrong. Try again."
            })

        # ✅ Now safe to use
        repo_count = len(repos)

        total_stars = 0
        languages = {}

        for repo in repos:

            total_stars += repo.get('stargazers_count', 0)

            lang = repo.get('language')

            if lang:
                languages[lang] = languages.get(lang, 0) + 1

        top_language = max(languages, key=languages.get) if languages else "N/A"

        # Rating logic
        if repo_count >= 15 and total_stars >= 20:
            rating = "Strong Profile 💪"
        elif repo_count >= 5:
            rating = "Moderate Profile 👍"
        else:
            rating = "Beginner Profile 🚀"

        return render(request, "github_result.html", {
            "repo_count": repo_count,
            "total_stars": total_stars,
            "top_language": top_language,
            "rating": rating
        })

    return render(request, "github.html")