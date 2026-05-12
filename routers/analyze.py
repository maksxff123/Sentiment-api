from fastapi import APIRouter, Depends
from app.schemas.sentiment import AnalyzeRequest, AnalyzeResponse
from app.services.ml import predict_sentiment
from app.core.security import get_current_user


router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest, current_user: dict=Depends(get_current_user)):
    result = predict_sentiment(request.text)
    return result

