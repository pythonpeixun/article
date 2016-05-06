#跟黄哥学python序列文章之python二分查找算法

如果你感觉黄哥的文章对你有帮助请打赏，支付宝账号：18610508486@163.com


在计算机科学中，二分查找算法（binary search）、也称折半搜索（英语：half-interval search），  
二分搜索法、二分搜索、二分探索，是一种在有序数组中查找某一特定元素的搜索算法。  
搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；  
如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，  
而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。  
这种搜索算法每一次比较都使搜索范围缩小一半。  (来源于维基百科)

# 二分查找循环版  

		#! /usr/bin/python
		# coding:utf-8


		def binary_search_while(key, arr):
		    '''list 必须是排序好的
		    黄哥python培训_python编程思路之四 咨询qq:1465376564
		    http://www.tudou.com/programs/view/Z4IClY5Wj-g/
		    运维如何通过学习python学会编程
		    https://github.com/pythonpeixun/article/blob/master/python/how_to_learn_python.md
		    黄哥python远程视频培训班
		    https://github.com/pythonpeixun/article/blob/master/index.md
		    黄哥python培训试看视频播放地址
		    https://github.com/pythonpeixun/article/blob/master/python_shiping.md
		    '''
		    start = 0
		    end = len(arr) - 1
		    while start <= end:
		    	mid = start + (end - start) // 2
		    	if arr[mid] < key:
		    		start = mid + 1
		    	elif arr[mid] > key:
		    		end = mid - 1
		    	else:
		    		return mid
		    return -1

		if __name__ == '__main__':
		    arr = [3, 9, 28, 67, 12, 45]
		    arr.sort()
		    print(binary_search_while(12, arr))
		    print(binary_search_while(3, arr))
		    print(binary_search_while(9, arr))
		    print(binary_search_while(99, arr))



＃二分查找递归版  

		#! /usr/bin/python
		# coding:utf-8


		def binary_search_recursion(key, arr, start, end):
		    '''list 必须是排序好的
		    黄哥python培训_python编程思路之四 咨询qq:1465376564
		    http://www.tudou.com/programs/view/Z4IClY5Wj-g/
		    运维如何通过学习python学会编程
		    https://github.com/pythonpeixun/article/blob/master/python/how_to_learn_python.md
		    黄哥python远程视频培训班
		    https://github.com/pythonpeixun/article/blob/master/index.md
		    黄哥python培训试看视频播放地址
		    https://github.com/pythonpeixun/article/blob/master/python_shiping.md
		    '''
		    if start > end:
		        return -1
		    mid = start + (end - start) // 2
		    if arr[mid] > key:
		    	return binary_search_recursion(key, arr, start, mid - 1)
		    if arr[mid] < key:
		    	return binary_search_recursion(key, arr, mid + 1, end)
		    return mid


		if __name__ == '__main__':
		    arr = [3, 9, 28, 67, 12, 45]
		    arr.sort()
		    print(binary_search_recursion(12, arr, 0, len(arr)-1))
		    print(binary_search_recursion(3, arr, 0, len(arr)-1))
		    print(binary_search_recursion(9, arr, 0, len(arr)-1))
		    print(binary_search_recursion(99, arr, 0, len(arr)-1))


#用途实例：
白名单过滤，有一家商业银行，将数千万客户名单保存为文本文件中，为白名单。  
白名单处理成排序好的数组。可以用二分查找算法快速排除用户账号是不是银行的客户。

[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)

