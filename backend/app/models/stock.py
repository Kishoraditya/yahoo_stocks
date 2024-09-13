from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Stock(Base):
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    company_name = Column(String)
    current_price = Column(Float)
    last_updated = Column(DateTime)


