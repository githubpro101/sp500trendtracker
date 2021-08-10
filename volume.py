# https://www.youtube.com/watch?v=CaB3o_PbTJU
# https://towardsdatascience.com/historical-stock-price-data-in-python-a0b6dc826836
import yfinance as yf
from yahoo_fin.stock_info import *
from datetime import date, timedelta


period1date=date.today()-timedelta(days=15)
period1date1=period1date.strftime('%Y-%m-%d')
period2=date.today().strftime('%Y-%m-%d')
stock=tickers_sp500()
sp500=' '.join(stock)

data = yf.download(sp500, start=period1date1, end=period2, interval='1d').to_csv('test.csv')





