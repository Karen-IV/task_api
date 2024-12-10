from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Base para Rol
class RolBase(BaseModel):
    type_user: str = Field(..., title="Role Type", max_length=50)
    description: str = Field(..., title="Description", max_length=255)

# Esquema para crear un Rol
class RolCreate(RolBase):
    pass

# Esquema para salida de un Rol
class Rol(RolBase):
    id: int
    class Config:
        from_attributes = True

# Base para Usuario
class UserBase(BaseModel):
    name_user: str = Field(..., title="User Name", max_length=100)
    email: EmailStr = Field(..., title="Email Address")
    number: Optional[int] = Field(None, title="Phone Number", ge=1000000, le=9999999999)  # Validación básica para un número de teléfono
    rol_id: int = Field(..., title="Role ID")

# Esquema para crear un Usuario
class UserCreate(UserBase):
    #create_at: Optional[datetime] = Field(default_factory=datetime.now, title="Creation Timestamp")
    hashed_password: str = Field(..., title="Hashed Password", min_length=8)

# Esquema para salida de Usuario
class User(UserBase):
    id: int
    class Config:
        from_attributes = True
