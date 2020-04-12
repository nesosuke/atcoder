#!/usr/bin/python3
N = int(input())
wa = 0
for i in range(1,N+1):
    if i % 3 != 0 and i % 5 != 0 and i % 15 != 0:
        wa += i
print(wa)