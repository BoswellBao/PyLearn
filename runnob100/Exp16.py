'''
输出指定格式的日期。
'''

import datetime
print(datetime.datetime.now().strftime("%d/%m/%Y"))
mytime = datetime.date(1993,12,17)
print(mytime)
mytimeNextDay = mytime + datetime.timedelta(days=1)
print(mytimeNextDay)
mytimeNextYear = mytime.replace(year=1994)
print(mytimeNextYear)