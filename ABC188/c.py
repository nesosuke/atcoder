n=int(input())
a=list(map(int,input().split()))
a.remove(max(a))
semiscore=max(a)
i = 0
while a[i] != semiscore:
    i+=1
print(i)