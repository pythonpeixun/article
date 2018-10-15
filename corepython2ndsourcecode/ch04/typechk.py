#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
PEP 0237: Essentially, long renamed to int. That is,
there is only one built-in integral type, named int;
but it behaves mostly like the old long type.
Python3 long这个数据类型取消了
'''


def displayNumType(num):
    print(num, 'is', end=",")
    if isinstance(num, (int, float, complex)):
        print('a number of type:', type(num).__name__)
    else:
        print('not a number at all!!')


displayNumType(-69)
displayNumType(9999999999999999999999)
displayNumType(98.6)
displayNumType(-5.2 + 1.9j)
displayNumType('xxx')
