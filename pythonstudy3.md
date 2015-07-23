 #如何捅破python编程的那层纸之三
   
   
	# coding:utf-8

	"""
	如何捅破python编程的那层纸之三
	贴吧上有人问
	定义一个函数，名字为sameSums(aList)，alist是一个整形list，函数作用是判断能分成两组，使得两组数字的和相等。若可以择返回值是true，若不可以返回值是false。如下例：
	sameSums([4, 7, 6, 3]) --> True //4+6 = 10 and 7 + 3 = 10
	sameSums([3, 3]) --> True
	sameSums([4, 12, 16]) --> True //4+12= 16 and 16
	sameSums([5, 1]) --> False
	这个题目，对初学者来说，有点难度，但稍微有点算法基础，编程思路，就不难。
	前面用贪心算法，只能满足上面4个测试用例的正确解决。
	如何捅破python编程的那层纸之二
	https://github.com/pythonpeixun/article/blob/master/pythonstudy2.md
	但是对[4, 5, 6, 7, 8]，[2, 2, 2, 3, 3]这样的list，不能解答出正确的答案。
	这个问题：可以用递归解题，也可以用动态规划解题，黄哥用这样的思路解一下，供初学者参考！
	解题思路：
	      1、如果sum(list) 是奇数，就不能将list拆分为2个和相等的list
	      2、如果sum(list)之和为偶数，就 sub_sum = sum(list)/2
	      2、列出所有可能的子集（子list）
	      3、判断子集是不是和 sub_sum相等，如果相等则可以拆分为2个和相等的list，
	         否则不可以
	本文由黄哥python培训，黄哥所写
	黄哥python培训试看视频播放地址
	https://github.com/pythonpeixun/article/blob/master/python_shiping.md

	"""
	import itertools


	def get_all_subset(lst):
	    """求list 所有子集合"""
	    tmp_lst = []
	    length = len(lst)

	    for i in xrange(1, length):
	        tmp_lst += (set(itertools.combinations(lst, i)))
	    return tmp_lst


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
	    sum_of_lsit = sum(int_list)
	    sub_sum = sum_of_lsit / 2
	    if sum_of_lsit % 2:
	        return False
	    all_subset = get_all_subset(int_list)
	    for item in all_subset:
	        if sum(item) == sub_sum:
	            return True
	    return False

	if __name__ == "__main__":
	    import doctest
	    doctest.testmod()
	    lst1 = [3, 9, 10, 30, 8]
	    lst2 = [4, 5, 6, 7, 8]
	    lst3 = [2, 2, 2, 3, 3]
	    print sameSums(lst1)
	    print sameSums(lst2)
	    print sameSums(lst3)





[迪艾姆python培训_python编程思路－  ]
(http://v.youku.com/v_show/id_XNTY0MDA5MDMy.html)

[迪艾姆python培训_python编程思路二  ]
(http://v.youku.com/v_show/id_XNTY0MDE1NzA0.html)

[python爬虫之采集搜素引擎联想词 ] 
(http://www.tudou.com/programs/view/SXgshk-sYbw/)


[广告：如果自学有困难，建议参加迪艾姆python培训，可以节省学习成本。](https://github.com/pythonpeixun/article/blob/master/index.md)