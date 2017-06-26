'''
我们使用 try...except 块来处理任意异常。

它以如下方式工作：
    1、首先，执行 try 子句 （在 try 和 except 关键字之间的部分）。

    2、如果没有异常发生，except 子句 在 try 语句执行完毕后就被忽略了。

       如果在 try 子句执行过程中发生了异常，那么该子句其余的部分就会被忽略。

    3、如果异常匹配于 except 关键字后面指定的异常类型，就执行对应的 except 子句。然后继续执行 try 语句之后的代码。

    4、如果发生了一个异常，在 except 子句中没有与之匹配的分支，它就会传递到上一级 try 语句中。

    5、如果最终仍找不到对应的处理语句，它就成为一个 未处理异常，终止程序运行，显示提示信息。

'''

print('----------匹配到except后面的错误类型后，执行except子句，之后再执行try剩余部分的代码：')
a = 1
b = '2'
try:
    c = a + b
except TypeError:
    print('执行except子句。')
print('接着执行try之后的代码。',end=('\n') * 2)



print('----------用raise抛出异常：')
try:
    print('人为抛出异常。')
    raise TypeError()
except TypeError:
    print('捕获异常。', end='\n\n')


print('----------定义清理行为:')
try:
    raise TypeError
finally:
    print('无论异常有没有被处理，finally子句都得执行。')