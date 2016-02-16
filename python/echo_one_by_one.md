#有数字N，循环从list中依次输出元素。  

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
也就是说输出全部元素外，又从头输出起。

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
