#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
'readTextFile.py -- read and display text file'
'''


# get filename
fname = input('Enter file name: ')
print()

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print("*** file open error:", e)
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine, end=",")
    fobj.close()
