import yfinance as yf
from app.models.stock import Stock
from sqlalchemy.orm import Session

def fetch_stock_data(symbol: str, db: Session):
    stock = yf.Ticker(symbol)
    info = stock.info
    
    db_stock = Stock(
        symbol=symbol,
        company_name=info.get('longName'),
        current_price=info.get('currentPrice'),
        last_updated=datetime.utcnow()
    )
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock

