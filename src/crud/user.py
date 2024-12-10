from sqlalchemy.orm import Session
from src.models.user_model import User
from src.utils.utils import hash_password  # Asegúrate de importar la función hash
from datetime import datetime
from src.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = hash_password(user.hashed_password)
    db_user = User(
        name_user=user.name_user,
        email=user.email,
        hashed_password=hashed_password,
        rol_id=user.rol_id,
        #created_at=datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db:Session): 
    return db.query(User).all()

def get_user_by_id(db:Session, id = int):
    return db.query(User).filter(User.id == id).first()

def update_user(db: Session, user_id: int, name_user: str = None, hashed_password: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    if name_user:
        user.name_user = name_user
    if hashed_password:
        user.hashed_password = hash_password(hashed_password)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
