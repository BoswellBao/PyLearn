'''
Python 迭代器（Iterators）对象在遵守迭代器协议时需要支持如下两种方法：
__iter__()，返回迭代器对象自身。这用在 for 和 in 语句中。
__next__()，返回迭代器的下一个值。如果没有下一个值可以返回，那么应该抛出 StopIteration 异常。
'''

class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):    # 如果没有这个方法，就会报类型错误-->TypeError: 'Counter' object is not iterable
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

a = Counter(5, 10)
for i in a:
    print(i, end=' ')
print()
print(type(a))


