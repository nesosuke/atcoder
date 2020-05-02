#!/usr/bin/env python3
x = int(input())
wallet = 100
year = 0
while wallet < x:
    wallet = int(wallet * 1.01)
    year += 1
print(year)