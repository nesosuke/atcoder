x, y = map(int, input().split())
a = y/x
if x == y:
    print(0)
    exit()
diff = abs(y-x)
if diff < min(x, y)/2:
    print(diff)
    exit()

i = 0
while x*(2**(i)) < y and y < x*(2**(i+1)):
    i += 1
    diff = abs(y-x)
i += diff
print(i)
