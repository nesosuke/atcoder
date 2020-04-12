#!/usr/bin/python3
K = int(input())
sum_gcd = 0
gcd = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            i = 1
            while i <= min(a,b,c):
                if a % i == 0 and b % i == 0 and c % i == 0:
                   gcd = i  
                i += 1
            sum_gcd += gcd
print(sum_gcd)                