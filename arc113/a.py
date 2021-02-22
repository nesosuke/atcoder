k = int(input())
# 3つの整数組に因数分解する
count = 0
for a in range(1, k+1):
    bc = k / a
    if k % a != 0:
        pass
    else:
        print('bc', bc)
        for b in range(1, k+1):
            c = bc/b
            if bc % b != 0:
                pass
            else:
                print('c', c)
                count += 1
print(count)
