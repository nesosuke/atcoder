#!/usr/bin/python3
# わ～～～～～からんですわ～～～～～～～
from collections import Counter
N = int(input())
A = list(input().split())
for k in range(N):
    ans = 0
    A_copy=sorted(A)
    A_copy.remove(A[k])
    c = Counter(A_copy) #dict
    for l in c.keys():
       ans+= ( c[l] * (c[l]-1) ) / 2 
    print(int(ans))