n, m = map(int, input().split())
# for i in range(2*n):
#     hands = list(input())
# wins = [0]*2*n

# わからん

hands = [input() for i in range(2*n)]
rank = [[0, i] for i in range(2*n)]  # [wins, number]


def judge(a, b):
    # 引き分け:-1, a勝ち:0, b勝ち:1
    if a == b:
        return -1
    if (a, b) == ("C", "G"):
        return 1
    if (a, b) == ("G", "P"):
        return 1
    if (a, b) == ("P", "C"):
        return 1
    else:
        return 0


for i in range(m):
    for j in range(n):
        player1 = rank[2*i][1]
        player2 = rank[2*i+1][1]
        result = judge(hands[player1][j], hands[player2][j])
        if result != -1:
            rank[2*i+result][0] -= 1
    rank.sort()
for i in rank:
    print(i+1)
