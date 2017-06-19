import math
radius = input("请输入半径：")
int_radius = int(radius)
area = round(math.pi * math.pow(int_radius,2),10)
print(area)

#round(a, 10)  指定小数点后面10位数
#math.pow(3, 3)  3的3次方