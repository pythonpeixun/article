# Python 面试题：相同字母异序词

Anagram，翻译成中文为"相同字母异序词"。
写函数判断二个字符串是不是"相同字母异序词"，意思是说，所有字母相同，但前后顺序不一样。


		#! /usr/bin/python
		# coding:Utf-8


		def is_Anagram(s1, s2):
		    """黄哥python黄哥所写"""
		    s1, s2 = s1.lower(), s2.lower()
		    lsts1 = list(s1)
		    lsts2 = list(s2)
		    lsts1.sort()
		    lsts2.sort()
		    for i, char in enumerate(lsts1):
		        if lsts2[i] != char:
		            return False
		    return True


		def is_Anagram_another(s1, s2):
		    """黄哥python黄哥所写"""
		    s1, s2 = s1.lower(), s2.lower()
		    lst1 = [0] * 26
		    lst2 = [0] * 26
		    length1, length2 = len(s1), len(s2)
		    for i in range(length1):
		        pos = ord(s1[i]) - ord('a')
		        lst1[pos] += 1

		    for i in range(length2):
		        pos = ord(s2[i]) - ord('a')
		        lst2[pos] += 1

		    for i in range(26):
		        if lst1[i] != lst2[i]:
		            return False
		    return True


		print is_Anagram("Abbc", "cbaba")
		print is_Anagram_another("Abbc", "cbaba")
		print is_Anagram("JKwwi", "wkjwi")
		print is_Anagram_another("JKwwi", "wkjwi")



[216小时学会Python](https://github.com/pythonpeixun/article/blob/master/python/hours_216.mdown)
[感恩！感谢黄哥Python培训学员的支持和肯定。](https://github.com/pythonpeixun/article/blob/master/python/thanks.md)

