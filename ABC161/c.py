#!/usr/bin/python3 
n,k = map(int,input().split())
if abs(n-k) <= n:
    n = abs(n-k)
    
else:
    n = abs(n-k) % k
print(n)