n = int(input())
nuts = list(map(int, input().split()))
total = 0
for i in range(n):
    if nuts[i] > 10:
        total += (nuts[i]-10)
print(total)
