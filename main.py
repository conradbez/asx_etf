import streamlit as st 
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials



tables_efts = pd.read_html('https://en.wikipedia.org/wiki/List_of_Australian_exchange-traded_funds')
efts = tables_efts[0]
assert len(efts[efts.eq('BetaShares').any(1)])>50

efts
