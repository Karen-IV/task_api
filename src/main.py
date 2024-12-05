from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from src.models.user_model import User
from src.core.connection_db import get_db, Base, engine

app = FastAPI()

# Crear tablas en la base de datos
print("Creando tablas para la base de datos...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas exitosamente...")

@app.get('/', tags=['Home'])
def home(request: Request):
    return {"message": "Home"}

@app.post("/users/", tags=["CRUD_USERS"])
def create_user(name_user: str, email: str, db: Session = Depends(get_db)):
    try:
        user = User(name_user=name_user, email=email)
        db.add(user)  # Agrega el nuevo usuario a la base de datos
        db.commit()  # Guarda los cambios en la base de datos
        db.refresh(user)  # Actualiza el objeto usuario
        return user  # Devuelve el usuario recién creado
    except Exception as e:
        db.rollback()  # Revierte cambios si ocurre un error
        raise e

@app.get("/users/", tags=["CRUD_USERS"])
def read_users(db: Session = Depends(get_db)):  # Inyecta una sesión de base de datos
    return db.query(User).all()  # Consulta todos los usuarios
