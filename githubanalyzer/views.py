import requests
from django.shortcuts import render

def github_analysis(request):

    if request.method == "POST":

        username = request.POST['username']

        url = f"https://api.github.com/users/{username}/repos"

        response = requests.get(url)
        repos = response.json()

        repo_count = len(repos)

        total_stars = 0
        languages = {}

        for repo in repos:

            total_stars += repo.get('stargazers_count', 0)

            lang = repo.get('language')

            if lang:
                languages[lang] = languages.get(lang, 0) + 1

        # Find top language
        top_language = max(languages, key=languages.get) if languages else "N/A"

        # Profile strength logic
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
            "rating":rating
        })
    

    return render(request, "github.html")