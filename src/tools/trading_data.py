from langchain_core.tools import tool
import pandas as pd
from vnstock import Quote
from src.schema.trading import History

@tool(args_schema=History)
def get_price_history(symbol: str, start_date: str, end_date: str, interval: str, window_size: int) -> pd.DataFrame:
    """Lấy dữ liệu giá lịch sử của mã chứng khoán từ nguồn VCI."""
    quote = Quote(symbol=symbol, source='VCI')
    df = quote.history(start=start_date, end=end_date, interval=interval)
    return df

@tool(args_schema=History)
def caculate_sma(symbol: str, start_date: str, end_date: str, interval: str,window_size: int) -> pd.DataFrame:
    """Tính Simple Moving Average (SMA)"""
    df = get_price_history.func(symbol, start_date, end_date, interval, window_size)
    df = df[(df["time"] >= start_date) & (df["time"] <= end_date)]
    df[f"SMA{window_size}"] = df["close"].rolling(window=window_size).mean()
    
    return df

@tool(args_schema=History)
def calculate_smi(symbol: str, start_date: str, end_date: str, interval: str,window_size: int) -> pd.DataFrame:
    """Tính Relative Strength Index (RSI)"""
    df = get_price_history.func(symbol, start_date, end_date, interval, window_size)
    df = df[(df["time"] >= start_date) & (df["time"] <= end_date)]
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    avg_gain = gain.rolling(window=window_size).mean()
    avg_loss = loss.rolling(window=window_size).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    df[f"RSI{window_size}"] = rsi

    return df