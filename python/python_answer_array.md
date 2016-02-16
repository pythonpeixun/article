#用python写一个程序，找出数组中差值为K的数共有几对
##知乎上有人问“用python写一个程序，找出数组中差值为K的数共有几对”

[点击黄哥python培训试看视频播放地址](https://github.com/pythonpeixun/article/blob/master/python_shiping.md)

[黄哥python远程视频培训班](https://github.com/pythonpeixun/article/blob/master/index.md)



    #coding:utf-8
    """

    用python写一个程序，找出数组中差值为K的数共有几对



    示例：

    差值k=4 and 数组是[7, 6, 23,19,10,11, 9, 3, 15]

    这样的结果是(7,11) (7,3) (6,10) (19,23) (15,19) (15,11) 共6对



    从标准输入读入两行数据

    5 2

    1 5 3 4 2



    第一行代表N和K, N是数组是一共有多少数字，K是所要求的差值

    第二是数组，空白分格



    输出到标准输出





    Sample Input #00:

    5 2

    1 5 3 4 2

    Sample Output #00:

    3

    Sample Input #01:

    10 1

    363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793

    Sample Output #01:

    0

    """



    def diff_of_element_list(lst, k):

            """黄哥python远程视频培训班

            https://github.com/pythonpeixun/article/blob/master/index.md



            黄哥python培训试看视频播放地址

            https://github.com/pythonpeixun/article/blob/master/python_shiping.md

            """

            newlst = [i + k for i in lst]

            return len(set(lst) & set(newlst))



    if __name__ == '__main__':

            lst = [7, 6, 23,19,10,11, 9, 3, 15]

            k = 4

            print(diff_of_element_list(lst, k))

            lst = [1,5, 3, 4, 2]

            k = 2

            print(diff_of_element_list(lst, k))



            n, k = input("please input n and k:\n").split()

            lst = input("plesae input {0} number:\n".format(n)).split()

            lst = [int(i) for i in lst]

            print(diff_of_element_list(lst, int(k)))
