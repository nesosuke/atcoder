#!/usr/bin/python3
import math

n = int(input())
res = []
limit = int(math.sqrt(n))+1
for i in range(2, limit+1):
    j = 2
    while i**j <= n:
        res.append(i**j)
        j += 1
print(n - len(set(res)))
