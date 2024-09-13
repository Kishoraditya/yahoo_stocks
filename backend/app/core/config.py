from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "yahoo_stocks"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    DATABASE_URL: str
    API_KEY_YAHOO_FINANCE: str

    class Config:
        env_file = ".env"

settings = Settings()
