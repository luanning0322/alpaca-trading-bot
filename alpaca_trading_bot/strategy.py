import requests
import pandas as pd
from config import API_BASE, ALPACA_HEADERS, SYMBOL, INTERVAL

class MovingAverageStrategy:
    def __init__(self, short_window=5, long_window=20):
        self.short_window = short_window
        self.long_window = long_window

    def get_price_data(self):
        url = f"{API_BASE}/v2/stocks/{SYMBOL}/bars?timeframe={INTERVAL}&limit={self.long_window}"
        response = requests.get(url, headers=ALPACA_HEADERS)
        data = response.json()["bars"]
        df = pd.DataFrame(data)
        df["close"] = df["c"]
        return df

    def check_signal(self):
        df = self.get_price_data()
        df["short_ma"] = df["close"].rolling(window=self.short_window).mean()
        df["long_ma"] = df["close"].rolling(window=self.long_window).mean()

        if df["short_ma"].iloc[-2] < df["long_ma"].iloc[-2] and df["short_ma"].iloc[-1] > df["long_ma"].iloc[-1]:
            return "buy"
        elif df["short_ma"].iloc[-2] > df["long_ma"].iloc[-2] and df["short_ma"].iloc[-1] < df["long_ma"].iloc[-1]:
            return "sell"
        else:
            return "hold"
