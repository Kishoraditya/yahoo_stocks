import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const fetchUserStocks = async () => {
  const response = await axios.get(`${API_URL}/users/stocks`);
  return response.data;
};

export const fetchStockAnalysis = async (symbol) => {
  const response = await axios.get(`${API_URL}/stocks/${symbol}/analysis`);
  return response.data;
};

