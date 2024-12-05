from sqlalchemy import Column, String, Integer
from src.core.connection_db import Base

class User(Base):
    __tablename__ = "users"  # Nombre de la tabla
    id = Column(Integer, primary_key=True, index=True)
    name_user = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Rol(Base):
    __tablename__ = "rol"  # Nombre de la tabla
    id = Column(Integer, primary_key=True, index=True)
    type_user = Column(String, nullable=False)
    description = Column(String, nullable=False)