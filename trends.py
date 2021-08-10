#source:https://www.youtube.com/watch?v=cuTUbPQk2R4&t=299s
from pytrends.request import TrendReq
from SP500 import stock1
import time

pytrends = TrendReq(hl='en-US')


all_keywords = stock1

keywords=[]

cat='0'
geo=''
timeframes=['today 5-y','today 12-m','today 3-m','today 1-m']
gprop=''

def check_trends():
    pytrends.build_payload(keywords, cat, timeframes[3], geo, gprop)

    data=pytrends.interest_over_time().to_csv('test1.csv',mode='a+')
    


for kw in all_keywords:
    keywords.append(kw)
    check_trends()
    keywords.pop()
    time.sleep(2)

