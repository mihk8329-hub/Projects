from tools import get_market_data, calculate_indicators, generate_signal, risk_management

class TradingAgent:

    def analyze(self, symbol):

        data = get_market_data(symbol)

        indicators = calculate_indicators(data)

        signal = generate_signal(indicators)

        entry = float(data['Close'].iloc[-1].iloc[0])

        stoploss, target = risk_management(entry)

        return f"""
Market: {symbol}

Signal: {signal}

Entry: {entry:.2f}
Stoploss: {stoploss:.2f}
Target: {target:.2f}

RSI: {indicators['rsi']:.2f}
MACD: {indicators['macd']:.2f}
"""