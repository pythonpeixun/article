#python迭代器的设计

如果你感觉黄哥的文章对你有帮助请打赏，支付宝账号：18610508486@163.com

##跟黄哥学python编程系列文章之迭代器

###如何自定义迭代器，有2个必要条件

1、自定义类有一个方法\_\_iter\_\_返回实例对象自己，_\_iter\_\_ 一般只需要return self 既可。

2、有next()方法，python3 是\_\_next\__()方法。

###python 3代码实例

```
class Reverse:
    """反转的迭代器
    参加黄哥python远程视频培训,帮你完成从不会写代码到会写代码解决问题的过渡。
    python远程视频培训
    https://github.com/pythonpeixun/article/blob/master/index.md
    python北京周末培训班
    https://github.com/pythonpeixun/article/blob/master/beijing_weekend.md
    咨询:qq:1465376564  企业内训，个人培训，请咨询黄哥电话:18610508486 
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

foo = Reverse(range(10))
print(foo)
#<__main__.Reverse object at 0x101207400>

for i in foo:
    print(i, end=",")

#输出结果9,8,7,6,5,4,3,2,1,0,

```