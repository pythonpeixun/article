#＊吧上有海外留学生问全部用递归求第N个质数，不能用循环
如果你感觉黄哥的文章对你有帮助请打赏，支付宝账号：18610508486@163.com

## 习题定义了2个函数，还规定了求质数的算法，请看黄哥写的python代码和golang代码。  

[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)



    #coding:utf-8
    import math
    """
    黄哥python北京周末培训班
    https://github.com/pythonpeixun/article/blob/master/beijing_weekend.md
    黄哥python远程视频培训
    https://github.com/pythonpeixun/article/blob/master/index.md
    咨询:qq:1465376564  黄哥python培训

    """
    def check_pr(a, b):
        """传2个参数， a 和 b=sqrt(a),求a是不是质数"""
        if b < 2 and a > 1:
            return True
        elif a % b == 0:
            return False
        else:
            return check_pr(a, b-1)

    def nth_prime(n):
        """用递归替代循环求第n个质数（从2起）。"""
        count = 0
        def helper(i=1):
            nonlocal count
            if check_pr(i, int(math.sqrt(i))):
                count += 1
                if count == n:
                    return i
            return helper(i+1)

        return helper

    if __name__ == '__main__':
        n = 100
        print(nth_prime(n)())

##下面是golang实现  

    package main

    import (
    	"fmt"
    	"math"
    )

    // 求质数的函数
    func isPrime(a int, b float64) bool {
    	if b < 2 && a > 1 {
    		return true
    	} else if a%int(b) == 0 {
    		return false
    	} else {
    		return isPrime(a, b-1)
    	}
    }

    // 求第N个质数
    func nPrime(n int) int {
    	count := 0
    	var helper func(i int) int
    	helper = func(i int) int {
    		if isPrime(i, math.Sqrt(float64(i))) {
    			count += 1
    			if count == n {
    				return i
    			}

    		}
    		return helper(i + 1)

    	}
    	return helper(1)
    }

    func main() {
    	n := 100
    	fmt.Println(nPrime(n))

    }
