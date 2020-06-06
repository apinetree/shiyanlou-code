#!/usr/bin/env python3


import os
import sys


def find_num(path):
	"""
	函数找到文件中的所有数字，返回一个列表

	:argv path：文件的路径

	:return：返回数字的列表
	"""
	l = []
	
	f = open(path)
	s = f.read()
	f.close()
	for i in s:
		if i.isdigit():
			l.append(i)
		else:
			continue
	return l


def main(path):
	"""
	函数用于打印文件分析结果

	:arg path：要分析的文本文件的路径

	:return：纯数字的字符串
    """
	if os.path.exists(path):
		l = find_num(path)
		s_new = ''.join(l)
		print(s_new)
		return True
	else:
		print("文件不存在")
		return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
    	main(sys.argv[1])
    else:
    	sys.exit(-1)
    sys.exit(0)