x,n = map(int,input().split())
nglist = list(map(int,input().split()))

dif = 100
for i in range(len(plist)):
    if abs(x - i )< dif:
        dif = x - i
print()
