#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
P148页代码
'''

queue = []


def enQ():
    queue.append(input('Enter new queue element: '))


def deQ():
    if len(queue) == 0:
        print('Cannot dequeue from empty queue!')
    else:
        print('Removed [', queue.pop(0), ']')


def viewQ():
    print(str(queue))


def showmenu():
    prompt = """
(E)nqueue
(D)equeue
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
            if choice not in 'devq':
                print('invalid option, try again')
            else:
                chosen = 1

        if choice == 'q':
            done = 1
        if choice == 'e':
            enQ()
        if choice == 'd':
            deQ()
        if choice == 'v':
            viewQ()


if __name__ == '__main__':
    showmenu()
