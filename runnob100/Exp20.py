'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

high = 100
sum = 0
list = []
time = 3
for i in range(time):
    list.append(high)
    high /= 2
for i in range(1,time):
    sum += list[i]*2
print(sum + list[0])
print(list[-1] / 2)