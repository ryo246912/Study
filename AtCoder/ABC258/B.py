N = int(input())
X = []
amax = 0

for _ in range(N):
    ##MEMO 空白なし文字列をリストにする list(str) => ['s','t','r']
    ##MEMO 行列matrixへのアクセス M = [[列1,列2],[列1,列2]] → M[行][列]でアクセス
    row = list(map(int,list(input())))
    amax = max(amax,max(row))
    X.append(row)

directions = [(1, 0), (1, 1), (0, 1), (-1, 1),(-1, 0), (-1, -1), (0, -1), (1, -1)]
##MEMO starts = [(i, j) for i in range(N) for j in range(N)] #(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),・・・
##MEMO for i, j in starts:
starts = [(i, j) for i in range(N) for j in range(N) if X[i][j] == amax]

smax = 0
for i, j in starts:
    for di, dj in directions:
        i_, j_ = i, j
        s = X[i_][j_]
        for k in range(N - 1):
            i_, j_ = (i_ + di) % N, (j_ + dj) % N
            s = 10 * s + X[i_][j_]
        ##MEMO 最大値を求める→各値と今の値の最大を大きさを毎回比べる
        if s > smax:
            smax = s
print(smax)

