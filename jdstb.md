 剪刀石头布小习题三种语言python2、php、go代码
 学习编程不只是学习语法、学习计算思维、编程思路才是重点。
 参加黄哥python培训班、教会从只能看懂玩具代码过度到自己能写代码解决问题。
 [python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)


	# coding:utf-8
	"""
	python核心编程6-14习题的解题思路
	设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,下面是规则.
	你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从
	下面的规则中产生,这个规则本身是个悖论.
	(a) 布包石头.
	(b)石头砸剪子,
	(c)剪子剪破布.在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,然后由你
	的程序来决定一个胜利者或者平手.注意:最好的算法是尽量少的使用 if 语句.
	python培训 黄哥所写 python2
	"""

	import random
	guess_list = ["石头", "剪刀", "布"]
	win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]
	while True:
	    computer = random.choice(guess_list)
	    people = raw_input('请输入：石头,剪刀,布\n').strip()
	    if people not in guess_list:
	        people = raw_input('重新请输入：石头,剪刀,布\n').strip()
	        continue
	    if computer == people:
	        print "平手，再玩一次！"
	    elif [computer, people] in win_combination:
	        print "电脑获胜！"
	    else:
	        print "人获胜！"
	        break

上面的代码有一个小bug，感谢北交大校友发现的问题，黄哥修改如下（2016年8月5号上午）。

  # coding:utf-8

  import random
  guess_list = ["石头", "剪刀", "布"]
  win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]

  while True:
      computer = random.choice(guess_list)
      people = raw_input('请输入：石头,剪刀,布\n').strip()
      if people not in guess_list:
          continue
      elif computer == people:
          print "平手，再玩一次！"
      elif [computer, people] in win_combination:
          print "电脑获胜，再玩，人获胜才能退出！"
      else:
          print "人获胜！"
          break

##php语言实现

	<?php
	/*
	本代码由python视频培训班黄哥所写。
	python核心编程6-14习题,用php写一遍。
	在linux下终端运行 php test.php
	本代码在mac下测试运行无误。
	总计：这个代码是根据本人所写python代码修改过来的
	学会一种编程语言，再学第二种，就很容易，为啥？
	编程思路是一样的。
	*/
	$my_array = array("石头","剪刀","布");
	$guize = array(array("石头","剪刀"),array("剪刀","布"),array("布","石头"));
	//上面2个变量定义一个需要输入的数组，和一个获胜规则的二维数组
	// var_dump($guize);
	$rand_keys = array_rand($my_array);
	$computer = $my_array[$rand_keys];
	//取数组中随机值

	echo $computer . "\n";




	// echo $person;
	while (True)
	{
	    echo "请输入: 石头  剪刀  布\n";
	    $person = trim(fgets(STDIN)) ;
	    $input = array($computer,$person);
	    //将输入的$person和电脑随机产生的值构造一个数组
	    //再判断在不在获胜规则数组中

	    if (!(in_array($person,$my_array)))
	    {
	       echo "只能输入'剪刀、石头，布，请重新输入'";
	       continue;

	    }


	    if ($computer == $person )
	    {
	        echo "平手\n";

	    }
	    else if (in_array($input,$guize)) {
	        echo "电脑胜\n";

	    }
	    else
	    {
	      echo "人获胜\n";
	      break;
	    }
	}
	?>


##go语言实现

	package main

	// 将python习题剪刀石头布修改为go语言的代码
	// 黄哥写于2014年3月19日北京

	import (
	    "fmt"
	    "math/rand"
	)

	// 下面这个函数判断一个一维slice在不在二维slice中，相当于python中in功能
	func exist_in(str1 [][]string, str2 []string) int {
	    for _, item := range str1 {
	        if item[0] == str2[0] && item[1] == str2[1] {
	            return 1
	        }
	    }
	    return 0

	}
	func main() {
	    var person string
	    guess_list := []string{"石头", "剪刀", "布"}
	    Win := [][]string{{"布", "石头"}, {"石头", "剪刀"}, {"剪刀", "布"}}

	    for {
	        num := rand.Intn(len(guess_list))
	        computer := guess_list[num]
	        fmt.Println(computer)
	        fmt.Println("请输入'石头,剪刀,布'")
	        fmt.Scanf("%s\n", &person)
	        input := []string{computer, person} //构造一个一维slice
	        if computer == person {
	            fmt.Println("平手！")

	        } else if exist_in(Win, input) > 0 {
	            fmt.Println("电脑获胜")

	        } else {
	            fmt.Println("人获胜")
	            break
	        }
	    }

	}
