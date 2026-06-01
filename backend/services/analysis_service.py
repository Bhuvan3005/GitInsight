import requests
import base64
from services.llm_service import generate_analysis




def analyze_repository(owner: str, repo: str):

    headers = {
        "Accept": "application/vnd.github+json"
    }

    # Repository Metadata
    repo_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers
    )

    repo_info = repo_response.json()

    # Languages
    lang_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/languages",
        headers=headers
    )

    languages = lang_response.json()

    # README
    readme_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/readme",
        headers=headers
    )

    readme_text = ""

    if readme_response.status_code == 200:
        readme_data = readme_response.json()

        if "content" in readme_data:
            readme_text = base64.b64decode(
                readme_data["content"]
            ).decode("utf-8", errors="ignore")

    # File Tree
    default_branch = repo_info.get("default_branch", "main")

    tree_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1",
        headers=headers
    )

    files = []

    if tree_response.status_code == 200:
        tree_data = tree_response.json()

        files = [
            item["path"]
            for item in tree_data.get("tree", [])
            if item["type"] == "blob"
        ]

    # Build Context for LLM
    context = {
        "repository_name": repo_info.get("name"),
        "description": repo_info.get("description"),
        "stars": repo_info.get("stargazers_count"),
        "forks": repo_info.get("forks_count"),
        "language": repo_info.get("language"),
        "languages": languages,
        "readme": readme_text[:5000],
        "files": files[:200]
    }

    report = generate_analysis(context)

    return {
        "repo": repo,
        "analysis": report
    }