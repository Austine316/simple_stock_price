import streamlit as st
import yfinance as yf

st.title(
"Simple Stock Price App")

st.write("""Shown are the stock **closing price** and **volume** of Largest companies.""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
company_code = ["","AAPL","MSFT","GOOG","GOOGL","AMZN","TSLA","FB","NVDA","TSM","UNH","V","JPM"]
company_names = ["","Apple Inc", "Microsoft Corp", "Alphabet Inc (Google) Class C", "Alphabet Inc (Google) Class A", "Amazon.com, Inc", "Tesla, Inc", 
                 "Meta Platforms (Facebook)", "NVIDIA Corporation", "TAIWAN SEMICONDUCTOR MANUFACTURING COMPAN", 
                 "UNITEDHEALTH GROUP INCORPORATED", "Visa Inc", "JP MORGAN CHASE & CO."]

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
