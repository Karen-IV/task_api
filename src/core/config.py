from pydantic_settings import BaseSettings

class Settings (BaseSettings):
    DATABASE_URL: str  # Indica que esta variable es de tipo string

    class Config:
        env_file = ".env"  # O la ruta completa si está fuera de la carpeta actual
settings=Settings()
