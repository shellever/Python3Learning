#!/usr/bin/python
# -*- coding: utf-8 -*-


# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
'''
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
'''