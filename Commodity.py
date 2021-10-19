# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:29:18 2021

@author: deand
"""
import pandas as pd
import streamlit as st
import yfinance as yf


st.title('Sahara Builder Imports')


tickers = ('LBS=F','CL=F','GC=F','SI=F')

dropdown =st.multiselect('Pick Your Commodity Price', tickers)

start =st.date_input('Start',value =pd.to_datetime('2021-01-01'))
end =st.date_input('End',value=pd.to_datetime('today'))


# below code can be used to calculate the relative return of an asset
#def relativeret(df):
  #rel= df.pct_change ()
   #cumret=(1+rel).cumprod()-1
    #cumret=cumret.fillna(0)
    #return cumret

if len (dropdown)>0:
    df=yf.download(dropdown,start,end)['Adj Close']
    #df=relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.line_chart(df)
    
