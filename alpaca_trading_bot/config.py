# config.py

# 🗝️ 实盘 API 密钥（请妥善保管）
ALPACA_API_KEY = "AKRSPYRQKUINR3XBZ3ER"
ALPACA_SECRET_KEY = "j7XT3cVvrvbcq1VSXZVFodiI87sxYNr0lcNvWWCs"

# 📡 API 基础地址
DATA_API_BASE = "https://data.alpaca.markets"     # 用于行情（历史数据）
TRADE_API_BASE = "https://api.alpaca.markets"     # 用于下单/交易

# 📈 策略参数
SYMBOL = "NVDA"
INTERVAL = "5Min"        # 用于 API 请求
SLEEP_INTERVAL = 60      # 每轮休眠时间（单位：秒）
TIMEZONE = "America/New_York"

# 🔐 请求头
ALPACA_HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
}
