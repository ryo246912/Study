H , W = map(int,input().split())
S = []

# H × Wマス
for _ in range(H):
    S.append(list(input()))

direction = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

for i in range(H):
    s = ''
    for j in range(W):
        a = 0
        if S[i][j] == "#":
            a = "#"
        else:
            for di , dj in direction:
                _i , _j = i + di ,j + dj
                if 0 <= _i < H and 0 <= _j < W:
                    a += 1  if S[_i][_j] == "#" else 0
        s += str(a)
    print(s)