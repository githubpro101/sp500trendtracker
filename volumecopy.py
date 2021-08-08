# https://youtu.be/NjEc7PB0TxQ
import time
import datetime
from datetime import timedelta
import pandas as pd

ticker= 'TSLA'
period1date=datetime.datetime.today()-datetime.timedelta(days=5)
period1=int(time.mktime(period1date.timetuple()))
period2=int(time.mktime(datetime.datetime.today().timetuple()))
interval='1d'


query_string=f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df=pd.read_csv(query_string)

print(df)