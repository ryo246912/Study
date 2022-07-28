# N:コイントスの回数、B：連続表に応じたボーナス
N , M = map(int,input().split())
X = list(map(int,input().split()))
B = {}
for _ in range(M):
    c,y = map(int,input().split())
    B.update({c:y})    

ans = 0
cache = {}

#FIXME TLE
for i in range(2 ** N):
    yen = 0
    cnt = 0
    # MEMO 1:(i & 1)^1、ビット演算
    if (i & 1)^1 and i >> 1 in cache:
        cache.update({i:cache.get(i >> 1)})
        continue
    for j in range(N):
        if ((i >> j) & 1):
            yen += X[j]
            cnt += 1
            yen += B.get(cnt,0)
        else:
            cnt = 0
    if ans < yen:
        ans = yen
    cache.update({i:yen})

print(ans)