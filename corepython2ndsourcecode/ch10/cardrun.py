#!/usr/bin/env python
# coding:utf-8
'''
欢迎参加黄哥python远程视频培训,
帮你完成从不会写代码到会写代码解决问题的过渡。
https://github.com/pythonpeixun/article/blob/master/index.md
咨询qq:1465376564
黄哥Python培训 黄哥改写
Python 3
P246页代码
'''


def safe_float(object):
    'safe version of float()'
    try:
        retval = float(object)
    except (TypeError, ValueError) as diag:
        retval = str(diag)
    return retval


def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')
        else:
            log.write('ignored: %s' % result)
    print('$%.2f (new balance)' % (total))
    log.close()


if __name__ == '__main__':
    main()
