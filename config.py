from binance.client import Client
import pandas as pd
API_KEY = ""
API_SECRET = ""

client = Client(API_KEY, API_SECRET)

'''sList = ['btcusdt',
         'bnbusdt',
         'ethusdt',
         'dogeusdt',
         'btcbusd']'''

symbol = 'btcbusd'

quantity = 0.005

tframe = '1m'


fWsLink = f'wss://fstream3.binance.com/ws/{symbol}@kline_{tframe}' #TODO: Enviar para Hklines.py

histOrder = client.futures_get_all_orders(symbol=symbol, limit=1)
'''for i in histOrder:
    print(f"Last SIDE: [{i['side']}]")

for si in sList:
    print(si.upper())'''
