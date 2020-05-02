#!/usr/bin/env python3
n, m, q = map(int,input().split())
list_a = []
score = 0
for i in range(q):
    list_a.append(list(input().split()))
    if (n - int(list_a[i][0])) == int(list_a[i][2]) and (m - int(list_a[i][1])) == int(list_a[i][2]):
        score += int(list_a[i][3])
print(score)   