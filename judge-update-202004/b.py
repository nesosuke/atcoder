#!/usr/bin/python3
n = int(input())
list_input = []
list_red = []
list_blue = []
for i in range(n):
    list_input.append(list(map(str,input().split())))
for i in range(n):
    if list_input[i][1] == "R":
        list_red.append(int(list_input[i][0]))
    elif list_input[i][1] == "B":
        list_blue.append(int(list_input[i][0]))
list_red.sort()
list_blue.sort()
if len(list_red) != 0:
    for i in range(len(list_red)):
        print(list_red[i])
if len(list_blue) != 0:
    for i in range(len(list_blue)):
        print(list_blue[i])