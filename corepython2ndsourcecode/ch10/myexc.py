#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
P258页代码
八进制0 改为0o
'''

import os
import socket
import errno
import tempfile


class NetworkError(IOError):
    pass


class FileError(IOError):
    pass


def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)

    return tuple(myargs)


def fileArgs(fn, mode, args):
    if args[0] == errno.EACCES and \
            'access' in dir(os):
        perms = ''
        permd = {'r': os.R_OK, 'w': os.W_OK,
                 'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(fn, permd[eachPerm]):
                perms = perms + eachPerm
            else:
                perms = perms + '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')" % \
                    (mode, myargs[1], perms)

        myargs.append(args.filename)

    else:
        myargs = args

    return tuple(myargs)


def myconnect(sock, host, port):
    try:
        sock.connect((host, port))

    except socket.error as inst:
        myargs = updArgs(inst.args)        # convert inst to tuple
        if len(myargs) == 1:        # no #s on some errors
            myargs = (errno.ENXIO, myargs[0])

        raise Exception(NetworkError, updArgs(myargs, host + ':' + str(port)))


def myopen(fn, mode='r'):
    try:
        fo = open(fn, mode)
    except IOError as args:
        raise Exception(FileError, fileArgs(fn, mode, args))

    return fo


def testfile():

    fn = tempfile.mktemp()
    f = open(fn, 'w')
    f.close()

    for eachTest in ((0o0, 'r'), (0o100, 'r'), (0o400, 'w'), (0o500, 'w')):
        try:
            os.chmod(fn, eachTest[0])
            f = myopen(fn, eachTest[1])

        except FileError as args:
            print("%s: %s" % (args.__class__.__name__, args))
        else:
            print(fn, "opened ok... perms ignored")
            f.close()

    os.chmod(fn, 0o777)  # enable all perms
    os.unlink(fn)


def testnet():
    s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)

    for eachHost in ('deli', 'www'):
        try:
            myconnect(s, eachHost, 80)
        except Exception as args:
            print("%s: %s" % (args.__class__.__name__, args))


if __name__ == '__main__':
    testfile()
    testnet()
