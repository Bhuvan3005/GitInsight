from fastapi import APIRouter, Header
from services.github_service import get_user_repos

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)

@router.get("/{username}")
def fetch_repositories(
    username: str,
    authorization: str = Header(None)
):
    token = None

    if authorization:
        token = authorization.replace("Bearer ", "")

    return get_user_repos(username, token)