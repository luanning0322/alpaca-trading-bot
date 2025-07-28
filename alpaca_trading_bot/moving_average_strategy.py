import requests
import pandas as pd
from config import API_BASE, ALPACA_HEADERS, SYMBOL, INTERVAL

class MovingAverageStrategy:
    def __init__(self, short_window=5, long_window=20):
        self.short_window = short_window
        self.long_window = long_window

    def get_price_data(self):
        try:
            url = f"{API_BASE}/v2/stocks/{SYMBOL}/bars?timeframe={INTERVAL}&limit={self.long_window + 2}"
            response = requests.get(url, headers=ALPACA_HEADERS)
            response.raise_for_status()  # 如果返回不是200，将引发异常
            data = response.json()["bars"]

            if len(data) < self.long_window:
                raise ValueError("返回的数据不足以计算长周期均线")

            df = pd.DataFrame(data)
            df["close"] = df["c"]
            return df
        except Exception as e:
            print(f"⚠️ 获取价格数据失败: {e}")
            return None

    def check_signal(self):
        df = self.get_price_data()
        if df is None or len(df) < self.long_window + 1:
            return "hold"

        df["short_ma"] = df["close"].rolling(window=self.short_window).mean()
        df["long_ma"] = df["close"].rolling(window=self.long_window).mean()

        # 输出调试信息，观察最近3根均线数值
        print(df[["close", "short_ma", "long_ma"]].tail(3))

        # 改进后的金叉/死叉判断（方案一）
        short_ma_prev = df["short_ma"].iloc[-2]
        long_ma_prev = df["long_ma"].iloc[-2]
        short_ma_now = df["short_ma"].iloc[-1]
        long_ma_now = df["long_ma"].iloc[-1]

        if short_ma_now > long_ma_now and short_ma_prev <= long_ma_prev:
            return "buy"
        elif short_ma_now < long_ma_now and short_ma_prev >= long_ma_prev:
            return "sell"
        else:
            return "hold"
