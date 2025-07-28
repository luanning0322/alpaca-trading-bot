import requests
from config import ALPACA_HEADERS, API_BASE

class AlpacaTrader:
    def submit_order(self, symbol, qty, side):
        url = f"{API_BASE}/v2/orders"
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,
            "type": "market",
            "time_in_force": "day"
        }
        response = requests.post(url, headers=ALPACA_HEADERS, json=data)
        response.raise_for_status()
        print(f"✅ 已提交订单: {side.upper()} {qty} {symbol}")
        return response.json()

    def buy(self, symbol, qty=1):
        return self.submit_order(symbol, qty, "buy")

    def sell(self, symbol, qty=1):
        return self.submit_order(symbol, qty, "sell")
