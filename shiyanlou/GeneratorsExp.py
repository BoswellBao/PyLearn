'''
生成器(Generators)是更简单的创建迭代器的方法，这通过在函数中使用 yield 关键字完成：
'''

def my_generators():
    print('inside my generators')
    yield 'a'
    yield 'b'
    yield 'c'
a = my_generators()
for i in a:
    print(i)
print(type(a), end='\n\n')



def counter_generator(low, high):
    while low <= high:
        yield low    #有了yield关键字，这个方法就变成了个迭代器，从dir（）中可以看到有__iter__和__next__方法
        low += 1
for i in counter_generator(5, 10):
    print(i, end=' ')
print(dir(counter_generator(1,2)))



'''
我们通常使用生成器进行惰性求值。这样使用生成器是处理大数据的好方法。如果你不想在内存中加载所有数据，你可以使用生成器，一次只传递给你一部分数据。
'''
print()
print('----------可以使用生成器产生无限多的值:')
def infinite_generator(start):
    while True:
        yield start
        start +=1
        if start > 20:
            break
infinite = infinite_generator(1)
for i in infinite:
    print(i, end=' ')
print('')
print('这样的生成器不能重复使用：')
for i in infinite:
    print(i)

print()
print('要想重复使用，需要升级到类，且得有__iter__方法：')
class infinite_repeatable_generator(object):
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        while True:
            yield self.start
            self.start += 1
            if self.start > 20:
                break
repeable = infinite_repeatable_generator(1)
print('第一次使用生成器：')
for i in repeable:
    print(i, end=' ')
print()
print('第二次使用生成器：')
for i in repeable:
    print(i, end=' ')


print()
print('-----------生成器表达式：')
generator_expression = (x*x for x in range(1,10))
print(type(generator_expression))
for i in generator_expression:
    print(i, end=' ')



