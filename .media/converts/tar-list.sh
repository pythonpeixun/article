#!/bin/sh
# author: amoblin <amoblin@gmail.com>
# file name: tar-list.sh
# create date: 2013-03-07 15:13:36
# This file is created from $MARBOO_HOME/media/starts/default.sh
# 本文件由 $MARBOO_HOME/media/starts/default.sh　复制而来

name=`basename "$1"`
echo "# ${name}"
tar tvf "$1"|sed 's/^/    /'
