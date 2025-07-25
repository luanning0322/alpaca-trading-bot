import time
from strategy import BreakoutStrategy
from trader import AlpacaTrader
from config import SYMBOL, INTERVAL

if __name__ == "__main__":
    strategy = BreakoutStrategy(symbol=SYMBOL, interval=INTERVAL)
    trader = AlpacaTrader()

    print("🚀 Trading bot is starting...")

    while True:
        try:
            print("🔍 Checking for trading signal...")
            signal = strategy.check_signal()
            print(f"📡 Signal received: {signal}")

            if signal == "buy":
                print("🟢 Executing buy order")
                trader.buy(SYMBOL)
            elif signal == "sell":
                print("🔴 Executing sell order")
                trader.sell(SYMBOL)
            else:
                print("⏳ No valid signal. Waiting...")

        except Exception as e:
            print(f"❌ Error: {e}")

        time.sleep(60) 
