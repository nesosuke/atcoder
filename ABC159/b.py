#!/usr/bin/python3
String = str(input())
Mid = len(String) // 2 
StrFormer = String[0:Mid]
StrFormer_inv = StrFormer[::-1]
StrLater = String[:Mid:-1]
StrLater_inv = StrLater[::-1]
if StrFormer == StrFormer_inv and StrLater == StrLater_inv:
    if StrFormer == StrLater:
        print("Yes")
    else:
        print("No")
else:
    print("No")