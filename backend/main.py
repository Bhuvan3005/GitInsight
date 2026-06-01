from fastapi import FastAPI
from routers.auth import router as auth_router
from routers.repositories import router as repo_router
from routers.analyse import router as analyse_router

app = FastAPI(
    title="GitInsight API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(repo_router)
app.include_router(analyse_router)


@app.get("/")
def root():
    return {
        "message": "GitInsight Backend Running"
    }

