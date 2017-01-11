#!/bin/sh
# author: amoblin <amoblin@gmail.com>
# file name: flash2html.sh
# description: TODO
# create date: 2015-02-18 13:55:37
# This file is created from $MARBOO_HOME/.media/starts/default.sh
# 本文件由 $MARBOO_HOME/.media/starts/default.sh　复制而来

name=`basename "$1"`
name_without_extension=`echo ${name%.*}`
#tmp_file=/tmp/$name
echo "<div style=\"text-align:center\">\n \
<h1>$name_without_extension</h1>\n \
<div style=\"margin-top:100px\">\n \
   <embed height=\"500px\" pluginspage=\"http://www.macromedia.com/go/getflashplayer\" quality=\"high\" src=\"$name\" title=\"\" type=\"application/x-shockwave-flash\" width=\"700px\" />\n \
</div>\n \
</div>\n"
