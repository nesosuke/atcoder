#!/usr/bin/python3
a, b, c = map(float, input().split())
if (a*b)*4 < ((c-a-b))**2:
    print("Yes")
else:
    print("No")
