'''
斐波那契数列。1,1,2,3,5,8,13,21,34...
'''

list = [0,1]
for i in range(36):
    print(list[-1],end=" ")
    list.append(list[-1] + list[-2])


