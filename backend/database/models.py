from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    github_id = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String)
    avatar_url = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)

    github_repo_id = Column(Integer, unique=True, nullable=False)

    owner = Column(String, nullable=False)
    repo_name = Column(String, nullable=False)

    description = Column(Text)
    primary_language = Column(String)

    stars = Column(Integer, default=0)
    forks = Column(Integer, default=0)
    open_issues = Column(Integer, default=0)

    last_analyzed_at = Column(DateTime)

    analyses = relationship(
        "RepositoryAnalysis",
        back_populates="repository",
        cascade="all, delete-orphan"
    )


class RepositoryAnalysis(Base):
    __tablename__ = "repository_analyses"

    id = Column(Integer, primary_key=True, index=True)

    repository_id = Column(
        Integer,
        ForeignKey("repositories.id"),
        nullable=False
    )

    summary = Column(Text)
    project_purpose = Column(Text)
    tech_stack = Column(Text)

    health_score = Column(Float)
    documentation_score = Column(Float)

    strengths = Column(Text)
    weaknesses = Column(Text)
    recommendations = Column(Text)

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    repository = relationship(
        "Repository",
        back_populates="analyses"
    )