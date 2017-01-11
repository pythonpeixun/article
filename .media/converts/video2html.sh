#!/bin/sh
# author: amoblin <amoblin@gmail.com>
# file name: video2html.sh
# create date: 2014-07-06 06:37:27
# This file is created from $MARBOO_HOME/media/starts/default.sh
# 本文件由 $MARBOO_HOME/media/starts/default.sh　复制而来

name=`basename "$1"`
name_without_extension=`echo ${name%.*}`
#tmp_file=/tmp/$name
echo "<div style=\"text-align:center\">\n \
<h1>$name_without_extension</h1>\n \
<div class=\"player\" style=\"margin-top:100px\">\n\
  <video controls=\"\" name=\"media\" width=\"80%\">\n \
    <source src=\"$name\" type=\"video/mp4\">\n \
  </video>\n \
</div>"
