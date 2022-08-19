import pandas_ta as pta, pandas as pd, numpy as np
from dataread import download_data
def add_rsi(entire_df,data_name = 'close',period = 14):
    rsi = pta.rsi(entire_df[data_name], length=period)
    entire_df['rsi'+'_'+str(period)] = rsi
    return entire_df
def add_ma(entire_df, data_name = 'close',period = 20):
    entire_df['mean'+'_'+str(period)] = entire_df[data_name].rolling(window=period).mean()
    return entire_df
def add_ema(df, period: int = 30):
    array = df['close']
    ema = pta.ma("ema", pd.Series(array.astype(float)), length=int(period))
    df['ema'+'_'+str(period)] = ema
    return df
def add_stochastic(df,n = 14,m = 5,t = 5):
    ndays_high = df.high.rolling(window = n,min_periods = 1).max()
    ndays_low = df.low.rolling(window = n,min_periods = 1).min()
    fast_k = ((df.close - ndays_low) / (ndays_high - ndays_low)) * 100
    slow_k = fast_k.ewm(span=t).mean()
    slow_d = slow_k.ewm(span=t).mean()

    df = df.assign(fast_k = fast_k, fast_d = slow_k, slow_k = slow_k, slow_d = slow_d)
    return df
def add_macd(
    df: np.ndarray,
    fast_period: int = 12,
    slow_period: int = 26,
):

    temp = pta.macd(
        pd.Series(np.array(df['close']).astype(float)),
        fast=int(fast_period),
        slow=int(slow_period),
        signal=9,
    )
    macd = temp[temp.columns[0]]
    df['macd'+'_'+str(fast_period)+'_'+str(slow_period)] = macd
    return df
def add_disparity(df,period = 20):
    # 종가기준으로 이동평균선 값을 구함
    ma = df["close"].rolling(period).mean()

    # 시가가 이평선 기준으로 얼마나 위에 있는지 구함
    df['disparity'] = 100*(df["open"]/ma)
    return df
# df = download_data(since = '2020-01-01 00:00:00').get_data()
# entire_df = add_disparity(df)
# print(entire_df)