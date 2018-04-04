#!/usr/bin/env python
# coding: utf-8
# __author__ = 'mcb'
# Email: miaocbin@126.com
# 


f = open("ci", 'r', encoding='utf-8')  # 文件句柄

# print(f.readline(15))

# print the all lines in file f.
for line in f.readlines():
    print(line.strip())

# print the first five lines.
# for i in range(5):
#     print(f.readline())

