import ccxt,pandas as pd
import datetime
import time
class download_data:
  def __init__(self,since='2000-01-01 00:00:00',code_name = 'BTC/USDT',frame = '1d',day_range=10,data_amount = 1000):
    self.since = since
    self.code_name = code_name
    self.frame = frame
    self.limit = day_range
    self.data_amount = data_amount
  def to_timestemp(self,dt):
    dt = datetime.datetime.timestamp(dt)
    dt = int(dt) * 1000
    return dt
  def set_df(self,dt):
    binance = ccxt.binance()
    col = ['datetime', 'open', 'high', 'low', 'close', 'volume']
    btc_ohlcv = binance.fetch_ohlcv(self.code_name,limit = self.data_amount,timeframe=self.frame,since=dt)
    df = pd.DataFrame(btc_ohlcv,columns=col)
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    return df
  def get_data(self):
    format = '%Y-%m-%d %H:%M:%S'
    dt = datetime.datetime.strptime(self.since,format)
    dt = self.to_timestemp(dt)
    print(dt)
    df = self.set_df(dt)
    data = df
    for i in range(self.limit):
      dt = self.to_timestemp(df.index[-1])
      df = self.set_df(dt)
      data = pd.concat([data,df])
      time.sleep(0.5)
    data = data.loc[~data.index.duplicated(keep='first')]
    return data
  def Usdt_symbol(self):
    binance = ccxt.binance()
    markets = binance.fetch_tickers()
    temp = list(markets.keys())
    symbol = []
    for i in temp:
      idx = i.find('/')
      if i[idx + 1 :] == 'USDT':
        symbol.append(i)
    return symbol