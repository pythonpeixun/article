#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
'makeTextFile.py -- create text file'
P52页 中文版书上错误点
1、少一个变量fname = input('Enter file name: ')
2、书上11-14行（下面的代码22-26） 行代码没有缩进
'''


import os
ls = os.linesep

# get filename
while True:
    fname = input('Enter file name: ')
    if os.path.exists(fname):
        print("ERROR: '%s' already exists" % fname)
    else:
        break

# get file content (text) lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

# loop until user terminates input
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('DONE!')
