#!/usr/bin/env python3
n, m = map(int,input().split())
h = list(input().split())
h_comp = h
## path
for i in range(m):
    a,b = map(int,input().split())
    if h[a-1] <= h[b-1]:
            h_comp[a-1] = "Bad"
    elif h[b-1] >= h[a-1]:
            h_comp[b-1] = "Bad"

count = 0
for i in range(n):
    if h_comp[i] != "Bad":
        count += 1

#print(h_comp)
print(count)