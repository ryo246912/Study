N , M = map(int,input().split( ))
X = {(i,j) for i in range(1,N+1) for j in range(i+1,N+1)}

for _ in range(M):
    k , *num = map(int,list(input().split( )))
    for _i in range(k):
        for _j in range(_i+1,k):
            if (num[_i],num[_j]) in X: X.remove((num[_i],num[_j]))

if len(X) > 0:
    print('No')
else:
    print('Yes')
