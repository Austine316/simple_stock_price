import streamlit as st
import yfinance as yf
import pandas as pd

st.title(
"Simple Stock Price App")

st.write("""Shown are the stock **closing price** and **volume** of Largest companies.""")

@st.cache
def load_data():
    url = 'https://stockanalysis.com/stocks/'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

df = load_data()

#define the ticker symbol
company_code = list(df['Symbol'])
company_names = list(df["Company Name"])

company = st.selectbox("Select company", company_code)
selected_company_index = company_code.index(company)

tickerSymbol = company
#get data on this ticker
if company != "":
    st.header(f"{company_names[selected_company_index]}")
    
    tickerData = yf.Ticker(tickerSymbol)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2000-1-31', end='2021-12-31')
    # Open High Low Close Volume Dividends Stock Splits
    st.write(""" Closing Price""")
    st.line_chart(tickerDf.Close)
    st.write("""Volume Price""")
    st.line_chart(tickerDf.Volume)
