 #如何捅破python编程的那层纸之二
   
   
	# coding:utf-8

	"""
	如何捅破python编程的那层纸之二
	贴吧上有人问
	定义一个函数，名字为sameSums(aList)，alist是一个整形list(限定重复元素不超过2个)，函数作用是判断能分成两组，使得两组数字的和相等。若可以择返回值是true，若不可以返回值是false。如下例：
	sameSums([4, 7, 6, 3]) --> True //4+6 = 10 and 7 + 3 = 10
	sameSums([3, 3]) --> True
	sameSums([4, 12, 16]) --> True //4+12= 16 and 16
	sameSums([5, 1]) --> False
	这个题目，对初学者来说，有点难度，但稍微有点算法基础，编程思路，就不难。
	先讲一个故事：二个小孩儿时从树上采板栗，最后合并一堆，分板栗，采集一人选一个的分。
	假定人性是贪婪的，第一个先选的人，选最大的，第二个选的人，选次大的，一直循环下去。
	贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。
	也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。
	这个题目：先将list从大到小排序，中间设置2个空的list，从大的开始选，下一次选的时候，需要
	比较一下和，如果谁的和小，再添加一个，直到最后一个元素。
	本文由黄哥python培训，黄哥所写
	黄哥python培训试看视频播放地址
	https://github.com/pythonpeixun/article/blob/master/python_shiping.md

	"""


	def sameSums(int_list):
	    """黄哥python培训 黄哥所写 qq:1465376564
	    >>> sameSums([4, 7, 6, 3])
	    True
	    >>> sameSums([3, 3])
	    True
	    >>> sameSums([4, 12, 16])
	    True
	    >>> sameSums([5, 1])
	    False
	    """
	    new_lst = sorted(int_list, reverse=True)
	    list1 = list()
	    list2 = list()
	    for n in new_lst:
	        if sum(list1) < sum(list2):
	            list1.append(n)
	        else:
	            list2.append(n)
	    return sum(list1) == sum(list2)

	if __name__ == "__main__":
	    import doctest
	    doctest.testmod()
	    lst = [3, 9, 10, 30, 8]
	    print sameSums(lst)





[迪艾姆python培训_python编程思路－  ]
(http://v.youku.com/v_show/id_XNTY0MDA5MDMy.html)

[迪艾姆python培训_python编程思路二  ]
(http://v.youku.com/v_show/id_XNTY0MDE1NzA0.html)

[python爬虫之采集搜素引擎联想词 ] 
(http://www.tudou.com/programs/view/SXgshk-sYbw/)


[广告：如果自学有困难，建议参加迪艾姆python培训，可以节省学习成本。](https://github.com/pythonpeixun/article/blob/master/index.md)