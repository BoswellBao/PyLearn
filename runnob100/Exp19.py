'''
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

list_i = []
for i in range(1,1001):
    list_factor = []
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            list_factor.append(j)
    for k in list_factor:
        sum += k
    if sum == i:
        list_i.append(i)
print(len(list_i),list_i)