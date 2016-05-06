#有数字N，循环从list中依次输出元素。  

如果你感觉黄哥的文章对你有帮助请打赏，支付宝账号：18610508486@163.com


[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)  

晚上qq上有一个朋友，问我问题，提交的代码，简直没有办法看，需求也说不清楚。
这个是没有经过任何编程思路训练初学者常见问题，解决问题无从下手。硬搬一些语法，拼凑一些代码。
例子：
lst = ['A', 'B', 'C', 'D']
N = 15
要求输出结果是  
    A  
    B  
    C  
    D  
    A  
    B  
    C  
    D  
    A  
    B  
    C  
    D  
    A  
    B  
    C  
也就是说输出全部元素完，又从头输出起。

#解决这个问题，可以从循环方面着手写代码，但明显是一个队列的问题，可以用python的双端队列。

首先请看循环硬写代码

    #coding:utf-8


    def echo_one_by_one(lst, i):
        return lst[i]

    lst = ["A", "B", "C", "D"]
    n = 15
    length = len(lst)
    i = 0
    j = 0
    length = len(lst)
    while i < n:
        if i % length or j == 0:
            print echo_one_by_one(lst, j)

        elif i % length == 0 and i != 0:
            j = -1
            i -= 1
        i += 1
        j += 1


for 循环    

        #! /usr/bin/python
        #coding:utf-8


        def from_begin_to_end(lst, n):
            '''for 循环，辅助j,计算循环,窍门在于 ％4 == 0
             j = 0
            '''
            j = 0
            for i in range(1, n + 1):
                print lst[j]
                j += 1
                if i % 4 == 0:
                    j = 0

        if __name__ == '__main__':
            lst = ['A', 'B', 'C', 'D']
            n = int(raw_input('please input n:\n'))
            from_begin_to_end(lst, n)


下面是队列实现  

    #coding:utf-8

    import collections


    def echo_one_by_one(lst, n):
        d = collections.deque(lst)
        for i in range(n):
             tmp = d.popleft()
             print tmp
             d.append(tmp)

    lst = ["A", "B", "C", "D"]
    n = 15
    echo_one_by_one(lst, n)
