#跟黄哥学编程系列文章之插入排序

## 插入排序算法描述

**插入排序（Insertion Sort）**是一种简单直观的[排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。**插入排序**在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

##算法描述

一般来说，**插入排序**都采用in-place在数组上实现。具体算法描述如下：

1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5

## 下面是黄哥写的python代码和golang代码

###python 插入排序

    #coding:utf-8
        """
        如何通过学习python学会编程
        https://github.com/pythonpeixun/article/blob/master/python/how_to_learn_python.md
        黄哥python远程视频培训班
        https://github.com/pythonpeixun/article/blob/master/index.md
        黄哥python培训试看视频播放地址
        https://github.com/pythonpeixun/article/blob/master/python_shiping.md
        帮你完成从不会写代码到会写代码解决问题的过渡。
        咨询qq:1465376564
        """

        def insert_sort(lst):
            length = len(lst)
            for i in range(1, length):
                tmp = lst[i]
                for j in range(i-1, -1, -1):
                    if lst[j] > tmp:
                        lst[j+1] = lst[j]
                    else:
                        lst[j+1] = tmp
                        break
                if lst[0] > tmp:
                    lst[0] = tmp

        if __name__ == '__main__':
            lst = [8, 2, 4, 1, 9, 20, 15, 6, 0]
            insert_sort(lst)
            print(lst)


###golang插入排序代码    

    package main

        import (
        	"fmt"
        )

        func InsertSort(lst []int) {

        	length := len(lst)
        	for i := 1; i < length; i++ {
        		tmp := lst[i]
        		for j := i - 1; j >= 0; j-- {
        			if lst[j] > tmp {
        				lst[j+1] = lst[j]
        			} else {
        				lst[j+1] = tmp
        				break
        			}

        		}
        		// 这个地方有点小技巧，因为golang 中j是for循环作用域，所以
        		// 直接判断第一个元素
        		if lst[0] > tmp {
        			lst[0] = tmp
        		}

        	}
        }
        func main() {

        	lst := []int{3, 8, 2, 9, 7, 12, 33, 6, 97, 48, 23}
        	InsertSort(lst)
        	fmt.Println(lst)
        }

##c语言代码  
  void insertion_sort(int arr[], int len) {
  	int i, j;
  	int temp;
  	for (i = 1; i < len; i++) {
  		temp = arr[i]; //與已排序的數逐一比較，大於temp時，該數向後移
  		for (j = i - 1; j >= 0 && arr[j] > temp; j--) //j循环到-1时，由于[[短路求值]](http://zh.wikipedia.org/wiki/短路求值)，不会运算array[-1]
  			arr[j + 1] = arr[j];
  		arr[j+1] = temp; //被排序数放到正确的位置
  	}
  }

##python 其它的2个版本    

    def insertion_sort(n):
        if len(n) == 1:
            return n
        b = insertion_sort(n[1:])
        m = len(b)
        for i in range(m):
            if n[0] <= b[i]:
                return b[:i]+[n[0]]+b[i:]
        return b + [n[0]]

    def insertion_sort(lst):
        if len(lst) == 1:
            return

        for i in xrange(1, len(lst)):
            temp = lst[i]
            j = i - 1
            while j >= 0 and temp < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = temp
##算法复杂度

如果目标是把n个元素的序列升序排列，那么采用**插入排序**存在最好情况和最坏情况。最好情况就是，序列已经是升序排列了，在这种情况下，需要进行的比较操作需*(n-1)*次即可。最坏情况就是，序列是降序排列，那么此时需要进行的比较共有*n(n-1)/2*次。**插入排序**的赋值操作是比较操作的次数减去*(n-1)*次。平均来说**插入排序**算法复杂度为**O(n2)**。因而，**插入排序**不适合对于数据量比较大的排序应用。但是，如果需要排序的数据量很小，例如，量级小于千，那么**插入排序**还是一个不错的选择。 插入排序在工业级库中也有着广泛的应用，在STL的sort算法和stdlib的qsort算法中，都将插入排序作为快速排序的补充，用于少量元素的排序（通常为8个或以下）。

[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)

注：文字资源来源于维基百科
