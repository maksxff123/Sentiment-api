from fastapi import FastAPI
from app.routers.analyze import router as analyze_router
from app.routers.auth import router as auth_router
from app.core.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sentiment API")

app.include_router(analyze_router)
app.include_router(auth_router)

