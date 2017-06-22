'''
"r"，以只读模式打开，你只能读取文件但不能编辑/删除文件的任何内容
"w"，以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入
"a"，以追加模式代开，写入到文件中的任何数据将自动添加到末尾
'''
filepath1 = 'C:\\Users\\Administrator\\PycharmProjects\\PyLearn\\ForFileHandle1.txt'
filepath2 = 'C:\\Users\\Administrator\\PycharmProjects\\PyLearn\\ForFileHandle2.txt'

print('用open()打开文件，close()关闭文件：')
a = open(filepath1, 'r')
print(type(a))
a.close()


print('----------用read（）一次性读取文件所有内容：')
b = open(filepath1)
print(b.read())
b.close()

print('----------用readline（）按行读取文件：')
c = open(filepath1)
print(c.readline(), end=' ')
c.close()
print('或者循环读出每一行：')
d = open(filepath1)
for i in d:
    print(i.rstrip('\n'))    ###rstrip()可以去除指定的字符串
d.close()

print('----------用readlines（）把文件按行放进一个列表中：')
e = open(filepath1)
print(e.readlines())


print('----------用write()写文本：')
f = open(filepath2, 'w')
f.write('i am tom.i like apple.')
f.write('i am alice.\n')   ###用\n换行
f.write('i like banana')
f.close()
print('输出写的内容：')
g = open(filepath2)
for line in g:
    print(line.replace('\n', ''))    ###也可以用replace()把换行符去掉
g.close()



print('----------统计文件中的信息：')
h = open(filepath2)
space = 0
period = 0
line_num = 0
for i, line in enumerate(h):    ###enumerate()可以获取迭代器里面的索引及索引对应的值
    space += line.count(' ')    ###count()直接算出字符串中的目标元素的个数
    period += line.count('.')
    line_num = i + 1
print('ForFileHandle2文件中行数:%s，空格数:%s, 句号数:%s' %(line_num, space, period))    ###格式化输出




'''
在实际情况中，我们应该尝试使用 with 语句处理文件对象，它会文件用完后会自动关闭，就算发生异常也没关系。它是 try-finally 块的简写：
'''
print('----------用with...as...打开文件：')
with open(filepath2) as op:
    for line in op:
        print(line)





