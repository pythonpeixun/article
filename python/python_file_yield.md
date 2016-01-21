#python生成器处理文本文件大幅度提高效率

运维需要处理日志文件，感觉对自己写的代码处理速度不是很满意。  

黄哥建议试试生成器，可以大幅度提高效率。  

请看代码  


    #coding:utf-8
    """
    python远程视频培训
    https://github.com/pythonpeixun/article/blob/master/index.md
    c语言从入门到精通远程视频培训
    https://github.com/pythonpeixun/article/blob/master/c_course.md
    咨询:qq:1465376564  黄哥python培训
    """
    import time

    start_time = time.time()


    def find_ip(path):
        for line in open(path):
            s = line.find('"Sogou web spider')
            if s >= 0:
                yield line[:s].strip()

    p = find_ip("bigfile.txt")
    p = list(set(list(p)))

    for item in p:
        print item

    print time.time() - start_time, "seconds"


[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)
