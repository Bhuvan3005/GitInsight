import requests


def get_user_repos(username: str):

    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        headers={
            "Accept": "application/vnd.github+json"
        }
    )

    return response.json()