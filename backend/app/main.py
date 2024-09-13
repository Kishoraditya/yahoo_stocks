from fastapi import FastAPI
from app.api.endpoints import user, stock
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)


from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1.api import api_router



app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to StockInsights API"}