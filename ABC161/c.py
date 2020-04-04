#!/usr/bin/python3 
n,k = map(int,input().split())
n = abs(n-k) % k
if 2*n > k:
    n = abs(n-k)
print(n)