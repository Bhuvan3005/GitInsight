from fastapi import APIRouter
from services.analysis_service import analyze_repository

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

@router.post("/")
def analyze(owner: str, repo: str):
    return analyze_repository(owner, repo)