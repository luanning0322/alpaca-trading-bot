# main.py

import time
from moving_average_strategy import MovingAverageStrategy
from trader import AlpacaTrader
from config import SYMBOL, INTERVAL, SLEEP_INTERVAL

if __name__ == "__main__":
    strategy = MovingAverageStrategy(short_window=5, long_window=20)
    trader = AlpacaTrader()

    print("🚀 Real trading bot is starting...")

    while True:
        try:
            print("✅ Loop is running...")
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

            time.sleep(SLEEP_INTERVAL)

        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(60)
