import time

# 模拟策略类（始终返回“buy”）
class MockStrategy:
    def check_signal(self):
        return "buy"

# 模拟交易执行器（打印日志代替真实下单）
class MockTrader:
    def buy(self, symbol):
        print(f"✅ [Mock BUY] Executed buy order for {symbol}")

    def sell(self, symbol):
        print(f"✅ [Mock SELL] Executed sell order for {symbol}")

# 设定符号与时间间隔
SYMBOL = "AAPL"
INTERVAL = 1  # 单位分钟，测试用可忽略

if __name__ == "__main__":
    strategy = MockStrategy()
    trader = MockTrader()

    print("🚀 Mock trading bot is starting...")

    while True:
        try:
            print("🔍 Checking for trading signal...")
            signal = strategy.check_signal()
            print(f"📡 Signal received: {signal}")

            if signal == "buy":
                print("🟢 Executing mock buy order")
                trader.buy(SYMBOL)
            elif signal == "sell":
                print("🔴 Executing mock sell order")
                trader.sell(SYMBOL)
            else:
                print("⏳ No valid signal. Waiting...")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        time.sleep(60)  # 每 60 秒循环一次
