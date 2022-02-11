n, m = map(int, input().split())

if m == 0:
    out = n
if n == 0:
    out = 0
    
out = int(((10**n) // m) % m)
print(out)
