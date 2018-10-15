#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
P201页代码
'''


def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('largest factor of %d is %d' % (num, count))
            break
        count -= 1
    else:
        print(eachNum, 'is prime')


for eachNum in range(10, 21):
    showMaxFactor(eachNum)
