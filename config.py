from binance.client import Client

API_KEY = "QO9yXYOu0nRfdwXZsXBtJpXv5B6I2JFgdAVGy9x8hjtI4CNCH1PrKskoI5z41OEe"
API_SECRET = "jYT9dLwKD65lEUejmihyMDJJ8C46G4KBoHaUuX14J5HxkVL3Fxd9ACqTvXLOVhU1"

client = Client(API_KEY, API_SECRET)

symbol = 'btcbusd'
quantity = 0.005

tframe = '1m'
testFrame = '1m'

fWsLink = f'wss://fstream3.binance.com/ws/{symbol}@kline_{tframe}'

histOrder = client.futures_get_all_orders(symbol=symbol, limit=1)
for i in histOrder:
    print(f"SIDE: [{i['side']}]")

sList = ['btcusdt',
         'bnbusdt',
         'ethusdt',
         'dogeusdt',
         'btcbusd']

for si in sList:
    print(si.upper())
