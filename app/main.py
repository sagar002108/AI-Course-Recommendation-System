from fastapi import FastAPI

from app.routes.recommendation import router

app = FastAPI(
    title="AI Course Recommendation System"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "AI Course Recommendation System Running"
    }