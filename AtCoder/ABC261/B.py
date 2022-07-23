N = int(input())
X = [list(input()) for _ in range(N)]
p = [(i, j) for j in range(1,N) for i in range(j)]
#MEMO 1:(i, j) for j in range(1,N) for i in range(j)はfor j→for iの順で実行される
#MEMO 1:for j in range(1,N):
#MEMO 1:   for i in range(j):
#MEMO 1:        (i,j)に相当

for i, j in p:
    if X[i][j] == 'W' and X[j][i] == 'L':
        continue
    if X[i][j] == 'L' and X[j][i] == 'W':
        continue
    if X[i][j] == 'D' and X[j][i] == 'D':
        continue
    print('incorrect')
    break
else:
    print('correct')