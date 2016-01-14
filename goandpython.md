
#python 与go语言一行一行读文本文件的比较。  

python 更抽象，只要几行代码就可以完成。  
go语言处理这个问题代码量稍微多一点，但也很方便。

下面是python 一行一行读文本文件代码  
	#coding:utf-8


	with open("words.txt") as f:
		for line in f:
			print line


下面是go语言 一行一行读文本文件代码  

	package main

	import (
	  "fmt"
	  "os"
	  "bufio"
	  "strings"
	)

	func main() {
	  file, err := os.Open("words.txt")
	  if err != nil{
	    fmt.Println(nil)
	    os.Exit(1)
	  }
	  defer file.Close()
	  scanner := bufio.NewScanner(file)
	  for scanner.Scan(){
	    fmt.Println(strings.TrimSpace(scanner.Text()))
	  }

	}

[黄哥python远程视频培训班] (https://github.com/pythonpeixun/article/blob/master/index.md)
