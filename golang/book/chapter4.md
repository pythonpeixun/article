# 第四章 函数

## 函数的概念引入

假设要设计一段代码，分别对1 到100，100 到200 分别求和，按照前面学的知识，用累加算法。代码如下：

```go
package main

import "fmt"

func main(){
	sum1 := 0
	for i := 1; i <=100;i++ {
		sum1 += i
	}
	fmt.Printf("sum1 = %d\n", sum1)

	sum2 := 0
	for i := 100; i <=200;i++ {
		sum2 += i
	}
	fmt.Printf("sum2 = %d\n", sum2)
}

```

有没有发现上面的代码，for 循环中除了i的开始值和结束值不同，其它代码相似。这样可以抽取共同的代码，封装成一个整体，编程语言用函数来表示，以达到代码重用的目的。

```go
package main

import "fmt"

func main(){
	fmt.Printf("sum1 = %d\n", sumOfNumber(1, 100))
	fmt.Printf("sum2 = %d\n", sumOfNumber(100, 200))
}


func sumOfNumber(begin, end int) int {
	var res int
	for i := begin; i <= end; i++ {
		res += i
	}
	return res
}
```

## 函数定义

在编程中，函数是指用于进行特定计算的一序列语言的有名称的组合，定义一个函数时，需要指定函数的名称（匿名函数除外）并写下一序列语句，之后可以用这个名称来调用这个函数。

初学编程时，要养成习惯将一个大的问题分解为多个小的问题，每一个小的问题用函数来封装。函数就像一个黑箱子一样，设计者对使用者隐藏了实现细节。

