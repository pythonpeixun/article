#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
P175页代码
Python3 Removed dict.has_key() – use the in operator instead.
'''

db = {}


def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = input('passwd: ')
    db[name] = pwd


def olduser():
    name = input('login: ')
    pwd = input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        pass
    else:
        print('login incorrect')
        return

    print('welcome back', name)


def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)

            if choice not in 'neq':
                print('invalid menu option, try again')
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()


if __name__ == '__main__':
    showmenu()
