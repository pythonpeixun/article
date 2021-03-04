# 跟黄哥学习python第五章

# 顺序结构、判断结构

#顺序结构
顺序结构的程序设计是最简单的，只要按照解决问题的顺序写出相应的语句就行，它的执行顺序是自上而下，依次执行。    
通俗一点的说法，就是代码从上到下一行一行的执行。    
请看下面求圆面积代码，代码中，请注意，幂运算的优先级高于乘法，所以乘法放前面后面都可以。    
```
'''
python 3 代码演示顺序结构
'''

PI = 3.14159
radius = 3
area1 = PI * radius ** 2
area2 = radius ** 2 * PI
print("area = {0}".format(area1))
print("area = {0}".format(area2))
# area = 28.27431
# area = 28.27431
```

如果只有顺序结构，这样程序的灵活性不够，能解决的问题太少，计算机科学家设计编程语言的时候，设计了可以做选择的判断结构
和可以反复做一件事儿的循环结构。


#布尔表达式（逻辑表达式）
布尔表达式是一个能计算出一个布尔值True或False的表达式。

## 布尔类型
布尔类型的类型名是bool类，这个类型只有两个字面量 True 和 False（注意大小写形式），   
它们表示两个逻辑常量，True 计算出 True（表示逻辑值“真”），   
False 计算出 False（表示逻辑值“假”）。   

Python中任何对象，在if 语句，while 语句，或逻辑操作符中，都可以检测出真假值。   

下面的值，都会被检测出一个为假的值。   
None，False，0, 0.0,空字符串'', 空元组(), 空列表[]， 空字典{}。   
instances of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns the integer zero or bool value False.   
除上面的以外，都为真。   
是真还是假，用bool类检测一下，就知道！    
```
'''
逻辑真假值
'''
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))

print(bool('黄哥python培训'))

#False
#False
#False
#False
#False
#False
#False
#True
```

