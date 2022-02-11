#/usr/bin/python3
n = int(input())
list_a = list(map(int, input().split()))
result = 1
#if 0 in list_a:
#        print(0)
#        exit()
  
for i in range(n):
    result *= int(list_a[i])
if result > 10**18:
    print("-1")
    exit()
print(result)