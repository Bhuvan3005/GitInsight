from fastapi import APIRouter,HTTPException
from fastapi.responses import RedirectResponse
from services.oauth_service import get_github_oauth_url,exchange_code_for_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/login")
def github_login():
    """
    Redirect user to GitHub OAuth page
    """

    oauth_url = get_github_oauth_url()

    return RedirectResponse(url=oauth_url)

@router.get("/callback")
def github_callback(code: str):

    access_token = exchange_code_for_token(code)

    if not access_token:
        raise HTTPException(
            status_code=400,
            detail="Failed to get access token"
        )


    return RedirectResponse(f"http://localhost:8501/repo?token={access_token}")

