from app.services.prediction_service import predict_success
import pandas as pd

students = pd.read_csv("data/processed/students.csv")
courses = pd.read_csv("data/processed/courses.csv")
interactions = pd.read_csv("data/processed/student_interactions.csv")

data = interactions.merge(
    students,
    on="student_id"
)

data = data.merge(
    courses,
    on="course_id"
)

data["performance_score"] = (
    data["quiz_score"] * 0.6 +
    data["completion_rate"] * 0.4
)

def calculate_recommendation_score(row):

    score = 0

    if row["subject"] == row["preferred_subject"]:
        score += 30

    if row["performance_score"] < 60:
        score += 40

    if (
        row["skill_level"] == "Beginner"
        and row["difficulty"] == "Beginner"
    ):
        score += 20

    score += row["completion_rate"] * 0.1

    return score


data["recommendation_score"] = data.apply(
    calculate_recommendation_score,
    axis=1
)

data["success_probability"] = data.apply(
    lambda row: predict_success(
        row["quiz_score"],
        row["completion_rate"]
    ),
    axis=1
)

data["final_score"] = (
    data["recommendation_score"] * 0.4
    +
    data["success_probability"] * 100 * 0.6
)

def get_recommendations(student_id: int):

    student_data = data[
        data["student_id"] == student_id
    ].copy()

    ranked_courses = student_data.sort_values(
        by="final_score",
        ascending=False
    )

    return ranked_courses[
[
    "course_title",
    "subject",
    "difficulty",
    "success_probability",
    "final_score",
    "recommendation_reason"
]
].drop_duplicates().head(5)

def generate_reason(row):

    reasons = []

    if row["success_probability"] > 0.8:
        reasons.append(
            "High predicted success probability"
        )

    if row["subject"] == row["preferred_subject"]:
        reasons.append(
            "Matches preferred subject"
        )

    if row["difficulty"] == "Beginner":
        reasons.append(
            "Suitable difficulty level"
        )

    if not reasons:
        reasons.append(
            "Recommended based on overall ranking"
        )    

    return ", ".join(reasons)

data["success_probability"]

data["recommendation_reason"] = data.apply(
    generate_reason,                                    
    axis=1
)