from fastapi import APIRouter
from services.github_service import get_user_repos

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)

@router.get("/{username}")
def fetch_repositories(username: str):
    return get_user_repos(username)