#!/usr/bin/env python3
"""
拷贝给定的文本文件到另一个给定的文本文件
"""
import sys
if len(sys.argv) < 3:
	print("错误的参数")
	print("./CopyFlie.py 文件1 文件2")
	sys.exit(1)
f1 = open(sys.argv[1])
s = f1.read()
f1.close()

f2 = open(sys.argv[2], 'w')
f2.write(s)
f2.close()