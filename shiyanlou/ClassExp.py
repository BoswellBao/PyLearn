'''
在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
'''

print('----------定义类：')
class FirstClass(object):
    i = 123
    def f(self):
        return 'hello python'
print('类的实例:')
a = FirstClass()
print('通过实例调用类的方法：', a.f(), end='\n\n')


class SecondClass(object):
    '''
    很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法
    类定义了 __init__() 方法的话，类的实例化操作会自动为新创建的类实例调用 __init__() 方法
    '''
    def __init__(self, para1, para2):
        self.para1 = para1 * para1
        self.para2 = para2 * para2
print('----------__int__方法：')
print('实例化SecondClass，要传入和__init__对应的参数：')
b = SecondClass(2, 3)
print('这时，b就初始化了两个属性：para1-->%s和para2-->%s' %(b.para1, b.para2), end='\n\n')



