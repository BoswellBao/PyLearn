'''
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

str = input("输入一行字符串：")
alpha = 0
space = 0
digit = 0
other = 0
for i in str:
    if i.isalpha():
        alpha += 1
    if i.isspace():
        space += 1
    if i.isdigit():
        digit += 1
    else:
        other += 1
print("%s中有%s个字母，有%s个空格，有%s个数字，其他字符%s个。" %(str, alpha, space, digit, other))