
import pandas as pd
import streamlit as st
import yfinance as yf


st.title('Sahara Builder Imports')


tickers = ('LBS=F','CL=F','GC=F','SI=F')

dropdown =st.multiselect('Pick Your Commodity Price', tickers)

start =st.date_input('Start',value =pd.to_datetime('2021-01-01'))
end =st.date_input('End',value=pd.to_datetime('today'))


if len (dropdown)>0:
    df=yf.download(dropdown,start,end)['Adj Close']
    st.line_chart(df)
    
