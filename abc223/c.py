n = int(input())
length, speed = [], []
for i in range(n):
    data = list(map(int,input().split()))
    length.append(data[0])
    speed.append(data[1])

# 火花がぶつかる時刻をTとすると，
T = 0
for i in range(n):
    T += (length[i]/speed[i])
T = T/2
# したがって，時刻Tまでに進む距離Xは
X = 0
for i in range(n):
    X += min(length[i], speed[i]*T)
    T -= min(length[i]/speed[i], T)
print(X)
