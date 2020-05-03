#!/usr/bin/env python3
n, k = map(int,input().split())
list_people = list(range(1,n+1))
for i in range(k):
    d = int(input())
    list_get = list(input().split())
    for j in range(d):
        if int(list_get[j]) in list_people:
            list_people.remove(int(list_get[j]))
print(len(list_people))