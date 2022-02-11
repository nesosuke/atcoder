h, w = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(h)]
for i1 in range(h):
    for i2 in range(i1+1, h):
        for j1 in range(w):
            for j2 in range(j1+1, w):
                a = grid[i1][j1]+grid[i2][j2]
                b = grid[i2][j1]+grid[i1][j2]
                if a <= b:
                    continue
                else:
                    exit("No")
print("Yes")
