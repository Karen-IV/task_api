from sqlalchemy import Column, Integer
from src.core.connection_db import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key = True, index = True)