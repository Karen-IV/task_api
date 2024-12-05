from pydantic_settings import BaseSettings
#from typing import ClassVar

class Settings(BaseSettings):
    DATABASE_URL: str  # Indica que esta variable es de tipo string

    class Config:
        env_file = "C:\\Users\\DELL\\Documents\\entornos_virtuales\\task_app\\.env"  # O la ruta completa si está fuera de la carpeta actual
settings = Settings()
