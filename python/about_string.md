#编程杂谈  
     ##通过python、php、golang对实例对象的字符串表示语言比较


##python 代码  
    #coding:utf-8


    class Foo(object):

        def __str__(self):
            return "来自傻瓜类"

    foo = Foo()
    print foo

输出结果：来自傻瓜类
##php代码

      <?php

      class Foo {
        function __toString(){
          return "来自傻瓜类";
        }
      }

      $foo = new Foo();
      print $foo."\n";
输出结果：来自傻瓜类

##go语言代码
    package main

    import (
    	"fmt"
    )

    type Foo struct {
    	name string
    }

    func (foo *Foo) String() string {
    	return fmt.Sprintf("%s %s", "来自傻瓜类", foo.name)
    }
    func main() {
    	foo := &Foo{
    		name: "pythoner",
    	}
    	fmt.Println(foo)
    }
输出结果：来自傻瓜类 pythoner


以上三种语言实现相同功能语法有差别，但对实例对象的字符串表示，只是语法不同，表现的形式是一样。

学习编程只学语法是学不会编程的，需要学习计算思维－算法、解决问题的方法、编程思路等。这是你能看懂
代码但自己不能动手写代码的原因。欢迎有经济能力，有追求的青年参加黄哥的培训。

[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)
