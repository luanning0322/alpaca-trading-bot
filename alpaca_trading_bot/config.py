# config.py

ALPACA_API_KEY = "AKRSPYRQKUINR3XBZ3ER"
ALPACA_SECRET_KEY = "j7XT3cVvrvbcq1VSXZVFodiI87sxYNr0lcNvWWCs"
API_BASE = "https://data.alpaca.markets"
TIMEZONE = "America/New_York"

SYMBOL = "NVDA"
INTERVAL = "1Min"        # 用于 API 请求
SLEEP_INTERVAL = 60      # 用于轮询等待（单位：秒）

ALPACA_HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
}
