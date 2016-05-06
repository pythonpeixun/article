# 跟黄哥学习python第一章


## 完事开头难，千里之行始于足下。

## 为啥要学习python

		1、python是一门容易人们的语言，便于快速学习，快速应用到业务上。    
		2、python 有丰富的自带标准库和大量的第三方库。      
		3、python应用广泛。    
				（1）web开发。  
				（2）爬虫。   
				（3）linux下网络编程、特别是高并发服务端设计（高并发大流量分布式服务器后台开发）。  
				（2）机器学习和数据挖掘；  
				（3）图像处理、游戏开发等。  
				（4）云计算。  
				（5）ERP。  
				 (6) 科学计算、生物计算。  
				 (7) 运维自动化。  
				 (8)测试自动化等等方面。  

		4、学习python可以让一些想从事IT行业的朋友，通过学习python学会编程，快速进入到IT行业。
		    

## 学习python 2 还是 python 3      
	为啥有那么多python      
		CPython是用C语言实现的Python解释器。作为官方实现，它是最广泛使用的Python解释器。    
		除了CPython以外，还有用Java实现的Jython，用.NET实现的IronPython，    
		使Python方便地和Java程序、.NET程序集成。另外还有一些实验性的Python解释器比如PyPy。    
		本书以cpython 也就是常说的python为主。    

	python 有两个版本，python 2 和 python 3 ，学习python2 还是3，这个不是一个问题。     
	学习编程不是纯学语法，是学习编程思路，python 2 和 3 都姓“python“，   
	差别没有那么大，差别可以通过查文档解决。所以根据自己的喜好选择python 2 还是 python 3。      
	目前工作上大家还在用python 2。   


## 为啥要在linux下学习python

	提到Linux，部份人不熟悉，不熟悉没有关系，不熟悉可以学习啊。   
	白纸才好写字，python不是也不熟悉吗？   
	可以在学习python的同时，在Linux操作系统下学习，同时学会了python 和Linux，一举两得，多好的事。   

	1、python以后开发的程序，大部分跑在Linux操作系统下，以后工作环境需要用到Linux，你说该学吗？   

	2、企业招聘要求会Linux，你说该学吗？   

	3、连微软都拥抱Linux，你说该学吗？   

	4、在windows下学习，会碰到各种麻烦问题，换一个没有病毒，学习python造成障碍少的操作系统，你说该学吗？   

## linux 可以选择centos，或ubuntu。   
   可以先择独立安装或通过虚拟机安装。    
   [安装ubuntu，请看](http://www.ubuntu.com/download/desktop/install-ubuntu-desktop)。    
   [安装centos，请看](https://wiki.centos.org/HowTos/InstallFromUSBkey)  


## 如何安装python  

python下载  
windows平台  
电脑64位     
[python 3.5.1](https://www.python.org/ftp/python/3.5.1/python-3.5.1-amd64.exe)  
[python 2.7.11](https://www.python.org/ftp/python/2.7.11/python-2.7.11.amd64.msi)  
 下载后双击安装  
 电脑32位   
[python 3.5.1](https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe)  
[python 2](https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi)  
下载后双击安装  
特别提示：winodws下需要设置环境变量  (Excursus: Setting environment variables)  
请看http://docs.python.org/2/using/windows.html  
使得cmd下任意路径输入python,没有报错信息，表示正确安装好了。  
特别提示：安装是选择添加path，自动设置好环境变量。  



mac 下 64位 下载这个     
[python 3.5.1](https://www.python.org/ftp/python/3.5.1/python-3.5.1-macosx10.6.pkg)  
[python 2.7.11](https://www.python.org/ftp/python/2.7.11/python-2.7.11-macosx10.6.pkg)  
点击安装  
 
 32位 
 [python 3.5.1](https://www.python.org/ftp/python/3.5.1/python-3.5.1-macosx10.5.pkg)    
 [python 2.7.11](https://www.python.org/ftp/python/2.7.11/python-2.7.11-macosx10.5.pkg)    

   
linux 下 以ubuntu为例

（1）下载

      在python官网中下载python2.7.9安装包 http://python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz

（2）解压

      tar   -zvf Python-2.7.9.tar.xz

（3）编译安装

      cd Python-2.7.9

      ./configure

      make 

      sudo make install

python默认安装目录在/usr/local/lib/python2.7，终端shell下python -V 查看版本号

（4）更改系统默认版本

       sudo rm /usr/bin/python

       sudo ln -s /usr/include/python2.7 /usr/bin/python

这样在终端输入python显示的默认版本就是2.7.9了


# 操作系统有了，得会常用的命令

	linux shell，一种壳层与命令行界面，是linux操作系统下传统的用户和计算机的交互界面。
	第一个用户直接输入命令来执行各种各样的任务。普通意义上的shell就是可以接受用户输入命令的程序。   
	它之所以被称作shell是因为它隐藏了操作系统低层的细节。   
	同样的linux下的图形用户界面GNOME和KDE，有时也被叫做“虚拟shell”或“图形shell”。   
	linux操作系统下的shell既是用户交互的界面，也是控制系统的脚本语言。   
	当然在这点也有别于Windows下的命令行，虽然也提供了很简单的控制语句。   
	在Windows操作系统下，可能有些用户从来都不会直接的使用shell，  
	然而在linux系列操作系统下，shell仍然是控制系统启动、XWindow启动和很多其他实用工具的脚本解释程序。

	常用的命令:  
			mkdir 创建目录   
			rmdir 删除目录   
			cd    切换目录  
			pwd 显示目录  
			ls 列目录  
			cp 复制文件
			mv 更改文件名
			rm 删除文件
			chmod 改变权限
			cat 编辑文件
			less 显示文件内容

[学习Linux command 请参考](http://linuxcommand.org/lc3_learning_the_shell.php)


# 常用ide或编辑器
1、[pycharm](https://www.jetbrains.com/pycharm/download/)  
2、[atom](https://atom.io/)  
3、[sublime text](https://www.sublimetext.com/3)  
4、[Visual Studio Code](https://code.visualstudio.com/)  
5、[wingide](https://wingware.com/downloads)  
6、[liclipse pydev](http://www.liclipse.com/download.html)  
7、vim  
8、emacs  
........  
萝卜白菜各有所爱，选择适合自己的.  

## 学习方法   

1、动手，又动脑，一定要自己敲代码。  

2、[如何通过学习python学会编程](https://github.com/pythonpeixun/article/blob/master/python/how_to_learn_python.md)  

如果你感觉黄哥的文章对你有帮助请打赏，支付宝账号：18610508486@163.com

[跟黄哥学习python第二章](learn_python_follow_brother_huang_2.md)

[黄哥python培训_python初学者的第一步](http://www.tudou.com/programs/view/pZvrOt9RlmE/)
[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)  

