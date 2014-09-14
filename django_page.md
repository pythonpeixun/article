#django通过二种方式取得分页的page值

###第一：通过正则表达式的分组和视图结合取得url中的参数。  
urls.py中这样写  

     url(r'^page=(\d+)', 'blogapp.views.index')
    
views.py中这样写函数。  
    
     def index(request,page):  ＃是2个参数
           try:
               number = int(page)
           except :
                page = 1    
url 的样式 http://127.0.0.1:8000/page=2
  
###第二：通过request的方法  
    def index(request):  ＃是一个参数
        try:
             page = int(request.GET.get('page'))
        except ValueError:
             page = 1
这样，urls.py中,正则不用特殊设置。url 的样式 http://127.0.0.1:8000/?page=1


[python培训黄哥所写，50讲视频＋作业＋辅导](https://github.com/pythonpeixun/article/blob/master/index.md)，让参加的学员，可以通过学习python学会编程。


     


