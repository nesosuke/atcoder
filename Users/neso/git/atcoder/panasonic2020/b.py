#!/usr/bin/python3
Height, Width = map(int,input().split())
masu = Height * Width 
if Height == 1 or Width == 1:
    print(1)
elif masu % 2 == 0:
    print(masu // 2)
else:
    print(masu // 2 + 1)