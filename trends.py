#source:https://www.youtube.com/watch?v=cuTUbPQk2R4&t=299s
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US')

all_keywords = ['Blockchain','Home alone','Food','Cycling','Beer','Wine']

keywords=[]

cat='0'
geo=''
timeframes=['today 5-y','today 12-m','today 3-m','today 1-m']
gprop=''

def check_trends():
    pytrends.build_payload(keywords, cat, timeframes[0], geo, gprop)

    data=pytrends.interest_over_time()
    mean=round(data.mean(),2)
    #average interest of the last 5 years
    avg=round(data[kw][-52:].mean(),2)
    #last year average interest
    avg2=round(data[kw][:52].mean(),2)
    #yearly average interest of 5 years ago. 
    trend=round(((avg/mean[kw])-1)*100,2)
    trend2=round(((avg/avg2)-1)*100,2)
    print('The average 5 years interest of '+kw+' was '+str(mean[kw]))
    print('The last year interest of '+kw+' compared to the last 5 years'+' has changed by '+str(trend)+'%.')

    #stable trend
    if mean[kw]>75 and abs(trend)<=5:
        print('The interest for '+kw+' is stable in the last 5 years.')
    elif mean[kw]>75 and trend>5:
        print('The interest for '+kw+' is stable and increasing in the last 5 years.')
    elif mean[kw]>75 and trend<-5:
        print('The interest for '+kw+' is stable and decreasing in the last 5 years.')
    #relatively stable trend
    elif mean[kw]>60 and abs(trend)<=15:
        print('The interest for '+kw+' is relatively stable in the last 5 years.')
    elif mean[kw]>60 and trend>15:
        print('The interest for '+kw+' is relatively stable and increasing in the last 5 years.')
    elif mean[kw]>65 and trend<-15:
        print('The interest for '+kw+' is relatively stable and decreasing in the last 5 years.')
    #seasonal
    elif mean[kw]>20 and abs(trend)<=15:
        print('The interest for '+kw+' is seasonal in the last 5 years.')
    #new keyword
    elif mean[kw]>20 and trend>15:
        print('The interest for '+kw+' is trending.')
    #declining keyword
    elif mean[kw]>20 and trend>15:
        print('The interest for '+kw+' is significantly decreasing.')
    #cyclical
    elif mean[kw]>5 and abs(trend)<=15:
        print('The interest for '+kw+' is cyclical in the last 5 years.')
    #new
    elif mean[kw]>0 and trend>15:
        print('The interest for '+kw+' is new and trending.')
    #Dying 
    elif mean[kw]>0 and trend<-15:
        print('The interest for '+kw+' is dying and out of trend.')
    #other
    else:
        print('This is something to be checked.')
    #comparison of interest in last year (Avg) and 5 years ago (Avg2)
    if avg2==0:
        print('This didn\'t exist 5 years ago.')
    elif trend2>15:
        print('The last year interest is quite higher when compared to 5 years ago.'+' It has increased by '+str(trend2)+'%.')
    elif trend2<-15:
        print('The last year interest is quite lower when compared to 5 years ago.'+' It has decreased by '+str(trend2)+'%.')
    else:
        print('The last year\'s interest is comparable to 5 years ago.'+' It has changed by '+str(trend2)+'%.')

    #just to break the list up so we can know where one starts and ends. 
    print('')

    






for kw in all_keywords:
    keywords.append(kw)
    check_trends()
    keywords.pop()
