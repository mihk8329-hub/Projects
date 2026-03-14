import yfinance as yf
import requests
from ta.momentum import RSIIndicator
from ta.trend import MACD


def get_top_gainers():
    url = "https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved?scrIds=day_gainers"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (404, 500, etc.)

        data = response.json()  # Can still fail if response is not JSON

        quotes = data.get("finance", {}).get("result", [{}])[0].get("quotes", [])
        if not quotes:
            return []

        symbols = [q["symbol"] for q in quotes[:10]]
        return symbols

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return []
    except ValueError as e:
        print("Invalid JSONs:", e)
        return []


def analyze_stock(symbol):

    data = yf.download(symbol, period="5d", interval="15m")

    close = data["Close"].squeeze()

    rsi = RSIIndicator(close).rsi().iloc[-1]

    macd = MACD(close).macd().iloc[-1]

    price = float(close.iloc[-1])

    return price, rsi, macd