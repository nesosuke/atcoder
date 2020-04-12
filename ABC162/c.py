#!/usr/bin/python3
K = int(input())
sum_gcd = 0
gcd = 0
for a in range(K+1,1,-1):
    for b in range(K+1,1,-1):
        for c in range(K+1,1,-1):
            i = max(a,b,c)
            while i <= min(a,b,c):
                if a == b and b ==c:
                    gcd = a
                elif a % i == 0 and b % i == 0 and c % i == 0:
                   gcd = i  
                   break
                i -= 1
            sum_gcd += gcd
print(sum_gcd)                