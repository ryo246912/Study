S = input()
T = input()
    
def z(l):
    a = 1
    x = []
    length = len(l)
    
    for i in range(length):
        if i == length - 1 and l[i-1] != l[i]:
            x.append((l[i],1))
            continue
        if i == length - 1 and l[i-1] == l[i]:
            x.append((l[i],a))
            continue
        if l[i] == l[i+1]:
            a += 1
        else:
            x.append((l[i],a))
            a = 1
    
    return x
    
s = z(list(S))
t = z(list(T))

## MEMO1: zipの要素数が違う場合、少ない要素で展開終了
## MEMO1: for i , j in zip([1],[1,2]) → (i,j) = (1,1)で終了 
for x,y in zip(s,t):
    if x[0] != y[0]:
        print('No')
        break
    if x[1] > y[1] or (x[1] < y[1] and x[1] == 1):
        print('No')
        break
else:
    if len(s) != len(t):
        print('No')
    else:
        print('Yes')