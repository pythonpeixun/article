##跟黄哥学python序列文章之python 函数是第一类对象

有人问python函数可以返回函数，php如何实现一样的功能

python 中函数是第一类对象，函数名字是函数对象的引用，函数名可以赋值给变量，可以作为参数传递给函数，可以作为函数的返回值从函数中返回。

        #! /usr/bin/python
        #coding:utf-8
        """
        参加黄哥python远程视频培训,帮你完成从不会写代码到会写代码解决问题的过渡。
        python远程视频培训
        https://github.com/pythonpeixun/article/blob/master/index.md
        python北京周末培训班
        https://github.com/pythonpeixun/article/blob/master/beijing_weekend.md
        咨询:qq:1465376564  企业内训，个人培训，请咨询黄哥电话:18610508486
        """


        def f1(f2):
            def f3():
                return f2
            return f3


        def f2():
            print("I come from f2")

        foo = f1(f2) # 返回值函数
        print(foo()) # foo()的值还是函数
        #<function f2 at 0x10c0ab140>
        foo()()  # 带括号调用
        #I come from f2
有人问php如何实现上面的功能呢？

php匿名函数（Anonymous functions），也叫闭包函数（closures），允许 临时创建一个没有指定名称的函数。最经常用作回调函数（callback）参数的值。

        <?php


        $f2 = function(){
          return "I come from f2()";
        };

        function f1($func) {
          $f3 = function() use($func){
            return $func();
          };
          return $f3;
        }

        print f1($f2)();
        print "\n";
