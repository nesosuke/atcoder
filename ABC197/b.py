h,w,x,y=map(int,input().split())
count_seethru=0
for row in range(h):
    s=str(input())
    # (x,y)の上下左右に#がない場合の数を求める
    