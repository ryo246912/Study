import sys

H ,W = map(int,input().split())
s = []


for _ in range(H):
    s.append(list(input()))

for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            ok = False
            for di , dj in [(1,0),(0,-1),(-1,0),(0,1)]:
                _i , _j = i + di , j + dj
                if 0 <= _i < H and 0 <= _j < W and s[_i][_j] == "#":
                    ok = True
            if not ok:
                print("No")
                sys.exit()

print("Yes")

