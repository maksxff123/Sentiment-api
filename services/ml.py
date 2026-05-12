import joblib 

model = joblib.load("app/ml_model/model.pkl")
vectorizer = joblib.load("app/ml_model/vectorizer.pkl")



def predict_sentiment(text: str)->dict:
    text_tfidf = vectorizer.transform([text])

    lable = model.predict(text_tfidf)[0]

    proba = model.predict_proba(text_tfidf)[0]
    confidence=  round(max(proba)*100,2)

    return {
        "sentiment": lable,
        "confidence": confidence,
    }