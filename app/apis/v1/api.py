# backend/app/apis/v1/api.py
from fastapi import APIRouter
from .endpoints import auth, listings # Import listings

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(listings.router, prefix="/listings", tags=["Listings"])

@api_router.get("/test") # Keep for testing if needed
async def test_v1_route():
    return {"message": "API V1 is working!"}