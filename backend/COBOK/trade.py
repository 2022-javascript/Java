import ccxt 
import pprint
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
binance = ccxt.binance(config={
    'apiKey': api_key, 
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

def set_ma(data,size,column):
  ma = data[column].rolling(window=size).mean()
  return ma

def set_bolingerband(data):
  ma20 = data['close'].rolling(window = 20).mean()
  stddv = data['close'].rolling(window = 20).std()
  upper = ma20 + 3*stddv
  lower = ma20 - 3*stddv
  return upper,lower

def entryprice():
  balance = binance.fetch_balance()
  positions = balance['info']['positions']

  for position in positions:
      if position["symbol"] == "BTCUSDT":
        return float(position['entryPrice'])

def now_price():
  btc_ohlcv = binance.fetch_ohlcv("BTC/USDT",limit = 500,timeframe='1d')
  df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
  df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
  df.set_index('datetime', inplace=True)
  return df['close'][-1]

def download_data(frame):
  binance = ccxt.binance()
  btc_ohlcv = binance.fetch_ohlcv("BTC/USDT",limit = 500,timeframe=frame)
  df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
  df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
  df.set_index('datetime', inplace=True)
  return df

def position_check():
  balance = binance.fetch_balance()
  positions = balance['info']['positions']
  ck = 0
  for position in positions:
      if position["symbol"] == "BTCUSDT" and position['positionAmt'] != '0.000':
          ck = 1
  return ck

def auto_trade(api_key,secret):
    binance = ccxt.binance(config={
    'apiKey': api_key, 
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
        }
    })
    print(binance)
def trade():
  amount = 0
  position = position_check()
  price = 0
  while(True):
    data = download_data('30m')
    upper,lower = set_bolingerband(data)

    # 볼린저 밴드 하단 돌파시 매수
    if data['close'][-1] <= lower[-1] and data['close'][-2] > lower[-2]:
      order = binance.create_market_buy_order(
      symbol="BTC/USDT",
      amount=0.01)

      current_time = datetime.now()
      price = entryprice()
      print('매수시점:',current_time,'진입가격:',price)

      position = position_check()

    # 볼린저 밴드 상단 돌파시 매도
    elif data['close'][-1]>=upper[-1] and data['close'][-2] < upper[-2] and position == 1:
      order = binance.create_market_sell_order(
      symbol="BTC/USDT",
      amount=0.01)

      current_time = datetime.datetime.now()
      price = entryprice()
      print('매도시점:',current_time,'매도가격:',price)

      position = position_check()
    
    # -5% 손실 시 매도
    elif price*0.95 >= now_price():
      order = binance.create_market_sell_order(
      symbol="BTC/USDT",
      amount=0.01)
      
      current_time = datetime.datetime.now()
      price = entryprice()
      print('매도시점:',current_time,'매도가격:',price)

      position = position_check()
    time.sleep(0.5)
trade()