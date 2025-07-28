import time
from strategy import MovingAverageStrategy  # 使用你刚刚上传的策略
from trader import AlpacaTrader
from config import SYMBOL, INTERVAL

if __name__ == "__main__":
    strategy = MovingAverageStrategy(short_window=5, long_window=20)
    trader = AlpacaTrader()

    print("🚀 Real trading bot is starting...")

    while True:
        try:
            print("🔍 Checking for trading signal...")
            signal = strategy.check_signal()
            print(f"📈 Signal received: {signal}")

            if signal == "buy":
                print("🟢 Executing real buy order")
                trader.buy(SYMBOL)
            elif signal == "sell":
                print("🔴 Executing real sell order")
                trader.sell(SYMBOL)
            else:
                print("⏸️ No valid signal. Waiting...")

            time.sleep(INTERVAL * 60)  # 每 INTERVAL 分钟运行一次

        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)  # 错误后等待1分钟再尝试
