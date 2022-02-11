import math


def calc_sum(value):
    sum_row = 0
    for row in range(3):
        if '0' not in value[row]:
            sum_row = sum(value[row])
            break
    return sum_row


def func_1行に0が2個あるかどうか判定する(value):
    for row in range(len(value)):
        if value[row].count(0) == 2:
            return True
    return False


size = int(input())
value = []
for row in range(size):
    value.append(list(map(int, input().split())))

print(func_1行に0が2個あるかどうか判定する(value))