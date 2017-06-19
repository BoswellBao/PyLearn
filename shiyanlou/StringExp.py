print('----------title方法，把字符串变成标题格式，首字母大写：')
a = 'god is a girl'
b = a.title()
print(b)


print('----------swapcase将字符串的大小写互换：')
c = 'aBcDeFgH'
d = c.swapcase()
print(d)


print('----------isalnum判断字符串中的字符是否都是字母数字：')
e = 'adfe df'
f = 'fsafsf'
print(e.isalnum(), f.isalnum())


print('----------isalpha判断字符串中字符是否都只是字母：')
g = 'ff3gr'
h = 'guhk'
print(g.isalpha(), h.isalpha())


print('检查字符串\'fse332334\'的字符是否都是数字：', 'fse332334'.isdigit())
print('检查字符串\'DFfrgregr\'是否都是小写:', 'DFfrgregr'.islower())
print('检查字符串\'DFfrgregr\'是否都是大写:', 'DFfrgregr'.isupper())
print('检查字符串\'God Is a Girl\'是否是标题格式:', 'God Is a Girl'.istitle())


print('----------split()可以分割任何字符串，默认以空格分割，也可以加分割的参数,没有空格就生成一个元素的列表：')
i = 'fsfa,fasf fa,fd fe,rge'
j = i.split()
print(j)
k = i.split(',')
print(k)


print('----------join()使用指定字符连接多个字符串，它需要一个包含字符串元素的列表作为输入然后连接列表内的字符串元素。')
l = '-'.join('i love you'.split())
print(l)


print('-----------find() 能帮助你找到第一个匹配的子字符串，没有找到则返回 -1。')
m = "faulty for a reason"
print(m.find('for'))
print(m.find('fora'))


print('----------startswith和endswith判断开头是否由指定字符串开始结尾：')
print(m.startswith("fa"))
print(m.endswith('aon'))


