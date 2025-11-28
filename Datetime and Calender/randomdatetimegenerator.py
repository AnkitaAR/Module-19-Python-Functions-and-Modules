import random
import time
from tracemalloc import start
def getRandomDate(startdate,enddate):
    print("Random Date Generation between",startdate,"and",enddate)
    r=random.random()
    dateFormat='%Y-%m-%d'
    startTime=time.mktime(time.strptime(startdate,dateFormat))
    endTime=time.mktime(time.strptime(enddate,dateFormat))
    randomTime=startTime+r*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
startdate='2016-01-01'
enddate='2018-12-12'
print("Random Date:",getRandomDate(startdate,enddate))