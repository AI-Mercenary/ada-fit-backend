import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    PROJECT_NAME: str = "AdaFit Backend"
    API_V1_STR: str = "/api"
    
    # Cors
    @property
    def BACKEND_CORS_ORIGINS(self) -> list[str]:
        origins = [
            "http://localhost:5173", 
            "http://localhost:8080", 
            "http://localhost:3000",
            "http://192.168.29.192:8080" # Network device access
        ]
        if self.FRONTEND_URL:
            origins.append(self.FRONTEND_URL)
        if self.VERCEL_URL:
            origins.append(self.VERCEL_URL)
        return origins
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
    
    # Gemini
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")
    AGENT_MODEL: str = os.getenv("AGENT_MODEL", "gemini-pro")
    
    # CORS & Environment
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:5173")
    VERCEL_URL: str = os.getenv("VERCEL_URL", "")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    class Config:
        case_sensitive = True

settings = Settings()
