# 集合是一个无序不重复元素的集
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("集合自动去除重复的元素：",basket)


a = 'orange' in basket
print('输出某个元素是否在集合中的布尔值：', a)
b = 'pineapple' in basket
print('输出某个元素是否在集合中的布尔值：', b)


print('--' * 20 + '想要创建空集合，你必须使用 set() 而不是 {}：')
c = set()
print('这是个空集合：', c, type(c))
d = {}
print('这是个空字典：', d, type(d))


print('--' * 20 + '集合的逻辑运算：')
e = set('abracadabra')
f = set('alacazam')
print('去重后的集合e：', e)
print('去重后的集合f：', f)
g = e - f
print('在e中但不在f中的元素：', g)
h = e | f
print('在e或者f中的元素：', h)
i = e & f
print('e和f中都有的元素：', i)
j = e ^ f
print('存在e或f中，但不同时存在的元素：', j)


print('--' * 20 + '从集合里弹出元素和添加元素:')
k = {'a','e','h','g'}
k.pop()
print(k)
k.add('f')
print(k)