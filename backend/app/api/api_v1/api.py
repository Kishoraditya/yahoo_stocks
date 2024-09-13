from fastapi import APIRouter
from app.api.api_v1.endpoints import stocks, users

api_router = APIRouter()
api_router.include_router(stocks.router, prefix="/stocks", tags=["stocks"])
api_router.include_router(users.router, prefix="/users", tags=["users"])