#!/usr/bin/python3
N = list(input())
for i in range(len(N)):
    if N[i] == '7':
        print("Yes")
        exit()
print("No")