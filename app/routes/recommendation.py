from fastapi import APIRouter

from app.services.recommendation_service import (
    get_recommendations
)

router = APIRouter()


@router.get("/recommend/{student_id}")
def recommend(student_id: int):

    recommendations = get_recommendations(student_id)

    results = []

    for _, row in recommendations.iterrows():

        results.append({
            "course_title": row["course_title"],
            "subject": row["subject"],
            "difficulty": row["difficulty"],
            "success_probability": round(
                row["success_probability"] * 100,
                2
            ),
            "final_score": round(
                row["final_score"],
                2
            ),
            "recommendation_reason": 
            row["recommendation_reason"]
        })

    return results