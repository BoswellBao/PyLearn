'''
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

a = input("输入a值：")
b = int(input("输入个数："))
listStr = []
listInt = []
sum = 0
for i in range(1,b+1):
    listStr.append(a * i)

str = " + ".join(listStr)

for i in listStr:
    listInt.append(int(i))

for i in listInt:
    sum += i
print(str + " = ", sum)