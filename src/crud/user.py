from sqlalchemy.orm import Session
from src.models.user_model import User
from src.utils.utils import hash_password  # Asegúrate de importar la función hash
from datetime import datetime
from src.schemas.user import UserCreate
from fastapi import HTTPException

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

def update_user(db: Session, user_id: int, user: UserCreate):
    # Busca al usuario existente en la base de datos
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Actualiza los campos proporcionados dinámicamente
    update_data = user.model_dump(exclude_unset=True)  # Solo incluye campos enviados por el cliente
    if "hashed_password" in update_data:
        update_data["hashed_password"] = hash_password(update_data["hashed_password"])  # Hashea si es necesario
    
    for key, value in update_data.items():
        setattr(db_user, key, value)  # Actualiza los atributos dinámicamente

    # Confirma los cambios en la base de datos
    db.commit()
    db.refresh(db_user)
    
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
