from sqlalchemy.orm import Session
from src.models.user_model import User
from src.schemas.user import UserCreate

def create_user (db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users (db:Session): 
    return db.query(User).all
