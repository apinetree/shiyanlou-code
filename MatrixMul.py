#!/usr/bin/env python3
"""
两个矩阵相乘
"""
n = int(input("输入矩阵大小n："))

print("输入矩阵A的值：")
a = []
for i in range(n):
	a.append([int(x) for x in input().split()])

print("输入矩阵B的值：")
b = []
for i in range(n):
	b.append([int(x) for x in input().split()])

c = []
for i in range(n):
	c.append([a[i][j] * b[i][j] for j in range(n)])

print("A * B的值为：")
print('-' * 7 * n)
for x in c:
	for y in x:
		print(str(y).rjust(5), end=' ')
	print()
print('-' * 7 * n)