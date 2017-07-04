'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''

list = []
for i in range(3):
    list.append(int(input("输入：")))

list.sort()
for j in list:
    print(j)