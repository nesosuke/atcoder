#!/usr/bin/python3
n = int(input())
minprice = 10**10
for i in range(n):
    a, p, x = map(int, input().split())
    if a+0.5 < x and p < minprice:
        minprice = p
if minprice == 10**10:
    print('-1')
else:
    print(minprice)
