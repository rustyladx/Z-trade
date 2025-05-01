import pandas as pd
import ta

def analyze_coin(exchange, symbol):
    ohlcv = exchange.fetch_ohlcv(symbol, '15m', limit=100)
    df = pd.DataFrame(ohlcv, columns=["time", "open", "high", "low", "close", "volume"])

    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    df["macd"] = ta.trend.MACD(df["close"]).macd_diff()
    bb = ta.volatility.BollingerBands(df["close"])
    df["bb_high"] = bb.bollinger_hband()
    df["bb_low"] = bb.bollinger_lband()

    last = df.iloc[-1]
    score = 0
    strategy = []

    if last["rsi"] < 30:
        score += 1
        strategy.append("RSI oversold")

    if last["macd"] > 0:
        score += 1
        strategy.append("MACD bullish")

    if last["close"] < last["bb_low"]:
        score += 1
        strategy.append("Bollinger bounce")

    if score == 0:
        return None

    entry = last["close"]
    tp = entry * 1.02
    sl = entry * 0.98

    return {
        "symbol": symbol,
        "entry": entry,
        "exit": tp,
        "tp": tp,
        "sl": sl,
        "score": score,
        "strategy": ", ".join(strategy),
    }
