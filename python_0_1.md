#python 判断连续是0 或1 的最大次数  

[python北京周末培训班](https://github.com/pythonpeixun/article/blob/master/beijing_weekend.md )  
[python上海周末培训班 ](https://github.com/pythonpeixun/article/blob/master/shanghai_weekend.md)  
[c语言从入门到精通远程视频培训](https://github.com/pythonpeixun/article/blob/master/c_course.md)  

贴吧上有人问，从终端读入一个整数n，随机一个输入一个0 或1
判断连续是0 或1 的最大次数。如：
输入
0
0
0
1
1
1
1
0
1
0
1在连续输入中，出现4次

	#coding:utf-8
	"""python北京周末培训班 
	https://github.com/pythonpeixun/article/blob/master/beijing_weekend.md 
	python上海周末培训班 
	https://github.com/pythonpeixun/article/blob/master/shanghai_weekend.md 
	咨询:qq:1465376564 黄哥所写
	做这个练习题的思路是：做这个练习题的思路是：先用一个n次的循环，将0或1添加到一个list中，
      最后用一个循环加一个变量来计数，统计连续相等数字1或0的出现次数。

	"""

	input_lst = []
	total_num = []
	n = int(raw_input("please input n:\n").strip())
	for i in xrange(n):
	    number = int(raw_input("please input number:\n").strip())
	    input_lst.append(number)

	length = len(input_lst)

	j = 1
	for i in range(length - 1):
	    if input_lst[i] == input_lst[i+1]:
	        j += 1
	    else:
	        total_num.append(j)
	        j = 1
	total_num.append(j)

	print input_lst
	print total_num
	print max(total_num)
	

