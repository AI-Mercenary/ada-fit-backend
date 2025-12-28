import os
from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "AdaFit Backend"
    API_V1_STR: str = "/api"
    
    # Cors
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:8080", "http://localhost:3000"]
    
    # Database
    DATABASE_URL: str = "sqlite:///./sql_app.db"
    
    # Gemini
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")

    class Config:
        case_sensitive = True

settings = Settings()
