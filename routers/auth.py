from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from app.core.database import get_db
from app.core.security import hash_password,verify_password,create_access_token
from app.models.user import User
from app.schemas.user import UserRegistre,TokenResponse


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=TokenResponse)
def registr(data: UserRegistre, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email ==data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email alredy registered")
    
    user = User(
        username = data.username,
        email = data.email,
        hashed_password = hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email==form_data.username).first()

    if not user:
       raise HTTPException(status_code=401, detail="User with this email not fouded")

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Password is incorrect")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


