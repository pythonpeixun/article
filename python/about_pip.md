# 黄哥小议Python pip 包管理工具

Python 的pip 包管理工具太好用了
Python 2.7.9 以上默认都自动安装了这个pip工具，
在windows cmd或Linux等终端下  
输入pip，如果显示没有此命令，
可能是没有安装好或路径（windows环境变量）没有设置好。
有的centos，ubuntu自带Python，pip没有安装。可以这样安装一下。
下载get-pip.py https://bootstrap.pypa.io/get-pip.py ，
再切换到get-pip.py 文件所在的目录 
输入 python get-pip.py，再配置好路径，即可使用。
Pip 常见命令

Usage:  pip <command> [options]
Commands:
install                     Install packages.
download                    Download packages.
uninstall                   Uninstall packages.
freeze                      Output installed packages in requirements format.
list                        List installed packages.
show                        Show information about installed packages.
search                      Search PyPI for packages.
wheel                       Build wheels from your requirements.
hash                        Compute hashes of package archives.
completion                  A helper command used for command completion
help                        Show help for commands

1、 常用的是pip install 库。

例： 
pip install django  
Linux 用户权限不够的时候，需要用sudo pip install django

2、当你开发project时

有很多依赖包，当你的代码放到公司git代码仓库前，最好执行一下
pip freeze >requirements.txt  
这样将你的依赖包都放到requirements.txt 文件中了。
团队同事，需要用到你的代码时，
pip install -r requirements.txt，
即可安装项目的依赖包。
3、pip 可以选择安装不同的版本

先安装一个第三方库

$ pip install yolk
$ yolk -V django
Django 1.10rc1
Django 1.10b1
Django 1.10a1
Django 1.9.8
Django 1.9.7
Django 1.9.6
Django 1.9.5
Django 1.9.4
Django 1.9.3
Django 1.9.2
Django 1.9.1
Django 1.9
Django 1.9rc2
Django 1.9rc1
Django 1.9b1
Django 1.9a1
Django 1.8.14
Django 1.8.13
Django 1.8.12
Django 1.8.11
Django 1.8.10
Django 1.8.9
Django 1.8.8
Django 1.8.7
Django 1.8.6
Django 1.8.5
Django 1.8.4
Django 1.8.3
Django 1.8.2
Django 1.8.1
Django 1.8
Django 1.8c1
Django 1.8b2
Django 1.8b1
Django 1.8a1
Django 1.7.11
Django 1.7.10
Django 1.7.9
Django 1.7.8
Django 1.7.7
Django 1.7.6
Django 1.7.5
Django 1.7.4
Django 1.7.3
Django 1.7.2
Django 1.7.1
Django 1.7
Django 1.6.11
Django 1.6.10
Django 1.6.9
Django 1.6.8
Django 1.6.7
Django 1.6.6
Django 1.6.5
Django 1.6.4
Django 1.6.3
Django 1.6.2
Django 1.6.1
Django 1.6
Django 1.5.12
Django 1.5.11
Django 1.5.10
Django 1.5.9
Django 1.5.8
Django 1.5.7
Django 1.5.6
Django 1.5.5
Django 1.5.4
Django 1.5.3
Django 1.5.2
Django 1.5.1
Django 1.5
Django 1.4.22
Django 1.4.21
Django 1.4.20
Django 1.4.19
Django 1.4.18
Django 1.4.17
Django 1.4.16
Django 1.4.15
Django 1.4.14
Django 1.4.13
Django 1.4.12
Django 1.4.11
Django 1.4.10
Django 1.4.9
Django 1.4.8
Django 1.4.7
Django 1.4.6
Django 1.4.5
Django 1.4.4
Django 1.4.3
Django 1.3.7
Django 1.3.6
Django 1.3.5
Django 1.2.7
Django 1.1.4
Django 1.0.4

这样pip install Django==1.9.8 你想安装哪个版本就安装哪个版本。

[216小时学会Python](https://github.com/pythonpeixun/article/blob/master/python/hours_216.md)

[感恩！感谢黄哥Python培训学员的支持和肯定。](https://github.com/pythonpeixun/article/blob/master/python/thanks.md)
