# # 文字列の操作，左シフト，右シフト
s = str(input())


def shift_left(string, count):
    res = string[count:]+string[0:count]
    return res


def shift_right(string, count):
    res = string[-count:]+string[0:-count]
    return res


L = []
L.append(s)
if len(s) != 1:
    for i in range(len(s)):
        L.append(shift_left(s, i))
        L.append(shift_right(s, i))
    L = sorted(L)
print(L[0])
print(L[-1])
