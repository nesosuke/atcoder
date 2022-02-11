n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            xi, yi = grid[i][0], grid[i][1]
            xj, yj = grid[j][0], grid[j][1]
            xk, yk = grid[k][0], grid[k][1]
            S = 0.5 * abs((xk-xi)*(yj-yi)-(xj-xi)*(yk-yi))
            if S > 0:
                count += 1
print(count)
