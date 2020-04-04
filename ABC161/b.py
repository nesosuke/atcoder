#!/usr/bin/python3
n,m = map(int,input().split())
List_a = list(map(int,input().split()))
List_a.sort(reverse=True)
Condition = sum(List_a) / (4*m)
for i in range(m):
    if List_a[i] < Condition:
        print("No")
        exit()
print("Yes")
