from datetime import datetime, timedelta
import requests
from config import ALPACA_HEADERS, API_BASE, TIMEZONE
import pytz

class BreakoutStrategy:
    def __init__(self, symbol, interval="1D"):
        self.symbol = symbol
        self.interval = interval

    def get_recent_bars(self, limit=3):
        url = f"{API_BASE}/v2/stocks/{self.symbol}/bars?timeframe={self.interval}&limit={limit}"
        response = requests.get(url, headers=ALPACA_HEADERS)
        response.raise_for_status()
        bars = response.json()["bars"]
        return bars

    def check_signal(self):
        bars = self.get_recent_bars()
        if len(bars) < 3:
            return None

        prev_high = bars[-2]["h"]
        prev_low = bars[-2]["l"]
        curr_close = bars[-1]["c"]

        if curr_close > prev_high:
            return "buy"
        elif curr_close < prev_low:
            return "sell"
        return None
