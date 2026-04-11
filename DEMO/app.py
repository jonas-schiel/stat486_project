import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import yfinance as yf
from datetime import datetime, timedelta
import os

st.set_page_config(page_title="Market Crisis Detector", layout="wide")
st.title("Market Crisis Detection — Gradient Boosting")
st.write("Anomaly prediction model trained on 2005–2024 market")

@st.cache_resource
def load_model():
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, '..', 'analysis', 'models', 'best_mod', 'best_model.pkl')
    return pickle.load(open(path, 'rb'))

@st.cache_data
def load_data():
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, '..', 'data', 'marketdata.csv')
    data = pd.read_csv(path)
    data['Date'] = pd.to_datetime(data['Date'])
    return data

model = load_model()
data = load_data()

features = ['Vix', 'VIX_roll_10', 'VIX_roll_20', 'VIX_day_change', 'VIX_sd',
            'SPY_roll_10', 'SPY_roll_20', 'SPY_roll_60', 'SPY_day_return',
            'SPY_5_day_return', 'SPY_20_day_return', 'QQQ_day_return',
            'IWM_day_return', 'TLT_day_return', 'GLD_day_return', 'SPY_drawdown',
            'QQQ_drawdown', 'IWM_drawdown', 'SPY_TLT_corr_20', 'SPY_TLT_corr_60',
            'SPY_GLD_corr_20', 'SPY_VIX_corr_20', 'SPY_vol_ratio', 'QQQ_vol_ratio',
            'IWM_vol_ratio', 'spy_above_avg']

y = data['market_crisis'].reset_index(drop=True)
dates = data['Date'].reset_index(drop=True)

crisis_periods = [
    ("2007-10-01", "2009-03-31", "GFC"),
    ("2010-04-23", "2010-07-02", "Flash Crash"),
    ("2011-07-22", "2011-10-03", "Debt Ceiling"),
    ("2015-08-01", "2016-02-29", "China/Oil"),
    ("2018-10-01", "2018-12-31", "Rate Hike"),
    ("2020-02-19", "2020-03-23", "COVID"),
    ("2022-01-01", "2022-10-31", "Inflation"),
]

st.subheader("Predicted Crisis Probabilities (2005–2024)")

probs = model.predict_proba(data[features])[:, 1]
smoothed = pd.Series(probs).rolling(window=10).mean().reset_index(drop=True)

fig, ax = plt.subplots(figsize=(16, 5))
ax.plot(dates, smoothed, color='steelblue', linewidth=1.2, label='Crisis Probability (10-day avg)')
ax.axhline(y=0.5, color='red', linestyle='--', linewidth=1, label='Decision Threshold (0.5)')
for start, end, label in crisis_periods:
    ax.axvspan(pd.Timestamp(start), pd.Timestamp(end), alpha=0.1, color='red')
    ax.text(pd.Timestamp(start), 0.95, label, fontsize=7, color='dimgray')
ax.set_xlim(dates.min(), dates.max())
ax.set_ylim(0, 1)
ax.set_xlabel('Date')
ax.set_ylabel('Crisis Probability')
ax.legend()
plt.tight_layout()
st.pyplot(fig)


st.subheader("Single Day Lookup")
st.write("Select a date to see the model's crisis probability and prediction for that day.")
date_options = data['Date'].dt.strftime('%Y-%m-%d').tolist()
selected_date = st.selectbox('Select a Date', date_options)
idx = data[data['Date'] == selected_date].index[0]
prob = probs[idx]
predicted = 'CRISIS' if prob >= 0.5 else 'NORMAL'
actual = 'Crisis' if y[idx] == 1 else 'Normal'

col1, col2, col3 = st.columns(4)
col1.metric('Crisis Probability', f'{prob:.1%}')
col2.metric('Model Prediction', predicted)
col3.metric('Actual Label', actual)
