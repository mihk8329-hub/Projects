import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import MACD


# Fetch market data
def get_market_data(symbol):

    data = yf.download(
        symbol,
        period="5d",
        interval="15m"
    )

    return data


# Calculate indicators
def calculate_indicators(data):

    # Convert Close column to 1-D series
    close_prices = data['Close'].squeeze()

    rsi = RSIIndicator(close_prices).rsi()
    macd = MACD(close_prices).macd()

    return {
        "rsi": rsi.iloc[-1],
        "macd": macd.iloc[-1]
    }


# Generate signal
def generate_signal(indicators):

    if indicators["rsi"] < 30:
        return "BUY"

    if indicators["rsi"] > 70:
        return "SELL"

    return "HOLD"


# Risk management
def risk_management(entry):

    stoploss = entry * 0.98
    target = entry * 1.04

    return stoploss, target