#!/usr/bin/env python
# coding: utf-8
# __author__ = 'mcb'
# Email: miaocbin@126.com
# 

# 元组(tuple)
tuple_0 = (1, 3, 5, 7, 9)
print('元组--->', tuple_0)

# 列表[list]
list_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_1 = [2, 4, 6, 8, 0]
list_2 = [2, 4, 6, 66, 44, 22, 88, 20]

print('列表--->', list_1)

# 字典(dict)
dict_1 = {'name': 'john', 'age': 20, 'sex': 'male'}
print('字典--->', dict_1)

# 集合,列表转换为集合
list_1 = set(list_1)

print('集合--->', list_1)

# 元组转换为集合
aaa = set(tuple_0)
print('集合--->', aaa)




