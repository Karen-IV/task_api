from fastapi import FastAPI, Depends, Request, HTTPException
from sqlalchemy.orm import Session
#from src.routers.user import get_db
from src.crud.user import create_user, get_user_by_id, update_user, get_users, delete_user
from src.schemas.user import UserCreate
from src.models.user_model import Rol, User
from src.core.connection_db import SessionLocal
from datetime import datetime


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/', tags=['Home'])
def home(request: Request):
    return {"message": "Home"}

@app.post("/users/create/", tags=["CRUD_USERS"])
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):

    db_role = db.query(Rol).filter(Rol.id == user.rol_id).first()
    if not db_role:
        raise HTTPException(status_code=400, detail="Rol not found")
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created_user = create_user(db, user)
    return created_user

@app.get("/users/get/", tags=["CRUD_USERS"])
def read_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users

@app.get("/users/get/user/{user_id}", tags=["CRUD_USERS"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", tags=["CRUD_USERS"])
def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    # Llama a la función para actualizar el usuario
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User updated successfully", "user": updated_user}

@app.delete("/users/{user_id}", tags=["CRUD_USERS"])
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

