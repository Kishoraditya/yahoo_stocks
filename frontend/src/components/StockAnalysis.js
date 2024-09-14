import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { fetchStockAnalysis } from '../services/api';
import { Line } from 'react-chartjs-2';

function StockAnalysis() {
  const { symbol } = useParams();
  const [analysisData, setAnalysisData] = useState(null);

  useEffect(() => {
    const loadAnalysis = async () => {
      const data = await fetchStockAnalysis(symbol);
      setAnalysisData(data);
    };
    loadAnalysis();
  }, [symbol]);

  if (!analysisData) return <div>Loading...</div>;

  const chartData = {
    labels: analysisData.technical_analysis.index,
    datasets: [
      {
        label: 'Close Price',
        data: analysisData.technical_analysis.Close,
        borderColor: 'blue',
        fill: false,
      },
      {
        label: 'SMA 20',
        data: analysisData.technical_analysis.SMA_20,
        borderColor: 'red',
        fill: false,
      },
      {
        label: 'SMA 50',
        data: analysisData.technical_analysis.SMA_50,
        borderColor: 'green',
        fill: false,
      },
    ],
  };

  return (
    <div className="stock-analysis">
      <h1>{symbol} Analysis</h1>
      <div className="chart">
        <Line data={chartData} />
      </div>
      <div className="prediction">
        <h2>Price Prediction</h2>
        <p>30-day forecast: ${analysisData.price_prediction[29].toFixed(2)}</p>
      </div>
    </div>
  );
}

export default StockAnalysis;

