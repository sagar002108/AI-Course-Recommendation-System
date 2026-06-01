# 🎓 Performance-Aware Hybrid Course Recommendation System

## Overview

The Performance-Aware Hybrid Course Recommendation System is an AI-powered recommendation engine designed for educational and tutoring platforms. The system combines Content-Based Filtering, Collaborative Filtering, and Random Forest-based Student Success Prediction to generate personalized, explainable, and performance-aware course recommendations.

This project was developed as part of a Master's research project and demonstrates how machine learning techniques can improve recommendation quality within online learning environments.

---

## Research Objectives

* Develop a hybrid course recommendation system for educational platforms.
* Improve recommendation accuracy using collaborative and content-based recommendation techniques.
* Incorporate student success prediction into recommendation ranking.
* Evaluate recommendation quality using Precision@5.
* Build a deployable API architecture suitable for real-world integration.

---

## System Architecture

```text
                    Student Data
                          │
                          ▼
              Student Profile Processing
                          │
                          ▼
                 Course Information
                          │
                          ▼
         ┌─────────────────────────────┐
         │ Content-Based Recommendation │
         └─────────────────────────────┘
                          │
                          ▼
         ┌─────────────────────────────┐
         │ Collaborative Filtering     │
         └─────────────────────────────┘
                          │
                          ▼
         ┌─────────────────────────────┐
         │ Random Forest Student       │
         │ Success Prediction Model    │
         └─────────────────────────────┘
                          │
                          ▼
         ┌─────────────────────────────┐
         │ Hybrid Ranking Engine       │
         └─────────────────────────────┘
                          │
                          ▼
                 FastAPI REST API
                          │
                          ▼
                Course Recommendations
```

---

## Key Features

✅ Content-Based Recommendation

✅ Collaborative Filtering

✅ Hybrid Recommendation Engine

✅ Random Forest Student Success Prediction

✅ Explainable Recommendations

✅ FastAPI REST API

✅ PostgreSQL Integration

✅ Docker Containerization

✅ Model Evaluation Framework

---

## Recommendation Strategy

The final recommendation score is generated using:

```text
Final Recommendation Score =
(Recommendation Score × 0.4)
+
(Predicted Success Probability × 100 × 0.6)
```

Where:

* Recommendation Score comes from the hybrid recommendation engine.
* Success Probability is predicted using the Random Forest model.
* Final ranking prioritizes both recommendation relevance and likelihood of student success.

---

## Experimental Results

| Model                   | Precision@5 |
| ----------------------- | ----------: |
| Popularity-Based        |      0.0667 |
| Content-Based           |      0.1756 |
| Collaborative Filtering |      0.2711 |
| Hybrid + Random Forest  |      0.4622 |

### Performance Improvement

| Comparison              | Improvement |
| ----------------------- | ----------: |
| Hybrid vs Content-Based |     163.22% |
| Hybrid vs Collaborative |      70.49% |
| Hybrid vs Popularity    |     592.98% |

The proposed Hybrid Recommendation System achieved the highest Precision@5 and significantly outperformed traditional recommendation approaches.

---

## Key Achievements

* Developed four recommendation approaches:

  * Popularity-Based Recommendation
  * Content-Based Recommendation
  * Collaborative Filtering
  * Hybrid Recommendation System

* Achieved a Precision@5 score of 0.4622.

* Improved recommendation accuracy by:

  * 163.22% over Content-Based Recommendation
  * 70.49% over Collaborative Filtering
  * 592.98% over Popularity-Based Recommendation

* Built a complete REST API using FastAPI.

* Containerized the entire application using Docker and Docker Compose.

* Integrated PostgreSQL for scalable data management.

---

## Results Visualization

### Model Performance Comparison

![Precision Comparison](results/precision_comparison.png)

### Swagger API Documentation

![Swagger API](results/swagger_api.png)

### Recommendation Output

![Recommendation Output](results/recommendation_output.png)

---

## API Documentation

### Recommendation Endpoint

```http
GET /recommend/{student_id}
```

### Example Request

```http
GET /recommend/1
```

### Example Response

```json
[
  {
    "course_title": "Course 35",
    "subject": "Programming",
    "difficulty": "Advanced",
    "success_probability": 100.0,
    "final_score": 75.12,
    "recommendation_reason": "High predicted success probability, Matches preferred subject"
  }
]
```

---

## Project Structure

```text
AI_Course_Recommendation_System
│
├── app
│   ├── routes
│   ├── services
│   ├── database.py
│   └── main.py
│
├── training
│   └── train_success_model.py
│
├── data
│   ├── raw
│   └── processed
│
├── models
│   └── student_success_model.pkl
│
├── notebooks
│   ├── 01_content_based.ipynb
│   ├── 02_collaborative_filtering.ipynb
│   ├── 03_hybrid_recommendation.ipynb
│   └── 04_model_evaluation.ipynb
│
├── results
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── test_prediction.py
```

---

## Technology Stack

### Machine Learning

* Scikit-Learn
* Random Forest
* Content-Based Filtering
* Collaborative Filtering
* Hybrid Recommendation System

### Backend

* FastAPI
* Python

### Database

* PostgreSQL

### Deployment

* Docker
* Docker Compose

### Data Processing

* Pandas
* NumPy

---

## Installation

### Clone Repository

```bash
git clone https://github.com/sagar002108/AI-Course-Recommendation-System.git
cd AI-Course-Recommendation-System
```

### Start Application

```bash
docker compose up --build
```

### Open API Documentation

```text
http://localhost:8001/docs
```

---

## Future Enhancements

* XGBoost Success Prediction
* Neural Collaborative Filtering (NCF)
* Knowledge Graph Integration
* Graph Neural Networks (GNN)
* Learning Path Recommendation
* Reinforcement Learning-Based Personalization
* Cloud Deployment (AWS, Azure, GCP)

---

## Research Contribution

This research proposes a Performance-Aware Hybrid Recommendation Framework that combines recommendation relevance with predicted student success.

Unlike traditional recommendation systems that only consider user-item similarity, the proposed approach incorporates student performance prediction to improve recommendation quality and learning outcomes in educational environments.

---

## Citation

If you use this work in academic research, please cite:

Sagar

Performance-Aware Hybrid Course Recommendation System

Master's Research Project

Asian Institute of Technology (AIT)

2026

---

## License

This project is released under the MIT License.

---

## Author

Sagar

Master of Engineering in Computer Science

