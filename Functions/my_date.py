import datetime
import time
import calendar

# print(time.localtime())
#
# localTime = time.asctime(time.localtime(time.time()))
# print(localTime)

import datetime
from datetime import date
import calendar


def findDay(date):
    day, month, year = (int(i) for i in date.split('/'))
    born = datetime.date(year, month, day)
    return born.strftime("%A")



date = '04/07/1776'
print(findDay(date))
