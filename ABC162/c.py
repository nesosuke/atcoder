#!/usr/bin/python3
import math
K = int(input())
gcd = 0
sum_gcd = 0
for a in range(1,K+1):
    for b in range(1,a+1):
        for c in range(1,b+1):
            i = 1
            while i <= min(a,b,c):
                if a % i == 0 and b % i == 0 and c % i == 0:
                   gcd = i  
                i += 1
            
            if a == b and b == c :
                sum_gcd += gcd
            elif a == b or b == c or c == a:
                sum_gcd += 3 * gcd
            else:
                sum_gcd += 6 * gcd
print(sum_gcd)