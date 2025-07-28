ALPACA_API_KEY = "AKRSPYRQKUINR3XBZ3ER"
ALPACA_SECRET_KEY = "j7XT3cVvrvbcq1VSXZVFodiI87sxYNr0lcNvWWCs"
API_BASE = "https://api.alpaca.markets"
TIMEZONE = "America/New_York"

SYMBOL = "AAPL"
INTERVAL = "1Min"        # 用于 API 请求的时间单位
SLEEP_INTERVAL = 60      # 用于 time.sleep 的秒数（单位：秒）

ALPACA_HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
}
