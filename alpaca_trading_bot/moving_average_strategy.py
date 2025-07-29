import requests
import pandas as pd
from config import DATA_API_BASE, ALPACA_HEADERS, SYMBOL, INTERVAL

class MovingAverageStrategy:
    def __init__(self, short_window=5, long_window=20):
        self.short_window = short_window
        self.long_window = long_window

    def get_price_data(self):
        url = f"{DATA_API_BASE}/v2/stocks/{SYMBOL}/bars?timeframe={INTERVAL}&limit={self.long_window}"
        print(f"📡 请求地址: {url}")  # 打印请求URL

        try:
            response = requests.get(url, headers=ALPACA_HEADERS, timeout=10)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print("⏱ 请求超时，请检查网络或API状态")
            raise
        except requests.exceptions.RequestException as e:
            print(f"❌ 请求异常: {e}")
            raise

        try:
            data = response.json().get("bars", [])
        except ValueError:
            print("❗ 无法解析JSON响应")
            raise

        if not data:
            print("⚠️ API响应成功但没有K线数据")
            raise Exception("K线数据为空，无法生成信号")

        df = pd.DataFrame(data)
        if "c" not in df.columns:
            print("❌ 数据中缺少收盘价字段 'c'")
            raise Exception("无效的K线结构")

        df["close"] = df["c"]
        return df

    def check_signal(self):
        print("🔁 正在检查交易信号...")  # 心跳日志
        try:
            df = self.get_price_data()
            df["short_ma"] = df["close"].rolling(window=self.short_window).mean()
            df["long_ma"] = df["close"].rolling(window=self.long_window).mean()

            # 改进策略：当短期均线刚刚上穿/下穿长期均线或当前偏离超过一定比例则发出交易信号
            if df["short_ma"].iloc[-2] < df["long_ma"].iloc[-2] and df["short_ma"].iloc[-1] > df["long_ma"].iloc[-1]:
                print("📈 收到信号：买入（BUY）")
                return "buy"
            elif df["short_ma"].iloc[-2] > df["long_ma"].iloc[-2] and df["short_ma"].iloc[-1] < df["long_ma"].iloc[-1]:
                print("📉 收到信号：卖出（SELL）")
                return "sell"
            else:
                # 增加强信号判定：当前偏离阈值（例如0.5%）
                latest_short = df["short_ma"].iloc[-1]
                latest_long = df["long_ma"].iloc[-1]
                if (latest_short - latest_long) / latest_long > 0.005:
                    print("📈 偏离增强信号：强买入（BUY）")
                    return "buy"
                elif (latest_long - latest_short) / latest_long > 0.005:
                    print("📉 偏离增强信号：强卖出（SELL）")
                    return "sell"
                print("⏸ 收到信号：保持（HOLD）")
                return "hold"

        except Exception as e:
            print(f"🚨 策略执行异常：{e}")
            return "hold"
