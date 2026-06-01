from fastapi import APIRouter, Header

from services.analysis_service import analyze_repository

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

@router.post("")
def analyze(
    owner: str,
    repo: str,
    authorization: str = Header(None)
):

    token = ""

    if authorization:
        token = authorization.replace(
            "Bearer ",
            ""
        )

    return analyze_repository(
        owner,
        repo,
        token
    )