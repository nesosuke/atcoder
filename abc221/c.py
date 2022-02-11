# --- 正攻法 ---

# # 整数Nの情報
# N = list(input())  # int -> list
# N.sort()  # 昇順
# num_zero = N.count("0")  # 0の個数
# N_digit = len(N)
# numbers_in_N=sorted(list(set(N)))


# # Nを2個の正整数a,bに分けることを考える
# # Nがn桁のとき，aの桁数はは最大で (n/2 - 1)桁

# # aの選び方について考える
# # N から i 個の数字を取り出す

# a = []
# for i in range(N_digit/2 - 1):
#     for j in
#     a.append()

# ---

# --- 適解(多分) ---
N = sorted(input(),reverse=True)

a=N[0::2]
b=N[1::2]

a=int("".join(a))
b=int("".join(b))
print(a*b)

# a, b = "", ""
# for i in range(int((len(N)+1)/2)):
#     for j in range(len(N)):
#         if len(N) == 0:
#             break
#         a += N[0]
#         N.remove(N[0])
#         if len(N) == 0:
#             break
#         b += N[0]
#         N.remove(N[0])
    
# print(a, b)
# print(int(a)*int(b))
