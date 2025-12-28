from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
import logging
import os

# --- Logging Setup ---
# --- Logging Setup ---
handlers = [logging.StreamHandler()]
try:
    os.makedirs("logs", exist_ok=True)
    handlers.append(logging.FileHandler("logs/backend.log"))
except Exception:
    pass # Fallback to console only if read-only filesystem

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=handlers
)
logger = logging.getLogger(__name__)

# Import routes later

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to AdaFit API"}

@app.get("/health")
@app.get("/kaithhealthcheck")
@app.get("/kaithheathcheck") # Handle typo seen in logs
def health_check():
    return {"status": "ok"}

from app.routes import today, profile

# Include routers
app.include_router(today.router, prefix="/api/today", tags=["today"])
app.include_router(profile.router, prefix="/api/profile", tags=["profile"])