## 逻辑运算符 （布尔运算符）   

	Boolean Operations — and, or, not
	
	运算符(Operation)	    计算结果(Result)	     优先级
	x or y	if x is false, then y, else x	     (1)
	x and y	if x is false, then x, else y	     (2)
	not x	if x is false, then True, else False (3）
	
	逻辑运算符优先级，not 最高，and 第二， or 第三。
	not 运算符优先级低于其它非逻辑运算符，not a == b 相当于 not (a == b),
	如果写成 a == not b 就会报语法错误。
	逻辑短路，计算2个值和一个逻辑运算符组成的表达式。
	x or y 只有当 bool(x) 为False时，才会计算后面的y，否则直接得出表达式的值。
	下面的代码发生短路情况，0为除数不合法，但发生短路，3/0没有被计算。
	>>> 1 or 3 / 0   
	    1
	x and y 只有当 bool(x) 为True时，才会计算后面的y。
	下面的代码发生短路情况
	>>> 0 and 3 / 0
	    0
	
	特别提示：初学者在布尔表达式中，有几个纠结。
	有的朋友说，下面这样的表达式为啥不发生短路。为啥结果不是0，而是[]
	>>> 0 and 3 / 0 or None and 1 or []
	   []
	黄哥的解答是，逻辑短路，计算2个值和一个逻辑运算符组成的表达式，0 and 3 / 0 发生了短路，
	0 and 3 / 0计算结果为0，但整个表达式求值没有完，要继续计算 0 and 3 / 0 or None and 1 or [] 变为
	0 or None and 1 or [],前面说了and 优先级高于or,0 or None and 1 or []相当于
	0 or (None and 1) or [],进一步简化，0 or None or [],再看上面
	x or y	if x is false, then y, else x， 所以0 or None or [] 计算为None or []
	最后结果为[]
	
	第二个纠结是：
	>>> 3 and 4
	   4
	
	结果为4，有的朋友纠结说，为啥不是True。
	文档上说了x and y	if x is false, then x, else y。

真值表   
```
'''
演示 and or 的八种组合运算
'''

print("----------------------真值表------------------")
print("True and True 结果为:{0}".format(True and True))
print("True and False 结果为:{0}".format(True and False))
print("False and True 结果为:{0}".format(False and True))
print("False and False 结果为:{0}".format(False and False))
print("True or True 结果为:{0}".format(True or True))
print("True or False 结果为:{0}".format(True or False))
print("False and True 结果为:{0}".format(False and True))
print("False and False 结果为:{0}".format(False and False))
print("----------------------over------------------")

# ----------------------真值表------------------
# True and True 结果为:True
# True and False 结果为:False
# False and True 结果为:False
# False and False 结果为:False
# True or True 结果为:True
# True or False 结果为:True
# False and True 结果为:False
# False and False 结果为:False
# ----------------------over------------------
```

## 关系运算符(也称比较运算符)    

	in, not in, is, is not, <, <=, >, >=, !=, ==
	运算符	含义
	<	小于
	<=	小于等于
	>	大于
	>=	大于等于
	==	相等
	!=	不想等
	is	是不是同一个对象
	is not	negated object identity
	in 在
	not in 不在
	x < y < z 想当于 x < y and y < z
	关系运算符的结果有一个真假值。
	>>> 3 < 4
	True
	>>> 3 > 4
	False


## 运算符优先级   
前面学习的算术运算符，逻辑运算符， 关系运算符可以结合起来，组成表达式。    
表达式可以为变量赋值，也可以作为if 语句，while 语句后面的布尔表达式使用，所谓的条件判断。    
下表对 Python 中运算符的优先顺序进行了总结，从最低优先级（最后绑定）到最高优先级（最先绑定）。 相同单元格内的运算符具有相同优先级。 除非句法显式地给出，否则运算符均指二元运算。 相同单元格内的运算符均从左至右分组（除了幂运算是从右至左分组）。
请注意比较、成员检测和标识号检测均为相同优先级，并具有如 比较运算 一节所描述的从左至右串连特性。


| 运算符                                                       | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| :=                                                           | 赋值表达式                                                   |
| [`lambda`](https://docs.python.org/zh-cn/3/reference/expressions.html#lambda) | lambda 表达式                                                |
| [`if`](https://docs.python.org/zh-cn/3/reference/expressions.html#if-expr) -- `else` | 条件表达式                                                   |
| [`or`](https://docs.python.org/zh-cn/3/reference/expressions.html#or) | 布尔逻辑或 OR                                                |
| [`and`](https://docs.python.org/zh-cn/3/reference/expressions.html#and) | 布尔逻辑与 AND                                               |
| [`not`](https://docs.python.org/zh-cn/3/reference/expressions.html#not) `x` | 布尔逻辑非 NOT                                               |
| [`in`](https://docs.python.org/zh-cn/3/reference/expressions.html#in), [`not in`](https://docs.python.org/zh-cn/3/reference/expressions.html#not-in), [`is`](https://docs.python.org/zh-cn/3/reference/expressions.html#is), [`is not`](https://docs.python.org/zh-cn/3/reference/expressions.html#is-not), `<`, `<=`, `>`, `>=`, `!=`, `==` | 比较运算，包括成员检测和标识号检测                           |
| `|`                                                          | 按位或 OR                                                    |
| `^`                                                          | 按位异或 XOR                                                 |
| `&`                                                          | 按位与 AND                                                   |
| `<<`, `>>`                                                   | 移位                                                         |
| `+`, `-`                                                     | 加和减                                                       |
| `*`, `@`, `/`, `//`, `%`                                     | 乘，矩阵乘，除，整除，取余 [5](https://docs.python.org/zh-cn/3/reference/expressions.html#id21) |
| `+x`, `-x`, `~x`                                             | 正，负，按位非 NOT                                           |
| `**`                                                         | 乘方 [6](https://docs.python.org/zh-cn/3/reference/expressions.html#id22) |
| [`await`](https://docs.python.org/zh-cn/3/reference/expressions.html#await) `x` | await 表达式                                                 |
| `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute` | 抽取，切片，调用，属性引用                                   |
| `(expressions...)`,`[expressions...]`, `{key: value...}`, `{expressions...}` | 绑定或加圆括号的表达式，列表显示，字典显示，集合显示         |


请看一面表达式。
1 + 2 * 5 > 3 * (2 + 6) - 1
上面表达式由算术运算符和关系运算符组合起来的，由于算术运算符优先级高于关系运算符，所以表达式    
相当于(1 + 2 * 5) > (3 * (2 + 6) - 1) 先分别计算">"左边和右边，1 + 2 * 5 先计算2 * 5    
1 + 10 再1 + 10 得11, 3 * (2 + 6) - 1 先计算 2 + 6,得 3 ＊ 8 - 1 再 24 － 1 得23，

1 + 2 * 5 > 3 * (2 + 6) - 1 相当于 11 > 23 ,最后整个表达式的值为False。

特别提醒：如果自己写复杂表达式，可以用括号。


#判断结构（也叫选择结构）

人生充满着选择，重要时刻，判断准确，选择着正确的方向，会少走很多弯路。    
很多朋友，学习编程，选择了python，是不是经过比较选择的结果。    

判断结构语法形式：    

	1、if 布尔表达式:
	      语句块
	
	2、if 布尔表达式:
	      语句块
	   else:
	       语句块
	
	3、if 布尔表达式:
	       语句块
	   elif 布尔表达式:
	       语句块
	   elif 布尔表达式:
	       语句块
	   ........
	   else:
	       语句块
	
	4、if嵌套 
	   if 布尔表达式:
	      语句块
	      if 布尔表达式:
	          语句块
	      else:
	          语句块
	   else:
	       语句块

if判断结构，以if 关键字开头，中间空一个空格，再跟上布尔表达式，再跟上冒号(:)    
if之后的布尔表达式俗称条件，如果它为真，如果为真，则执行if语句下面缩进的语句块
（或称为复合语句）。一般语句块以4个空格为习惯的缩进（相当于c语言的{}）。如果
语句块暂时不写语句，可以用pass语句暂占位置，pass语句是啥也不做的意思。

```
salary = 9000
if salary < 10000:
    print("那是因为你还没有学会编程")

# 那是因为你还没有学会编程
```

两路分支判断    

	if 布尔表达式:    
	   语句块    
	else:    
	   语句块    

这个是if 语句后面的条件为真，则执行下面的语句块，否则执行else下面的语句块。
```
salary = 9000
if salary > 10000:
    print("那是因为你还没有学会编程")
else:
    print("需要好好通过学习python学会编程")
#需要好好通过学习python学会编程
```

多路分支判断    

	if 布尔表达式:    
	   语句块    
	elif 布尔表达式:    
	   语句块    
	elif 布尔表达式:   
	   语句块    
	........    
	else:    
	   语句块    

如果if 语句后面条件为假，就不执行if下面的语句块,转到elif 判断，如果有一个elif    
后面的条件为真，则执行下面的语句，执行完，就跳出判断结构，继续下面的语句执行。
如果if elif 语句后面的条件都为假，则执行else 下面的语句块。
```
score = float(input("请输入你的分数:\n"))
if 60 <= score < 70.0:
    print("及格")
elif 70.0 < score <= 80.0:
    print("一般")
elif 80.0 < score <= 90.0:
    print("优秀")
elif score > 90.0:
    print("超级棒")
else:
    print("不及格")

```

代码解释：上图中，第三行代码,input()函数为python内置函数，直接可以调用，
input()函数可以传递一个参数，一般是传递字符串，提示输入信息。input作用是
从输入读一行，并以字符串的形式返回。前面加float(),是将这样的字符串("89.8")
转化为浮点数。4到12行为多路分支判断结构。


if 嵌套    
if 或 if-else 语句中可以是任意语句，当然也可以是if或if-else语句。
如果if 或if-esle 中再包含if 或if-else语句，则称为if 嵌套。

	   if 布尔表达式:
	      语句块
	      if 布尔表达式:
	          语句块
	      else:
	          语句块
	   else:
	       语句块

```
x = 3
y = 5

if x == y:
    print("x 等于 y")
else:
    if x < y:
        print("x 小于 y")
    else:
        print("x 等于 y")


# x 小于 y

```


# 判断结构实例：    
1、判断是不是闰年

	代表年的数字（如2016）能被4整除但不能被100整除，或能被400整除，那么这个年份为闰年。    
	整除的意思是能除尽，没有余数，python中用% 运算符， 2016 % 4 结果为 0。    
	将闰年的定义，翻译为python语言中的逻辑表达式，变量year代表年份。     
	year % 4 == 0 and year % 100 != 0 or year % 400 == 0     
	前面说过，关系运算符优先逻辑运算符，逻辑运算符and优先or,所以可以写成上面的表达式。     
	为了清晰，可以写成(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)     
```
# User enters the year
year = int(input("Enter Year: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


year = int(input("请输入年份:\n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("{0}年是闰年".format(year))
else:
    print("{0}年不是闰年".format(year))

```


# 习题：
特别提示：只有参加[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)  或参加黄哥收费答疑群，才能得到习题和辅导。


如果你感觉黄哥的文章对你有帮助请打赏，支付宝账号：18610508486@163.com

[跟黄哥学习python第六章](learn_python_follow_brother_huang_6.md)


[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)




​    
