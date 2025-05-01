from backend import scanner

def generate_trade_signal():
    top_coins = scan_market()
    if not top_coins:
        return {"status": "No signal"}

    signal = top_coins[0]  # best scoring coin
    return {
        "coin": signal["symbol"],
        "strategy": signal["strategy"],
        "entry": round(signal["entry"], 5),
        "exit": round(signal["exit"], 5),
        "tp": round(signal["tp"], 5),
        "sl": round(signal["sl"], 5),
    }
