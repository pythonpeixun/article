#!/bin/sh
# author: amoblin <amoblin@gmail.com>
# file name: zip-list.sh
# create date: 2013-03-01 11:27:53
# This file is created from $MARBOO_HOME/media/starts/default.sh
# 本文件由 $MARBOO_HOME/media/starts/default.sh　复制而来

name=`basename "$1"`
echo "# ${name}"
unzip -l "$1"|sed 's/^/    /'
