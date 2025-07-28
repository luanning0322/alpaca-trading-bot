import requests
import pandas as pd
from config import API_BASE, ALPACA_HEADERS, SYMBOL, INTERVAL

class MovingAverageStrategy:
    def __init__(self, short_window=5, long_window=20):
        self.short_window = short_window
        self.long_window = long_window

    def get_price_data(self):
        url = f"{API_BASE}/v2/stocks/{SYMBOL}/bars?timeframe={INTERVAL}&limit={self.long_window}"
        print(f"📡 请求地址: {url}")  # 打印请求URL

        response = requests.get(url, headers=ALPACA_HEADERS)

        # 如果请求失败，打印错误信息并抛出异常
        if response.status_code != 200:
            print(f"❌ 请求失败: {response.status_code}")
            print(f"❗ 返回内容: {response.text}")
            raise Exception("获取K线数据失败")

        data = response.json().get("bars", [])

        if not data:
            print("⚠️ API成功响应，但返回数据为空")
            raise Exception("K线数据为空，无法生成信号")

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
