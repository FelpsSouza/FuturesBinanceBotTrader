import websockets
import config as cfg
import json
import talib
import numpy as np
import pandas as pd
from time import sleep
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import csv
from array import array
from numpy import genfromtxt
import pprint
import asyncio

F_SOCKET = cfg.fWsLink

client = Client(cfg.API_KEY, cfg.API_SECRET)

TRADE_SYMBOL = 'BTCBUSD'
SYMBOL_POS = 41
TRADE_QUANTITY = 0.001  # sample quantity

RSI_PERIOD = 14
RSI_OB = 80
RSI_OS = 20

# client.futures_change_leverage(symbol=TRADE_SYMBOL, levarage=1)


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET, timeInForce=TIME_IN_FORCE_GTC):
    try:
        testOrder = client.create_test_order(symbol=symbol, type=order_type,
                                             side=side, quantity=quantity)

        reOrder = client.futures_create_order(
            symbol=symbol, type=order_type, side=side, quantity=quantity)

        print(f"Test Order: {testOrder}")
        print(f"Tipo TOrder: {type(testOrder)}")
        print(
            f"Moeda: {reOrder['symbol']}\nSide: {reOrder['side']}\nType: {reOrder['type']}\nQtd CrtiptoMoeda: {reOrder['origQty']};")
        print(f"Real Order (Sem formatação):\n{reOrder}")

    except Exception as error:
        print(error)


# tOrder_suceed = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)

# rOrder_suceed = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)


opBuyOrder = client.futures_account_trades(symbol=TRADE_SYMBOL, limit=1)

acount = client.futures_account()
ass = acount['positions']
df = pd.DataFrame(ass)
main = df[['symbol', 'initialMargin', 'entryPrice',
           'unrealizedProfit', 'positionSide', 'openOrderInitialMargin']]
btcbusd = main.loc[main['symbol'] == TRADE_SYMBOL]


profit = btcbusd['unrealizedProfit']
initMargin = btcbusd['initialMargin']
cv_initMargin = initMargin.iloc[0]
cv_profit = profit.iloc[0]

print(df.loc[df['symbol'] == TRADE_SYMBOL])
# print(btcbusd)

if(float(cv_initMargin) == 0):
    print("Nenhuma ordem em andamento. Nada a fazer.")
else:
    percent_profit = (float(cv_profit) / float(cv_initMargin)) * 100
    fee = float(cv_initMargin) * 0.027
    print("================")
    print(f'profit: {round(float(cv_profit),3)}')
    print(f"PNL(ROE%): {round(percent_profit, 2)}")
    print(f"Fee: {fee}\n")

'''for i in ass:
    print(i)'''
'''a = client.futures_recent_trades(symbol=TRADE_SYMBOL)
h = client.futures_get_all_orders(symbol=TRADE_SYMBOL, limit=1)
for i in h:
    print(f"Symbol: {i['symbol']}")
    print(f"Type: {i['type']}")
    print(f"Side: {i['side']}")'''

'''client.futures_create_order(
    symbol=TRADE_SYMBOL,
    side=SIDE_SELL,
    type='MARKET',
    quantity=TRADE_QUANTITY,
    reduceOnly='true'
)'''

# print(buyOrder)
