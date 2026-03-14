from tools import get_top_gainers, analyze_stock


class TradingAgent:


    def analyze_top_stocks(self):

        symbols = get_top_gainers()

        result = "Top 10 Stocks Today\n\n"

        for s in symbols:

            price, rsi, macd = analyze_stock(s)

            if rsi > 70:
                trade_type = "Intraday Sell"
                target = price * 0.98
                stoploss = price * 1.02

            elif rsi < 30:
                trade_type = "Intraday Buy"
                target = price * 1.03
                stoploss = price * 0.97

            elif macd > 0:
                trade_type = "Short Term"
                target = price * 1.05
                stoploss = price * 0.95

            else:
                trade_type = "Long Term Investment"
                target = None
                stoploss = None


            result += f"{s}\n"
            result += f"Type: {trade_type}\n"
            result += f"Price: {price:.2f}\n"

            if target:
                result += f"Target: {target:.2f}\n"
                result += f"Stoploss: {stoploss:.2f}\n"

            result += f"RSI: {rsi:.2f}\n\n"


        return result