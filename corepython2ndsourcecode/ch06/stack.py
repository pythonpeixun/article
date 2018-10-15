#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
P145页代码
'''

stack = []


def pushit():
    stack.append(input('Enter new string: '))


def popit():
    if len(stack) == 0:
        print('Cannot pop from an empty stack!')
    else:
        print('Removed [', stack.pop(), ']')


def viewstack():
    print(str(stack))


def showmenu():
    prompt = """
p(U)sh
p(O)p
(V)iew
(Q)uit

Enter choice: """

    done = 0
    while not done:

        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            if choice not in 'uovq':
                print('invalid option, try again')
            else:
                chosen = 1

        if choice == 'q':
            done = 1
        if choice == 'u':
            pushit()
        if choice == 'o':
            popit()
        if choice == 'v':
            viewstack()


if __name__ == '__main__':
    showmenu()
