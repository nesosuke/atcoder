k = int(input())
# 調和級数
count = 0
for a in range(1, k+1):
    for b in range(a,k+1):
        for c in range(b,k+1):
            p=a*b*c
            if p <= k :
                count+=1
            
print(count)
