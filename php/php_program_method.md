#php编程思路之一

黄哥从2012年底从事python培训以来得到很多朋友的支持和认可。

2016年陆续推出php和golang培训视频。

##有一个这样的问题

有一个数组，$arr = array("A", "B", "C", "D");

请根据n循环输出下面的样式：假定n = 15

A

B

C

D

A

B

C

D

A

B

C

D

A

B

C

也就是说循环输出，每次输出C后，又从头A开始输出。

相信大家计数循环大家都能看得懂，但用计算循环来解决这样的问题，初学者会感觉无从下手。

##以下代码以命令行的方式运行：php begintoend.php

##代码1，用循环





    <?php
        function echoBeginToend($arr, $n){
          $i = 1;
          $j = 0;
          while ($i < ($n + 1)){
            echo $arr[$j];
            echo "\n";
            $j += 1;
            if ($i % 4 == 0){
              $j = 0;
            }
            $i += 1;
    
          }
    
        }
    
        print("请输入: n\n");
        $n = trim(fgets(STDIN));
        $arr = array("A", "B", "C", "D");
        echoBeginToend($arr, $n);
##代码2  用php spl标准库中的队列





    <?php
    
        function echoBeginToend($q, $n){
          for ($i=1; $i<=$n; $i++){
            $tmp = $q->dequeue();
            echo $tmp;
            echo "\n";
            $q->push($tmp);
        }
        }
        print("请输入: n\n");
        $n = trim(fgets(STDIN));
        $q = new SplQueue();
        $q->push('A');
        $q[] = 'B';
        $q[] = 'C';
        $q[] = 'D';
        echoBeginToend($q, $n);
[黄哥php培训](https://github.com/pythonpeixun/article/blob/master/php_education.md)