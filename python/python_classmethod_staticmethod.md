# python类的静态方法和类方法区别

## 先看语法，python 类语法中有三种方法，实例方法，静态方法，类方法。


	# coding:utf-8


	class Foo(object):
	    """类三种方法语法形式"""

	    def instance_method(self):
	        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

	    \@staticmethod
	    def static_method():
	        print("是静态方法")

	    \@classmethod
	    def class_method(cls):
	        print("是类方法")

	foo = Foo()
	foo.instance_method()
	foo.static_method()
	foo.class_method()
	print('----------------')
	Foo.static_method()
	Foo.class_method()

实例方法只能被实例对象调用，静态方法(由\@staticmethod装饰的方法)、类方法(由\@classmethod装饰的方法)，可以被类或类的实例对象调用。     
实例方法，第一个参数必须要默认传实例对象，一般习惯用self。     
静态方法，参数没有要求。    
类方法，第一个参数必须要默认传类，一般习惯用cls。  

## 静态方法、类方法使用区别或者说使用场景

1、类方法用在模拟java定义多个构造函数的情况。
由于python类中只能有一个初始化方法，不能按照不同的情况初始化类。    
参考django https://docs.djangoproject.com/en/1.9/ref/models/instances/
请看下面的代码。

	# coding:utf-8


	class Book(object):

	    def __init__(self, title):
	        self.title = title

	    \@classmethod
	    def create(cls, title):
	        book = cls(title=title)
	        return book

	book1 = Book("python")
	book2 = Book.create("python and django")
	print(book1.title)
	print(book2.title)

特别说明，静态方法也可以实现上面功能，当静态方法每次都要写上类的名字，不方便。

2、类中静态方法方法调用静态方法的情况。    
下面的代码，静态方法调用另一个静态方法，如果改用类方法调用静态方法，可以让cls代替类，    
让代码看起来精简一些。也防止类名修改了，不用在类定义中修改原来的类名。



	# coding:utf-8


	class Foo(object):
	    X = 1
	    Y = 2

	    \@staticmethod
	    def averag(*mixes):
	        return sum(mixes) / len(mixes)

	    \@staticmethod
	    def static_method():
	        return Foo.averag(Foo.X, Foo.Y)

	    \@classmethod
	    def class_method(cls):
	        return cls.averag(cls.X, cls.Y)

	foo = Foo()
	print(foo.static_method())
	print(foo.class_method())


3、继承类中的区别
从下面代码可以看出，如果子类继承父类的方法，子类覆盖了父类的静态方法，      
子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。    
子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。   


	# coding:utf-8


	class Foo(object):
	    X = 1
	    Y = 2

	    \@staticmethod
	    def averag(*mixes):
	        return sum(mixes) / len(mixes)

	    \@staticmethod
	    def static_method():
	        return Foo.averag(Foo.X, Foo.Y)

	    \@classmethod
	    def class_method(cls):
	        return cls.averag(cls.X, cls.Y)


	class Son(Foo):
	    X = 3
	    Y = 5

	    \@staticmethod
	    def averag(*mixes):
	        return sum(mixes) / 3

	p = Son()
	print(p.static_method())
	print(p.class_method())
	# 1.5
	# 2.6666666666666665

共勉！  
黄哥写于2016-5-24 下午 北京


[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

