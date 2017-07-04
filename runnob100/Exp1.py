'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

data = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i==j or i==k or j==k):    # 用关键字or
                continue
            else:
                data.append(100 * i + 10 * j + k)
print("个数：", len(data))
print(data)