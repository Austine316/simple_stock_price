
import yfinance as yf
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="4M",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# > Creator: Gordon D. Pisciotta  ·  4M  ·  [modern.millennial.market.mapping]",
    }
)

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Largest companies.
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
company_names = ["","AAPL","MSFT","GOOGL","GOOG","AMZN","TSLA","FB","NVDA","TSM","UNH","V","JPM"]
company = st.selectbox("Select company",company_names)
tickerSymbol = company
#get data on this ticker
if company != "":
    tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High Low Close Volume Dividends Stock Splits
    st.write("""## Closing Price""")
    st.line_chart(tickerDf.Close)
    st.write("""## Volume Price""")
    st.line_chart(tickerDf.Volume)