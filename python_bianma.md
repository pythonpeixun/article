#将python2中汉字会出现乱码的事一次性说清楚
	[https://github.com/pythonpeixun/article/blob/master/index.md](python远程视频培训班)
##为了让初学者，不再为python2中汉字出现乱码的事烦恼！

###请看python培训黄哥细细道来：
###1、写的代码模块需要指定编码
	如果代码没有指定coding,python就默认所有的字符为ASCII码,
	ASCII码只支持256个字符,ASCII码不支持中文,所以就报错。
	所以要在代码前写上#coding:utf-8或#coding:gbk
	但通用写上#coding:utf-8

###2、python2内部所有编码统一为unicode
	unicode可以处理世界上所有语言的字符。
	utf-8为unicode的一种实现形式，所以需要在代码前写上#coding:utf-8

###3、编码转换
	牢记python2内部编码为unicode.
	其它的编码decode()为unicode,再编码encode()为你指定的编码,就不会出现乱码。

###4、网页采集时
	代码指定#coding:utf-8
	如果网页的编码为gbk
	需要这样处理：
	html = html.decode('gbk').encode('utf-8')

###5、代码前也可以写#coding:gbk,但也要保证你的代码文件的保存格式为gbk.这个在windos下会出现这样的问题。

###6、字典等key或值的汉字问题
	#coding:utf-8
	dict1 ={1:'python周末培训班',2:'咨询010-68165761 QQ：1465376564'}

	print dict1
	# 这样输出的没有显示汉字，是显示汉字的其它编码

	dict2 ={1:'python视频培训班',2:'咨询010-68165761 QQ：1465376564'}
	for key in dict2:
	print dict2[key]

###7、unicode的汉字编码写到文本文件中
	需要根据文本文件的编码进行转换
	可以encode('utf-8')或encode('gbk')

总结：凡是报错信息中出现的错误包含“ASCII”，就是汉字编码的问题。
[https://github.com/pythonpeixun/article/blob/master/python_shiping.md](点击黄哥python培训试看视频播放地址)