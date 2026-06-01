import joblib
import pandas as pd

model = joblib.load(
    "models/student_success_model.pkl"
)

def predict_success(
    quiz_score,
    completion_rate
):

    sample = pd.DataFrame([{
        "quiz_score": quiz_score,
        "completion_rate": completion_rate
    }])

    probability = model.predict_proba(
        sample
    )[0][1]

    return float(probability)