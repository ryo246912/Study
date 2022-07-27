n = int(input().split()[1])
m = int(input().split()[1])

for i in range(1,n+1):
    if i <= m:
        continue
    s = i
    x_r = []
    # MEMO 1:m進数に変換するには、mで割っていき余りを逆に見る
    # MEMO 1:while s > 0:
    # MEMO 1:    a = s % m
    # MEMO 1:    s = s // m
    # MEMO 1:    x_r.append(str(a))
    # MEMO 1:x = list(reversed(x_r))
    while s > 0:
        a = s % m
        s = s // m
        x_r.append(str(a))
    #MEMO 2:list(reversed(A)):リストを逆順にする
    x = list(reversed(x_r))

    flag = True

    for p , q in zip(x,x_r):
        if p != q:
            break
        for j in range(3,i,2):
            if i % j == 0:
                flag = False
                break
    else:
        if flag: print("".join(x))
