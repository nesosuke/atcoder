#!/usr/bin/python3
import math
K = int(input())
sum_gcd = 0
gcd = 0

primelist = []	
for i in range(1, K+1):	
    for j in range(2, int(math.sqrt(K)) + 1):	
        if i % j == 0:	
            primelist.append(i)

for a in range(K,0,-1):
    for b in range(K,0,-1):
        for c in range(K,0,-1):
            i = max(a,b,c)
            while i >= min(a,b,c):
                if a in primelist or b in primelist or c in primelist:
                    if a == b and b ==c:
                        gcd = a
                elif a % i == 0 and b % i == 0 and c % i == 0:
                   gcd = i  
                   break
                i -= 1
            sum_gcd += gcd
print(sum_gcd)