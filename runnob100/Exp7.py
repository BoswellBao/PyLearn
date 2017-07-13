'''
将一个列表的数据复制到另一个列表中。
'''

list1 = [1,3,5,6,7,8]
list2 = []
for i in range(len(list1)):
    list2.append(list1[i])
print(list2)

list3 = list1[:]    # 简单
print(list3)

