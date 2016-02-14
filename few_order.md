#*推荐几个好使的Linux命令*
##1.  下载网页版本电子书的好方法：  
wget镜像html版的电子书  
wget --mirror  -p --convert-links -p . http://interactivepython.org/courselib/static/pythonds/index.html


##2.  curl代理下载文件  
curl -x  proxy -o 文件名 下载地址

##3.  后台运行python代码  
有这样的需求，当ssh 登录到局域网用python *.py 运行python代码，等ssh断开后，运行的python程序也会退出。  
可以这样做，ssh断开后，运行的进程还不退出。  
#nohup python *.py &      
这样做，还可以将出错信息保存到一个文本文件中。
