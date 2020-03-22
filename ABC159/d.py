#!/usr/bin/python3
N = int(input())
A = list(input().split())
for i in range(N):
    print(i)
    print(A[0:i])
    print(A[i+1::])