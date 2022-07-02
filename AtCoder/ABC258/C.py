N , Q = map(int,input().split())
S = input()
p = 0

for i in range(Q):
    t , x = map(int,input().split())
    if t == 1:
        p += -x
        if p <= -N:
            p = p + N
    if t == 2:
        if p + x - 1 >= 0:
            print(S[p + x - 1])
        else:
            print(S[p + x - 1 + N])