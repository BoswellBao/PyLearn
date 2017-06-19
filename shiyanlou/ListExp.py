a = [23, 45, 1, -3434, 43624356, 234]
a.append(87)
print('append:', a)

a.insert(2, 22)    #insert 在指定位置前面插入元素
print('insert:', a)

print('count:', a.count(1))    #count 计算出指定元素的个数

a.remove(-3434)    #remove 删除指定元素
print('remove:', a)

a.reverse()    #reverse 将列表反转
print('reverse:', a)

b = [1, 2, 3]
a.extend(b)    #extend 在a列表后面加入b列表的元素
print('extend:', a)

b = sorted(a)    #sorted 会将指定列表排序，赋值给新列表，不改变原来的列表
print('sorted--b:', b)
print('sorted--a:', a)

a.sort()    #sort 直接给原列表排序，会重置原列表
print('sort:', a)

del a[-1]    #用关键字删除指定位置元素
print('del:', a)

a.pop()    #没有指定索引时，就遵守后进先出的规则
print('pop:', a)
a.pop(1)
print('pop--i=1:', a)

print('列表推导式：')
c = [x**2 for x in range(10)]
print('一般推导式：', c)
d = [1, 2, 3]
e = [x**2 for x in [i**2 for i in d]]
print('嵌套推导式：', e)
f = [(x, y) for x in [1, 3, 4] for y in [3, 5, 7] if x!=y]
print('嵌套带条件的推导式：', f)
