#如何捅破python编程的那层纸

       一些朋友自学python过程中，发现书也能看懂，书上的玩具代码也能看懂，但为啥自己不能做习题，不能写代码解决问题，自己不能动手写代码？
    原因是初学者没有学会计算思维、解决问题的方法、编程思路。
    编程思路的养成需要一个过程的，在编码过程中思考，多动手敲代码。
    有时候，想不明白的地方，有人稍微点破一下，那层纸就很容易破。
    请看下面的例子。
   

#编程思路一：
    经常有人问，一个文本文件，要抽取多少行以后的文本。
    相信记数循环，大家都看得懂，也会写。下面的代码就是利用记数循环来解决这个问题。

    代码一：
    一个几G的文本文件，需要每隔1000行写到新的文件中。
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
            if i % 1000 == 0:
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

#编程思路二：
    #coding:utf-8
    """
    本代码由迪艾姆公司黄老师所写，思路大家自己看代码。
    
    抓了a,b,c,d4名犯罪嫌疑人.其中有一名是小偷，审讯中：
            a说我不是小偷
            b说c是小偷
            c说小偷肯定是d
           d说c胡说！
    其中有3个人说的是实话，一个人说的是假话，编程推断谁是小偷。
    （用穷举法和逻辑表达式）
    
    """
    
    for xiaotu in ['a','b','c','d']:
    
          sum = (xiaotu != 'a') + (xiaotu == 'c') + (xiaotu == 'd') + (xiaotu !='d')
          if sum == 3:
              print "小偷是：%s " % xiaotu

总结：
     学习python编程，先学会过程式编程，再过度到面向对象的编程范式。
     学会函数抽象、类抽象。一步一步养成计算思维、学会解决问题的方法、编程思路。
     这个需要一个过程，也不要操之过急。
     看一下这些视频，可能对你有些帮助。
迪艾姆python培训_python编程思路－  
http://v.youku.com/v_show/id_XNTY0MDA5MDMy.html  
迪艾姆python培训_python编程思路二  
http://v.youku.com/v_show/id_XNTY0MDE1NzA0.html  
python爬虫之采集搜素引擎联想词  
http://www.tudou.com/programs/view/SXgshk-sYbw/  


[广告：如果自学有困难，建议参加迪艾姆python培训，可以节省学习成本。](https://github.com/pythonpeixun/article/blob/master/index.md)