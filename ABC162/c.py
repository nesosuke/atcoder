#!/usr/bin/python3
import math
K = int(input())
sum_gcd = 0

# K以下の素数
primelist = []
for i in range(1, K+1):
    for j in range(2, int(math.sqrt(K)) + 1):
        if i % j == 0:
            primelist.append(i)

# a,bの2項で検索 => 候補抽出(gcd_cand)
gcd_cand = []
for a in range(1, K+1):
    for b in range(1, K+1):
        if a == b:
            gcd_cand.append(a)
        else:
            for p in range(len(primelist)):
                if a % p == 0 and b % p == 0:
                    gcd_cand.append(a)

print(gcd_cand)
# cとgcd_candで比較
for c in range(1, K+1):
    for q in range(len(gcd_cand)):
        print(c,gcd_cand[q])

        if c == gcd_cand[q]:
            gcd = c
        else:
            for r in range(len(primelist)):
                if c % r == 0 and gcd_cand[q] % r == 0:
                    sum_gcd += r

print(sum_gcd)                