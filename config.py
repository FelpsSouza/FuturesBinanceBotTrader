from binance.client import Client

API_KEY = ""
API_SECRET = ""

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
