n=int(input())
a=list(map(int,input().split()))
sumation=0
for i in range(0,n-1):
    sumation += a[i]*sum(a[i+1:])
print(sumation%(10**9+7))

