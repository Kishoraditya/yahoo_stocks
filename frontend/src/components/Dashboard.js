import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchUserStocks } from '../services/api';

function Dashboard() {
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    const loadStocks = async () => {
      const userStocks = await fetchUserStocks();
      setStocks(userStocks);
    };
    loadStocks();
  }, []);

  return (
    <div className="dashboard">
      <h1>Your Stock Dashboard</h1>
      <ul>
        {stocks.map(stock => (
          <li key={stock.symbol}>
            <Link to={`/stock/${stock.symbol}`}>
              {stock.symbol} - {stock.company_name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;

