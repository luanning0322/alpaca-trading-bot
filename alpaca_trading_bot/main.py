import time
from strategy import BreakoutStrategy
from trader import AlpacaTrader
from config import SYMBOL, INTERVAL

if __name__ == "__main__":
    strategy = BreakoutStrategy(symbol=SYMBOL, interval=INTERVAL)
    trader = AlpacaTrader()

    print("🚀 自动交易系统启动...")

    while True:
        try:
            signal = strategy.check_signal()
            if signal == "buy":
                trader.buy(SYMBOL)
            elif signal == "sell":
                trader.sell(SYMBOL)
            else:
                print("等待信号中...")
        except Exception as e:
            print(f"❌ 错误: {e}")
        time.sleep(60)
