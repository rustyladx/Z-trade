import ccxt
from ta_utils import analyze_coin

def scan_market():
    exchange = ccxt.binance()
    markets = exchange.load_markets()
    symbols = [s for s in markets if s.endswith("/USDT")]

    signals = []
    for symbol in symbols:
        try:
            signal = analyze_coin(exchange, symbol)
            if signal:
                signals.append(signal)
        except Exception:
            continue

    signals = sorted(signals, key=lambda x: x["score"], reverse=True)
    return signals[:5]  # return top 5
