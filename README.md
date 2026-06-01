# Performance-Aware Hybrid Course Recommendation System

## Overview

This project is an AI-powered course recommendation system designed for educational and tutoring platforms. The system combines Content-Based Filtering, Collaborative Filtering, and Random Forest-based Student Success Prediction to provide personalized and explainable course recommendations.

The proposed model was developed as part of a Master's research project and evaluated against traditional recommendation approaches.

## Key Features

* Content-Based Recommendation
* Collaborative Filtering
* Hybrid Recommendation Engine
* Random Forest Success Prediction
* Explainable Recommendations
* FastAPI REST API
* PostgreSQL Integration
* Docker Support

## Experimental Results

| Model                   | Precision@5 |
| ----------------------- | ----------: |
| Popularity-Based        |      0.0667 |
| Content-Based           |      0.1756 |
| Collaborative Filtering |      0.2711 |
| Hybrid + Random Forest  |      0.4622 |

The proposed model achieved the highest Precision@5 and improved recommendation quality by approximately 70.5% compared to Collaborative Filtering.

## Technology Stack

* Python
* Scikit-Learn
* Pandas
* NumPy
* FastAPI
* PostgreSQL
* Docker
* Jupyter Notebook

## API Endpoint

GET /recommend/{student_id}

Returns personalized course recommendations with predicted success probability and recommendation explanations.

## Future Enhancements

* Neural Collaborative Filtering
* Knowledge Graph Integration
* Graph Neural Networks
* Real-Time Recommendation Pipeline
* Cloud Deployment
