#!/usr/bin/python3
a, b, c = map(float, input().split())
if (a*b) < ((c-a-b)/2)**2:
    print("Yes")
else:
    print("No")
