# https://www.youtube.com/watch?v=CaB3o_PbTJU

from yahoo_fin.stock_info import *
from datetime import *

stock=tickers_sp500()
sp500=','.join(stock)
stock1=sp500.split(",")
print (stock1)

