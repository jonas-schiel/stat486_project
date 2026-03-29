# Data and EDA Checkpoint

## Data Overview

### Research Question:

Can machine learning classifcation methods use market data to accurately detect and identify market behavior. Ultimately labeling the market to be either behaving normally (classified as 0), or in crisis (classified as 1).

### Dataset:

**Description:** The data that will be used to complete this project comes from a python library, titled 'yfinance'. The data is provided by Yahoo, publicly available, free to use, and contains a wide variety of financial data. For my project, I will only require data associated with tickers. 

**Citation:** Data sourced from Yahoo Finance via the yfinance Python library (Aroussi, 2024). All data retrieved covers the period January 2004 – December 2024 at daily frequency.

**Ethical Considerations:** The data obtained is publicly avaible and faces no ethical concerns, so long as it is used for educational and research purposes only. My project will soley be used for educational and research purposes.

## Data Description and Variables

**General Description:** The ticker data is made up of rows that contain the following columns: Open, High, Low, Close, Volume. Each row represents a trading day. Open is the stock price at the start of the day, high is the peak price for that day, low is the lowest price for that day, close is the price at the end of the day, and volume is the total amount traded that day. For my project I will be using the following tickers: SPY, ^VIX, QQQ, IWM, GLD, and TLT. These represent major ETFs, raw materials, bonds, and indexes that are often used to gauge market behavior.

**Target and Feature Variables:** The target variable for my project is a label for the market. Either the market is in crises (label = 1), or the market is not in crisis (label = 0). Feature variables have not been entirely determined yet, but might include: daily return for SPY (percentage change of Close), standard devation of daily returns over a 60-day window, VIX close, VIX spike indicator (if VIX increases by a given amount in a day-over-day period), SPY vs TLT return spread (side to side comparison of stock and bond performance), SPY vs GLD (side to side performance of stock and gold prices), rolling correlations between SPY and TLT (stocks and bonds), SPY and GLD (stocks and gold), SPY and VIX (Stocks and Volatility Index).

**Preprocessing Steps:** One of the most challenging aspects of this project will be the preprocessing of the data. The most important aspect of my project is correctly labeling the target variable. Crisis days will be defined using well documented time periods where various aspects of the market experienced abnormal behavior. Raw columns of the yfinance dataset will need to be converted into feature variables.

## Summary Statistics

The table below presents descriptive statistics for the three primary variables used in this analysis: SPY closing price, VIX level, and SPY daily return, computed over 4,781 trading days from 2005 to 2024.

| Statistic | SPY Price | VIX | SPY Daily Return |
|-----------|-----------|-----|-----------------|
| Count | 4,781 | 4,781 | 4,780 |
| Mean | 188.53 | 19.34 | 0.000438 |
| Std | 112.48 | 8.94 | 0.012168 |
| Min | 49.81 | 9.14 | -0.109424 |
| 25th % | 95.86 | 13.35 | -0.004076 |
| 50th % | 157.90 | 16.87 | 0.000673 |
| 75th % | 255.21 | 22.54 | 0.005807 |
| Max | 463.92 | 82.69 | 0.145197 |

### Key Observations

**VIX Range:** The VIX ranged from a minimum of 9.14 to a maximum of 82.69, with a mean of 19.34. The large gap between the 75th percentile (22.54) and the maximum (82.69) confirms that extreme volatility readings are rare outliers.

**SPY Price:** The wide range in SPY price ($49.81 to $463.92) and high standard deviation ($112.48) reflect long-term market appreciation over the 20-year window rather than volatility. This is why daily returns are used instead.

**SPY Daily Return:** The mean daily return of 0.000438 (~0.04%) is consistent with historical U.S. equity market performance, compounding to approximately 11% annually. The minimum single-day return of -10.94% and maximum of +14.52% are both consistent with the extreme volatility observed during the COVID-19 market crash in March 2020.

### Categorical Variable

**High VIX Days:** One of the most important classification variables used in 
