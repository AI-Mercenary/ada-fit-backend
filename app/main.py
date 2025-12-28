from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
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

from app.routes import today, profile

# Include routers
app.include_router(today.router, prefix="/api/today", tags=["today"])
app.include_router(profile.router, prefix="/api/profile", tags=["profile"])
