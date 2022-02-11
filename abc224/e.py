import numpy as np
h, w, n = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]

# grid = np.arange(h*w).reshape((h,w))
# grid=[list(map(int,input().split())) for i in range(n)]

for i in range(n):
    count=0
    for j in range(len(grid)):
        print(grid[j][2])