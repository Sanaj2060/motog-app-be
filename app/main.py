# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.apis.v1.api import api_router
from app.core.config import settings

# Create database tables
print("Attempting to create database tables...")
try:
    Base.metadata.create_all(bind=engine)
    print("Database tables should be created if they didn't exist.")
except Exception as e:
    print(f"Error creating database tables: {e}")

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
    version="0.1.0"
)

# CORS Middleware configuration
origins = [
    "http://localhost",
    "http://localhost:3000", # Your Next.js frontend origin
    "http://127.0.0.1:3000",  # Another common local development address
    "http://192.168.1.3:3000",
    "https://motog-app-fe.vercel.app",
    "https://www.gomotog.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to MotoG API!"}

@app.get(f"{settings.API_V1_STR}/test")
def test_api_v1():
    return {"message": "API V1 is working!"}