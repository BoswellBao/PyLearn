'''
暂停一秒输出，并格式化当前时间。
'''

import time,datetime

for i in range(5):
    time.sleep(1)
    mytime = datetime.datetime.now()
    print(mytime)
    print(mytime.strftime("%Y-%m-%d %H:%M:%S"))
    print()