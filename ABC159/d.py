#!/usr/bin/python3
# わ～～～～～からんですわ～～～～～～～
N = int(input())
A = list(input().split())
SolCnt = 0
for i in range(N):
    print(i)
    for j in range(N-i+1):
        if j != i :
            for p in range(N-j+1):
                print("i, j, p", A[i],A[j],A[p])
                #if A[j] == A[p]:
                #    SolCnt += 1
            
#        if A[i] == A[j]:

       
#        print(A[0:j])
#        print(A[j+1::])
    print(SolCnt)