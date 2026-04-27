# Data

## Primary Data Source: Yahoo Finance (yfinance)

**Description:** Python package containing Open, High, Low, 
Close, and Volume data for U.S. ETFs and the VIX volatility index

**Date range:** 2005-01-01 to 2024-01-01

**License/Terms:** Publicly available market data via Yahoo Finance.
No personal or sensitive information. Used for academic,
non-commercial purposes.

**Ethical considerations:** No PII or sensitive data involved.
No terms of service restrictions apply to academic use.

## Retrieval Instructions

Install the required library:
```bash
pip install yfinance
```

Run the data retrieval script:
```bash
python src/fetch_data.py
```

This will download all required data and save it to `data/raw/market_data.csv`.

Alternatively, retrieve manually in Python:
```python
import yfinance as yf

tickers = ["SPY", "^VIX", "QQQ", "IWM", "GLD", "TLT"]
df = yf.download(tickers, start="2005-01-01", end="2024-01-01")
df.to_csv("data/raw/market_data.csv")
```
## Marketdata.csv

**Tickers:**
| Ticker | Description |
|--------|-------------|
| **SPY** | S&P 500 ETF — tracks the 500 largest US companies |
| **QQQ** | Nasdaq 100 ETF — tracks the 100 largest non-financial Nasdaq companies, heavily tech-weighted |
| **IWM** | Russell 2000 ETF — tracks 2000 small-cap US companies |
| **TLT** | 20+ Year Treasury Bond ETF — tracks long-term US government bonds |
| **GLD** | Gold ETF — tracks the price of gold |
| **^VIX** | CBOE Volatility Index — measures expected market volatility, often called the "fear index" |

**Features and Target:**
| Column | Description |
|--------|-------------|
| **SPY_roll_10** | 10-day rolling standard deviation of SPY close |
| **SPY_roll_20** | 20-day rolling standard deviation of SPY close |
| **SPY_roll_60** | 60-day rolling standard deviation of SPY close |
| **SPY_day_return** | SPY 1-day percentage return |
| **SPY_5_day_return** | SPY 5-day percentage return |
| **SPY_20_day_return** | SPY 20-day percentage return |
| **QQQ_day_return** | QQQ 1-day percentage return |
| **IWM_day_return** | IWM 1-day percentage return |
| **TLT_day_return** | TLT 1-day percentage return |
| **GLD_day_return** | GLD 1-day percentage return |
| **SPY_drawdown** | SPY percentage drawdown from its 252-day rolling high |
| **QQQ_drawdown** | QQQ percentage drawdown from its 252-day rolling high |
| **IWM_drawdown** | IWM percentage drawdown from its 252-day rolling high |
| **SPY_TLT_corr_20** | 20-day rolling correlation between SPY and TLT returns |
| **SPY_TLT_corr_60** | 60-day rolling correlation between SPY and TLT returns |
| **SPY_GLD_corr_20** | 20-day rolling correlation between SPY and GLD returns |
| **SPY_vol_ratio** | SPY daily volume relative to its 20-day average volume |
| **QQQ_vol_ratio** | QQQ daily volume relative to its 20-day average volume |
| **IWM_vol_ratio** | IWM daily volume relative to its 20-day average volume |
| **spy_above_avg** | Binary indicator (1/0) for whether SPY is trading above its 200-day moving average |
| **market_crisis** | Target variable — indicates whether a market crisis (VIX > 30) occurs within the next 20 trading days |

