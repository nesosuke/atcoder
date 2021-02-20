x = input()
m = int(input())

cnt = 0
d = int(max(x))

if d ==0 or d ==1:
    pass

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

a = int(Base_10_to_n(int(x), d+1))
print(d+1,a)
cnt=0
while a <= m:
    a = int(Base_10_to_n(int(x), d+1))
    print(a)
    if a > m:
        break
    d += 1
    cnt+=1
print(cnt)

