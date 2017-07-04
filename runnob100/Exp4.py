'''
输入某年某月某日，判断这一天是这一年的第几天？

分析：先把这个月之前的月总天数加起来，中途判断闰年及二月，再加上当月的天数
'''

Pdays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
Rdays = [0,31,29,31,30,31,30,31,31,30,31,30,31]
year = int(input("年："))
month = int(input("月："))
day = int(input("日："))
th = 0
if year>0 and 0<month<=12 and 0<day<=31:
    if year % 400 == 0 or (year%4 == 0 and year%100!=0):
        if month == 2 and day > 29:
            print("闰年2月最多29天")
        else:
            for i in range(month):
                th += Rdays[i]
            th += day
            print("%s-%s-%s是%s年的第%s天" % (year, month, day, year, th))
    else:
        if month == 2 and day > 28:
            print("平年2月最多28天")
        else:
            for i in range(month):
                th += Pdays[i]
            th += day
            print("%s-%s-%s是%s年的第%s天" %(year,month,day,year,th))
else:
    print("输入格式有误。")