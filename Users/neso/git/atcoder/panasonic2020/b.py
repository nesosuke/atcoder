#!/usr/bin/python3
Height, Width = map(int,input().split())
masu = Height * Width 
if masu % 2 == 0:
    print(masu // 2)
else:
    print(masu // 2 + 1)