from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ

SQLALCHEMY_DATABASE_URL = environ.get("DATABASE_URL")

# Ensure SSL mode is set
if 'sslmode=require' not in SQLALCHEMY_DATABASE_URL:
    SQLALCHEMY_DATABASE_URL += '?sslmode=require'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        