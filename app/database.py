from sqlalchemy import create_engine

import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/ai_course_recommendation"
)
engine = create_engine(DATABASE_URL)

print("Database connected successfully")