#Library Imports
import pandas as pd
import yfinance as yf



#Raw Data
tickers = ["SPY", "^VIX", "QQQ", "IWM", "GLD", "TLT"]
df = yf.download(tickers, start="2005-01-01", end="2024-01-01", interval="1d")

#Creating Features
close = df['Close']
vol = df['Volume']
feature_df = pd.DataFrame(index=close.index)

## Rolling means
feature_df['SPY_roll_10'] = close['SPY'].rolling(window=10, min_periods=1).std()
feature_df['SPY_roll_20'] = close['SPY'].rolling(window=20, min_periods=1).std()
feature_df['SPY_roll_60'] = close['SPY'].rolling(window=60, min_periods=1).std()

## Returns
feature_df['SPY_day_return'] = close['SPY'].pct_change(1)
feature_df['SPY_5_day_return'] = close['SPY'].pct_change(5)
feature_df['SPY_20_day_return'] = close['SPY'].pct_change(20)
feature_df['QQQ_day_return'] = close['QQQ'].pct_change(1)
feature_df['IWM_day_return'] = close['IWM'].pct_change(1)
feature_df['TLT_day_return'] = close['TLT'].pct_change(1)
feature_df['GLD_day_return'] = close['GLD'].pct_change(1)


## Drawdowns
SPY_rolling_max = close["SPY"].rolling(window=252, min_periods=1).max()
feature_df['SPY_drawdown'] = (close["SPY"] - SPY_rolling_max) / SPY_rolling_max * 100  
QQQ_rolling_max = close["QQQ"].rolling(window=252, min_periods=1).max()
feature_df['QQQ_drawdown'] = (close["QQQ"] - QQQ_rolling_max) / QQQ_rolling_max * 100  
IWM_rolling_max = close["IWM"].rolling(window=252, min_periods=1).max()
feature_df['IWM_drawdown'] = (close["IWM"] - IWM_rolling_max) / IWM_rolling_max * 100  

## Correlations
spy_return = close['SPY'].pct_change()
tlt_return = close['TLT'].pct_change()
gld_return = close['GLD'].pct_change()


feature_df['SPY_TLT_corr_20'] = spy_return.rolling(window=20).corr(tlt_return)
feature_df['SPY_TLT_corr_60'] = spy_return.rolling(window=60).corr(tlt_return)
feature_df['SPY_GLD_corr_20'] = spy_return.rolling(window=20).corr(gld_return)

## Volume
feature_df['SPY_vol_ratio'] = vol['SPY'] / vol['SPY'].rolling(window=20).mean()
feature_df['QQQ_vol_ratio'] = vol['QQQ'] / vol['QQQ'].rolling(window=20).mean()
feature_df['IWM_vol_ratio'] = vol['IWM'] / vol['IWM'].rolling(window=20).mean()


## Trends
spy_moving_avg = close['SPY'].rolling(window=200).mean()
feature_df['spy_above_avg'] =  (close['SPY'] > spy_moving_avg).astype(int)

## Target 
target = (close['^VIX'] > 30).shift(-20)
feature_df['market_crisis'] = target

feature_df = feature_df.dropna()                
feature_df['market_crisis'] = feature_df['market_crisis'].astype(int)

feature_df.to_csv("data/marketdata.csv")


 