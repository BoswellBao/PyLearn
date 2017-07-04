'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

num = int(input("输入非素数："))
list = []
while True:    #while循环的目的是刷新j
    for j in range(2,int(num) + 1):
        if num % j == 0:
            list.append(j)
            num /= j
            break    #每次找到一个最小的因数，再跳出重新找商的一个最小因数
        else:
            continue
    if int(num) == 1:    #最后从2到自身-1都找不到因数，就跳出while循环
        break
    else:
        continue
print(list)