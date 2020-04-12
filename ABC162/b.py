#!/usr/bin/python3
N = int(input())
wa = 0
for i in range(N):
    if i % 3 != 0 and i % 5 != 0:
        wa += i
print(wa)