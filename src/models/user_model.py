from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.core.connection_db import Base



class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    type_user = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    users = relationship("User", back_populates="rol")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name_user = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    number = Column(Integer, unique=True, nullable=True)
    rol_id = Column(Integer, ForeignKey("roles.id"))
    create_at = Column(DateTime, nullable=False, server_default=func.now())
    rol = relationship("Rol", back_populates="users")
    hashed_password = Column(String, nullable=False)


class StatusTask(Base):
    __tablename__ = "status_tasks"
    id = Column(Integer, primary_key=True, index=True)
    type_status = Column(String, nullable=False)
    create_at = Column(DateTime, nullable=False, server_default=func.now())
    tasks = relationship("Tasks", back_populates="status")

class Tasks(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title_task = Column(String, nullable=False)
    description_task = Column(String, nullable=True)
    status_id = Column(Integer, ForeignKey("status_tasks.id"))
    create_at = Column(DateTime, nullable=False, server_default=func.now())
    status = relationship("StatusTask", back_populates="tasks")

class StatusUser(Base):
    __tablename__ = "status_users"
    id = Column(Integer, primary_key=True, index=True)
    type_status = Column(String, nullable=False, unique=True)
