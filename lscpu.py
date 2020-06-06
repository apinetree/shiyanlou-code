#!/usr/bin/env python3
file = "/proc/cpuinfo"
with open(file) as f:
	for line in f:
		print(line, end=' ')