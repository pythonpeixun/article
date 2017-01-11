
default: base pygmentize misc html5
	echo "Done!" > "测 试".count.md
	#make clean

base:
	# 基本测试
	touch "测 试".md; sleep 1;
	echo "你 好" >> "测 试".md; sleep 1
	touch "测 试".rst; sleep 1;
	echo "你 好" >> "测 试".rst; sleep 1

	touch "测 试".org; sleep 1;
	echo "* 你好" >> "测 试".org; sleep 1

	touch "测 试".t2t; sleep 1;
	echo "你好" >> "测 试".t2t; sleep 1

	touch "测 试".textile; sleep 1;
	echo "\n你好" >> "测 试".textile; sleep 1

	touch "测 试".html; sleep 1;
	echo 你好 >> "测 试".html; sleep 1

html5:
	# coffee
	touch "测 试".coffee; sleep 1;
	echo "require 'fs'" > "测 试".coffee; sleep 1
	# jade
	touch "测 试".jade; sleep 1
	echo "doctype html" > "测 试".jade; sleep 1
	echo "h1 成功" >> "测 试".jade; sleep 1

pygmentize:
	# pygmentize测试
	echo "import sys\nprint \"你好\"" > "测 试".py
	echo "#include <stdio.h>\nint main() {\npirntf(\"你好\\\\n\");\nreturn 0;\n}" > "测 试".c
	echo "var x='marboo';" > "测 试".js
	echo "f(1) -> 1;\nf(N)->N*f(N-1).\n" > "测 试".erl

misc:
	# 其他类型测试
	touch CNAME; sleep 1; echo marboo.io > CNAME; sleep 1
	touch domains.config; sleep 1; echo amoblin.marboo.io > domains.config

jekyll:
	# DO NOT support yet.
	#jekyll . /tmp/marboo.io

clean:
	rm -f "测 试".*
	rm -f 测试.*
	rm -f CNAME domains.config
