'''
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''

import math

for i in range(100,1000):
    a = i % 10
    b = int((i % 100)/10)
    c = int(i / 100)
    if i == math.pow(a,3) + math.pow(b,3) + math.pow(c,3):
        print(i)


