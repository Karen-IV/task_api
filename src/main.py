from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from src.models.user_model import User
from src.routers.user import get_db
from src.crud.user import create_user
from src.schemas.user import UserResponse,UserCreate

app = FastAPI()

@app.get('/', tags=['Home'])
def home(request: Request):
    return {"message": "Home"}

@app.post("/users/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/", tags=["CRUD_USERS"])
def read_users(db: Session = Depends(get_db)):  # Inyecta una sesión de base de datos
    return db.query(User).all()  # Consulta todos los usuarios
