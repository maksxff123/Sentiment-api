import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, recall_score, precision_score

df = pd.read_csv("IMDB.csv", engine="python")

X = df['review']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = TfidfVectorizer(max_features=10000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

pred = model.predict(X_test_tfidf)

print("Accuracy: ", round(accuracy_score(y_test, pred), 3))
print("Recall: ", round(recall_score(y_test, pred, pos_label='positive'), 3))
print("Precision: ", round(precision_score(y_test, pred, pos_label='positive'), 3))



joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model saved")