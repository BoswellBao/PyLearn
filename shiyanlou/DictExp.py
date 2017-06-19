'''
字典是是无序的键值对（key:value）集合，同一个字典内的键必须是互不相同的。一对大括号 {} 创建一个空字典。
'''

data = {'江西':'南昌', '浙江':'杭州', '江苏':'南京'}
print(data['江西'])


data['中国'] = '北京'
print('创建新的键值对:', data)


del data['江苏']
print('用del关键字可以删除指定的键值对:', data)


a = '抚州' in data
print('用in判断指定的键是否在字典中：', a)


print('dict() 可以从包含键值对的元组中创建字典:',end='')
b = dict((('Tom', 'boy'), ('Alice', 'girl')))
print(b)


print('--' * 20 + '遍历一个字典，使用字典的 items() 方法:')
for x, y in b.items():
    print('{} is {}'.format(x, y), end='    ')    #{}可以占位





