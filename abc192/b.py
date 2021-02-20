s = str(input())
if len(s) == 0:
    print('No')
    exit()

if len(s) == 1:
    if str.islower(s[0]) == True:
        print('Yes')
        exit()
    else:
        print('No')
        exit()

if len(s) % 2 == 0:  # 偶数字数
    for i in range(0, len(s), 2):
        if str.islower(s[i]) is False or str.isupper(s[i+1]) is False:
            print('No')
            exit()

if len(s) % 2 == 1:  # 奇数字数
    for i in range(1, len(s), 2):
        if str.islower(s[i-1]) is False or str.isupper(s[i]) is False:
            print('No')
            exit()
            
print('Yes')
