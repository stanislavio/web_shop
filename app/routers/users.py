from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login", response_model=schemas.User)
def login_user(username: str = Body(), password: str = Body(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None or user.hashed_password != password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return user


@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
