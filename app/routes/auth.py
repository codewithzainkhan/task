from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import os

from .. import models, schemas
from ..deps import get_db
from ..auth import hash_password, verify_password, create_access_token
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter_by(username=user.username).first():
        raise HTTPException(status_code=400, detail="User exists")

    new_user = models.User(
        username=user.username,
        password_hash=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}


@router.post("/login", response_model=schemas.Token)
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter_by(username=form.username).first()
    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        {"user_id": user.id},
        expires_minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")),
    )
    return {"access_token": token, "token_type": "bearer"}
