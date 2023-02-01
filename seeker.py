import websocket
import config as cfg
import json
import talib
import datetime
import re
import pandas as pd
from binance.client import Client
from binance.enums import *
import pprint  # TODO: APAGAR DPS DE FORMATADO
from binance.exceptions import BinanceAPIException, BinanceOrderException
#==============================================================================#

if cfg.tframe[-1] == 'm':
    tf1 = int(re.findall('\d+', cfg.tframe)[0])
    tme_frame = 1 * tf1
if cfg.tframe[-1] == 'h':
    tf1 = int(re.findall('\d+', cfg.tframe)[0])
    tme_frame = 60 * tf1

F_SOCKET = cfg.fWsLink

client = Client(cfg.API_KEY, cfg.API_SECRET)

TRADE_SYMBOL = cfg.symbol.upper()
TRADE_QUANTITY = 0.005  # TODO: Passar para config.py

in_position = False

symbols = client.futures_position_information()
df = pd.DataFrame(symbols)
symbol_Loc = df.index[df.symbol == TRADE_SYMBOL]
SYMBOL_POS = (symbol_Loc[-1])

# TODO: Passar abaixo para config.py
f_Hist_Orders = client.futures_get_all_orders(symbol=TRADE_SYMBOL, limit=1)
for i in f_Hist_Orders:
    print(f"SIDE: [{i['side']}]")

    lastOrder = i['side']
# TODO: Passar acima para config.py
lastOrder = i['side']
#==============================================================================#
# TODO: Enviar para config.py
levarege = 50

RSI_PERIOD = 14
RSI_OB = 75
RSI_OS = 25

MFI_OB = 80
MFI_OS = 20

#==============================================================================#
data = client.futures_exchange_info()

symbol_list = []
precision = []
stop_Data = 0

for pair in data['symbols']:
    if pair['status'] == 'TRADING':
        symbol_list.append(pair['symbol'])
        precision.append(pair['pricePrecision'])

df2 = pd.DataFrame(symbol_list)
df1 = pd.DataFrame(precision)
merge = pd.concat([df1, df2], axis=1)
merge.columns = ['precision', 'symbol']
merge.set_index('precision', inplace=True)
symbol_Loc = merge.index[merge.symbol == TRADE_SYMBOL]
round_off = symbol_Loc[-1]

#==============================================================================#
# Get Historical Data

csticks = client.futures_klines(symbol=TRADE_SYMBOL, interval=cfg.tframe)
df = pd.DataFrame(csticks)
df_edited = df.drop([0, 6, 7, 8, 9, 10, 11], axis=1)
df_final = df_edited.drop(df_edited.tail(1).index)
df_final.columns = ['o', 'h', 'l', 'c', 'v']
df_final['RSI'] = round(talib.RSI(df_final['c'], 14), round_off)
df_final['MFI'] = round(talib.MFI(
    df_final['h'], df_final['l'], df_final['c'], df_final['v'], 14), round_off)

#==============================================================================#


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        order = client.futures_create_order(
            symbol=symbol, type=order_type, side=side, quantity=quantity)

        now = datetime.datetime.now()
        print('Current time is: {}'.format(now.strftime("%d/%m/%Y %H:%M:%S")))
        #print(f"Order: [{order}]")
        print(
            f"Moeda: {order['symbol']}\nSide: {order['side']}\nType: {order['type']}\nQtd CrtiptoMoeda: {order['origQty']};")

    except Exception as error:
        print(error)


def stop_Order(symbol, side, oType, quantity, reduceOnly='true'):
    try:
        print("#"*74)
        print(f"\nstop_Order Function:")
        print(f"Side: [{side}]")

        stop_Order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=oType,
            quantity=quantity,
            reduceOnly=reduceOnly)

        if side == SIDE_SELL:
            print(f"StopWin:\n{stop_Order}")
            print("#"*74)

        elif side == SIDE_BUY:
            print(f"StopLoss:\n {stop_Order}")
            print("#"*74)

    except Exception as error:
        if side == SIDE_SELL:
            print(f"StopWin Error: {error}")
        elif side == SIDE_BUY:
            print(f"StopLoss Error: {error}")


def on_open(ws):
    print('='*74)
    print('Recebendo Dados...')
    print(f"Tempo de Mercado: [{cfg.tframe}]")
    print('='*74)


def on_close(ws):
    print('='*74)
    print('Conexão Fechada')
    print('='*74)


def on_message(ws, message):
    global df_final, in_position, StopData

    json_message = json.loads(message)
    candle = json_message['k']
    candle_closed = candle['x']
    open_data = candle['o']
    high_data = candle['h']
    low_data = candle['l']
    close_data = candle['c']

    if candle_closed:
        df_final = df_final.append(candle, ignore_index=True)
        df_final['RSI'] = round(talib.RSI(df_final['c'], 14), round_off)
        df_final['MFI'] = round(talib.MFI(
            df_final['h'], df_final['l'], df_final['c'], df_final['v'], 14), round_off)

        last_RSI = float(df_final['RSI'].tail(1))
        last_MFI = float(df_final['MFI'].tail(1))

        fut_Acc = client.futures_account()
        acc_Pos = fut_Acc['positions']
        acc_Pos_df = pd.DataFrame(acc_Pos)
        acc_Edited_Df = acc_Pos_df[['symbol', 'initialMargin', 'entryPrice',
                                    'unrealizedProfit', 'positionSide']]

        calc = acc_Edited_Df.loc[acc_Edited_Df['symbol'] == TRADE_SYMBOL]

        profit = calc['unrealizedProfit']
        initMargin = calc['initialMargin']
        cv_initMargin = initMargin.iloc[0]
        cv_profit = profit.iloc[0]

        print('='*74)
        now = datetime.datetime.now()
        print('Current time is: {}'.format(now.strftime("%d/%m/%Y %H:%M:%S")))
        print('='*74)
        print(f"Open: {open_data}   |   High: {high_data}",
              f"  |   Low: {low_data}  |  Close: {close_data}")
        # TODO: Formatar para padrão
        print(f"RSI: {last_RSI}      | MFI: {last_MFI} ")

        if float(cv_initMargin) == 0:
            print("Nenhuma 'position' em andamento. Aguardando...")
            print(f"Position: {in_position}")
            in_position = False

        else:

            in_position = True
            percent_profit = (float(cv_profit) / float(cv_initMargin)) * 100
            fee = (float(cv_initMargin)*levarege) * 0.0003
            #r_Profit = round(float(cv_profit, 3) - fee)

            print('='*74)
            print(f'Margin: {round(float(cv_initMargin),3)}')
            print(f"Profit: {round(float(cv_profit),3)}")
            #print(f"Real Profit: {r_Profit}")
            print(f"PNL(ROE%): {round(percent_profit, 2)}%")
            print(f"Fee: {fee}")
            print('='*74)
            print(f'Position: {in_position}')

#==============================================================================#


#==============================================================================#
ws = websocket.WebSocketApp(F_SOCKET, on_open=on_open,
                            on_close=on_close, on_message=on_message)
ws.run_forever()
