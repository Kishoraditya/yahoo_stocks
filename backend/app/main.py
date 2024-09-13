from fastapi import FastAPI
from app.api.endpoints import user, stock
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(stock.router, prefix="/stocks", tags=["stocks"])

