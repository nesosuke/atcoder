#!/usr/bin/python3
a, b, c = map(int, input().split())
if a+b <c and (a*b)*4 < ((c-a-b))**2:
    print("Yes")
else:
    print("No")
