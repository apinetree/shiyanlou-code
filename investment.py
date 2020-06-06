#!/usr/bin/env python3
"""
计算利率
"""
a = float(input("amount:"))
i = float(input("rate:"))
p = int(input("period:"))
value = 0
year = 1
while year <= p:
    value = a + (i * a)
    print("Year {} Rs. {:.2f}".format(year, value))
    a = value
    year += 1
