from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import dependencies
from app.services import stock_data, analysis
from app.schemas.stock import StockCreate, StockInDB

router = APIRouter()

@router.post("/", response_model=StockInDB)
def create_stock(stock: StockCreate, db: Session = Depends(dependencies.get_db)):
    db_stock = stock_data.fetch_stock_data(stock.symbol, db)
    return db_stock

@router.get("/{symbol}/analysis")
def get_stock_analysis(symbol: str, db: Session = Depends(dependencies.get_db)):
    stock = db.query(Stock).filter(Stock.symbol == symbol).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    historical_data = yf.Ticker(symbol).history(period="1y")
    analysis_result = analysis.perform_technical_analysis(historical_data)
    prediction = analysis.predict_stock_price(historical_data)
    
    return {
        "technical_analysis": analysis_result.to_dict(),
        "price_prediction": prediction.tolist()
    }

