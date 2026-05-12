# Sentiment Analysis API

NLP microservice for text sentiment classification — deployed as a REST API with JWT authentication and database persistence.

## Tech Stack
- **FastAPI** — REST API framework
- **scikit-learn** — ML model (TF-IDF + Logistic Regression, ~89% accuracy)
- **PostgreSQL + SQLAlchemy** — database
- **JWT + bcrypt** — authentication

## Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login, returns JWT token |
| POST | `/analyze` | Sentiment analysis (requires token) |

## Getting Started

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create `.env` file based on `.env.example`
4. Train the model:
```bash
python app/ml_model/train.py
```
5. Run the server:
```bash
uvicorn app.main:app --reload
```
6. Open docs: `http://127.0.0.1:8000/docs`

## .env.example
## Dataset
Model is trained on [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) from Kaggle.

