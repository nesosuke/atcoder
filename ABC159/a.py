#!/usr/bin/python3
n,m=map(int,input().split())
# even+even or odd+odd 
nC2 = n* (n-1) /2 
mC2 = m* (m-1) /2 
Ans = nC2 + mC2 
print(int(Ans))