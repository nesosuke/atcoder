n, k = map(int, input().split())
n = str(n)

if k == 0:
    print(n)
    exit()

g1 = int(''.join(sorted(n, reverse=True)))
g2 = int(''.join(sorted(n)))
fx = g1 - g2

for i in range(1, k):
    g1 = int(''.join(sorted(str(fx), reverse=True)))
    g2 = int(''.join(sorted(str(fx))))
    fx = g1 - g2
print(fx)
