#!/usr/bin/python3
import math
K = int(input())
sum_gcd = 0
for a in range(1,K+1):
    for b in range(1,a+1):
        for c in range(1,b+1):
            if a == b and b == c :
                sum_gcd += math.gcd(math.gcd(a,b),c)
            elif a == b or b == c or c == a:
                sum_gcd += 3 * math.gcd(math.gcd(a,b),c)
            else:
                sum_gcd += 6 * math.gcd(math.gcd(a,b),c)
print(sum_gcd)