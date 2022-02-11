n, p = map(int, input().split())
students = list(map(int, input().split()))
fail = 0
for i in range(len(students)):
    if students[i] < p:
        fail += 1
print(fail)
