#!/usr/bin/python3
n, x = map(int, input().split())
total = 0
yotta = -1
for i in range(n):
    v, p = map(int, input().split())
    total += v*p/100
    print(total)
    if yotta == -1 and total > x:
        yotta = i+1
print(yotta)
