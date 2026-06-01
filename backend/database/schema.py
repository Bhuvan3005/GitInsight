from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# -------------------------
# User Schemas
# -------------------------

class UserBase(BaseModel):
    github_id: str
    username: str
    email: Optional[str] = None
    avatar_url: Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# -------------------------
# Repository Schemas
# -------------------------

class RepositoryBase(BaseModel):
    github_repo_id: int
    owner: str
    repo_name: str
    description: Optional[str] = None
    primary_language: Optional[str] = None
    stars: int
    forks: int
    open_issues: int


class RepositoryResponse(RepositoryBase):
    id: int
    last_analyzed_at: Optional[datetime]

    class Config:
        from_attributes = True


# -------------------------
# Analysis Schemas
# -------------------------

class AnalysisCreate(BaseModel):
    repository_id: int


class AnalysisResponse(BaseModel):
    id: int
    repository_id: int

    summary: str
    project_purpose: str
    tech_stack: str

    health_score: float
    documentation_score: float

    strengths: str
    weaknesses: str
    recommendations: str

    generated_at: datetime

    class Config:
        from_attributes = True