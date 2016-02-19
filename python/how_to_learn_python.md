#运维如何通过学习python学会编程

运维必须懂开发，特别是python开发，已经形成大家的共识，不懂开发的运维，路会越走越窄。
黄哥，从2012年底，从事python教学过程中，接触到很多运维的朋友。部分运维是自学的Linux
或者是从运维培训班出来的。他们对编程懂很少或懂一些shell开发。

##部分运维运到的困难是：有的连书都不懂；有的书是可以看懂，别人写的简单代码也可以看懂，但自己不会写代码解决问题。

##黄哥提出一个观念：学习编程不止是学习语法，需要大力学习计算思维，解决问题的方法，算法，编程思路。

##何为计算思维：

        计算思维（Computational Thinking）概念的提出是计算机学科发展的自然产物。
        第一次明确使用这一概念的是美国卡内基·梅隆大学周以真（Jeannette M. Wing）教授。
        计算思维是运用计算机科学的基础概念去求解问题、设计系统和理解人类的行为；
        计算思维最根本的内容，即其本质是抽象和自动化。

##编程思路，其实就是计算思维的具体体现，用语法来表达解决问题的方法、算法。

#下面说说如何学习python

1、买一本好书，黄哥推荐看《python核心编程第2版》，书有一本足以。

2、边看书，需要边敲代码，书上每一个代码都需要敲一遍，敲的过程中，才能碰到问题。碰到问题，想办法
   解决，才能提高。

3、还需要做适当的习题来加强学习。

4、python有多种编程范式，面向过程，面向对象，函数式编程等。建议从面向过程学起。
  有的朋友好高骛远，连基本的逻辑表达式都没有搞清楚，循环和判断都没有搞清楚，就想学django。

      问题一:
      输出下面的样式 1,2,3,4,5,6,7,8,9,10
      很多初学者，会写出下面这样的代码，
      for i in range(1, 11):
          print str(i) + ",",
      输出结果为1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
      就百思不解的是怎么才能不输出最后一个逗号。黄哥告诉你，看书的时候知道if判断语句，但实际应用用不好。
      分析这个样式1,2,3,4,5,6,7,8,9,10 最后一个没有逗号，前面有逗号，这个明显是一个判断啊。
      所以代码这样写：
      n = 10
      for i in range(1, n+1):
          if i < n:
              print str(i) + ",",
          else:
              print str(i)

  问题二：
  记数循环，相信大部分都书上的玩具代码都可以看懂。
  那下面这个问题，初学者不一定想到用记数循环解决这个问题。
  代码一：
一个几M的文本文件，需要每隔100行写到新的文件中。
不要小看了计数循环,用计数循环和判断语句就可以解决这个问题。

      # coding:utf-8
      """
      迪艾姆python远程视频培训

      咨询:qq:1465376564

      """
      with open('dist_1.txt','r') as f1 ,open('dist_new.txt','w') as f2:
          i = 0
          for line in f1:
              i += 1
              if i % 100 == 0:
                  f2.write(line)

      代码二：
      请问一个日志文本文件有2000行，我要提取其中的100行到200行，怎么做？
      你可以试试下面的方法。
      别小看while计数循环，其实它可以用来干很多事。
      #coding:utf-8
      i = 0
      file1 = open("test.txt","r")
      file2 = open("out.txt","w")
      while True:
          line = file1.readline()
          i += 1
          if 100<=i and i<=200:
              file2.write(line)
          if i >200 :
              break
          if not line:
              break
      file1.close()
      file2.close()

5、函数抽象、需要掌握大的问题化解为小的问题，每一个小的问题用函数来解决，集成起来大的问题就解决了。

6、面向对象的类抽象，类就是由属性加方法构成的对象的蓝图。会用面向对象的思想建模。

总结：有不有编程思路,是自己能不能动手写代码的关键。掌握一些常用简单算法：穷举法，二分法，递推算法，递归算法，回溯算法等等；
     也是必要的。
     最重要的是解决问题的训练，有思路，能独立解决问题，才能在职场上战无不胜！

#如果自学有困难的朋友，或自学时间成本高的朋友，欢迎参加黄哥python培训，帮你快速完成不能写代码到自己能写代码的过渡。

黄哥联系方式：qq:1465376564 电话：18610508486

[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)  


#黄哥所写的文章

[如何捅破python编程的那层纸](https://github.com/pythonpeixun/article/blob/master/pythonstudy.md)  
[剪刀石头布小习题三种语言python2、php、go代码](https://github.com/pythonpeixun/article/blob/master/jdstb.md)  
[python2中汉字编码](https://github.com/pythonpeixun/article/blob/master/python_bianma.md)  
[如何捅破python编程的那层纸之二](https://github.com/pythonpeixun/article/blob/master/pythonstudy2.md)  
[如何捅破python编程的那层纸之三](https://github.com/pythonpeixun/article/blob/master/pythonstudy3.md)  
[go语言和python一行一行读文本文件比较](https://github.com/pythonpeixun/article/blob/master/goandpython.md)  
[python程序员如何加强搞定问题的能力](https://github.com/pythonpeixun/article/blob/master/python/about_problem_slove.md)  
[编程杂谈](https://github.com/pythonpeixun/article/blob/master/python/about_string.md)  
[python生成器处理文本文件大幅度提高效率](https://github.com/pythonpeixun/article/blob/master/python/python_file_yield.md)  
[全部用递归求第N个质数，不能用循环](https://github.com/pythonpeixun/article/blob/master/python/python_recursive_prime.md)  
[用python写一个程序，找出数组中差值为K的数共有几对](https://github.com/pythonpeixun/article/blob/master/python/python_answer_array.md)  
[这样理解python中的if name == 'main':](https://github.com/pythonpeixun/article/blob/master/python/python_main.md)  
[有数字N，循环从list中依次输出元素。](https://github.com/pythonpeixun/article/blob/master/python/echo_one_by_one.md)  
[python 反转嵌套list](http://www.oschina.net/code/snippet_1448389_53155)  
[有人问如何遍历取得类的子类或实例](http://www.oschina.net/code/snippet_1448389_47057)  
[http://www.oschina.net/code/snippet_1448389_47057](http://www.oschina.net/code/snippet_1448389_33561)  
[一段小代码说明@property装饰器的用法](http://my.oschina.net/pythonpeixun/blog/382586)  
[python 判断连续是0 或1 的最大次数](http://my.oschina.net/pythonpeixun/blog/380293)  
[黄哥通过代码来说明：python语法糖](http://my.oschina.net/pythonpeixun/blog/529801)  
