print('----------检测回文的函数：')
def palindromeFunction(pa):
    return pa == pa[::-1]    ###检测是不是回文最简单的方法

if __name__ == '__main__':
   input = input('请输入：')
   if palindromeFunction(input):
       print(input + '是回文')
   else:
       print(input + '不是回文')




print('----------默认参数值：')
def default_para_value(a, b = -33):
    if a < b:
        print('True')
    else:
        print('False')
default_para_value(12)    ###有默认值，可以传一个参数
default_para_value(12, 21)




'''
map 是一个在 Python 里非常有用的高阶函数。它接受一个函数和一个序列（迭代器）作为输入，然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果。
'''
lists = [1,2,3,4,5]
def square(num):
    return num * num
square_list = map(square, lists)    ###列表中的每个元素经过函数square处理后组合成一个列表
print(list(square_list))