import requests

def get_user_repos(username: str, token: str = None):

    headers = {
        "Accept": "application/vnd.github+json"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        headers=headers
    )

    return response.json()