'''
暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
'''

from time import sleep
list = [3,34,5,56,53,32]
for i in list:
    print(i)
    sleep(1)