import yfinance as yf
import streamlit as st
import numpy as np

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Largest companies.
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
company_names = ["Select company","AAPL","MSFT","GOOGL","GOOG","AMZN","TSLA","FB","NVDA","TSM","UNH","V","JPM"]
company = st.selectbox("",company_names)
tickerSymbol = company
#get data on this ticker
if company != "":
    tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High Low Close Volume Dividends Stock Splits

    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)