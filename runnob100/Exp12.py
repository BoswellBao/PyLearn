'''
判断101-200之间有多少个素数，并输出所有素数。
'''

list = []
for i in range(101,201):
    flag = 0
    for j in range(2,int((i + 1) / 2)):
        if i % j == 0:    # 只要有能整除的,变flag的值，并立即跳到下一个i值
            flag = 1
            break
        else:
            continue
    if flag == 0:    # 第二层循环出来flag还是0，说明该i值是素数
        list.append(i)
    else:
        continue
print("共有素数个数：", len(list))
print(list)