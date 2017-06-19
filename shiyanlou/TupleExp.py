# 元组是由数个逗号分割的值组成；元组是不可变类型，这意味着不能在元组内删除或添加或编辑任何值
a = 'Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus'
print(a)

(x, y) = divmod(15, 2)    # divmod（a，b）返回两个元素的元组，第一个值是a除以b的取整，第二个值是余数
print('divmod:', x, y)

# 要创建只含有一个元素的元组，在值后面跟一个逗号。
one = (1,)
print("one:", type(one))    # tuple类型
two = (1)
print('two:', type(two))    # int类型
