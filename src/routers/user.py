from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.connection_db import SessionLocal
from src.schemas.user import UserCreate
from src.crud.user import create_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.post("/users/", tags=["CRUD_USERS"])
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)