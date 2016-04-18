# 跟黄哥学python序列文章之python方法链(method chaining)

## 写这篇文章来由，有朋友说下面这样的代码看不懂。
choice = raw_input("please input:\n").strip()[0].lower()   
很多对于有经验的程序员来说，这些都不是事，   
但对于初学者来说，看到这样的语法头有点大。  

## 这个其实是面向对象中方法链的概念。
## 请看维基百科上Method chaining的定义  

		Method chaining, also known as named parameter idiom,   
		is a common syntax for invoking   multiple method calls 
		in object-oriented programming languages.
		Each method returns an   object, allowing the calls 
		to be chained together in a single statement without requiring   
		variables to store the intermediate results.
		Local variable declarations are syntactic   
		sugar because of the difficulty humans have with deeply nested method calls.
		A method chain is also known as a train wreck due to the increase 
		in the number of methods that come one after another in the same 
		line that occurs as more methods are chained together
		even though line breaks are often added between methods.

## 具体在python中，请看黄哥的分析：   

	有的python初学者对python方法连续调用不是很清楚，像雾里看花一样。
	python一切都是对象，对象调用它的方法，如果带返回值，放回值也是对象，  
	这个返回值也有方法，当然就可以用点号调用它的方法，   
	如此下去，就是python方法链调用也。

## 如何设计方法链python代码  


	# coding:utf-8
	"""
	如何通过学习python学会编程
	https://github.com/pythonpeixun/article/blob/master/python/how_to_learn_python.md
	黄哥python远程视频培训班
	https://github.com/pythonpeixun/article/blob/master/index.md
	黄哥python培训试看视频播放地址
	https://github.com/pythonpeixun/article/blob/master/python_shiping.md
	黄哥python培训 咨询qq:1465376564
	"""


	class Person(object):
	    """方法链小sample"""

	    def name(self, value):
	        self.name = value
	        return self # 返回实例对象自己才能再调用实例对象的方法。

	    def work(self, value):
	        self.working = value
	        return self

	    def introduce(self):
	        print "你好, 我的名字:", self.name, ",我的工作:", self.working, ",教初学者学会编程!"

	person = Person()
	person.name("黄哥").work("黄哥python培训").introduce()


## php方法链代码  

		<?php
		/*
		黄哥php培训 咨询qq:1465376564
		https://github.com/pythonpeixun/article/blob/master/php_education.md
		*/


		class Person{
		    public $name;
		    public $working;

		    public function setName($value){
		        $this->name = $value;
		        return $this;
		    }

		    public function work($value){
		        $this->working = $value;
		        return $this;
		    }

		    public function introduce(){
		        echo "你好, 我的名字:".$this->name.",我的工作:".$this->working.",教初学者学会编程!\n";
		    }
		}

		$person = new Person();
		$person->setName("黄哥")->work("黄哥php培训")->introduce();


[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)

