N = int(input())
S = str(input())
W = list(map(int,input().split()))

arr = []
for i in range(N):
    arr.append((int(S[i]),W[i]))

arr_sorted = sorted(arr,key= lambda x:x[1])

# child = 0 / adult = 1 
D = []
D.append(len([ x for x in arr_sorted if x[0] == 1]))
add = 0

##MEMO ループに応じて計算するには、for外でx=で定義→ループ内でx+=1等行う、
##MEMO ループごとに計算リセットするには、forの最後にx=0ように宣言してリセット
for i in range(N):
    if i!= N-1 and arr_sorted[i][1] == arr_sorted[i+1][1]:
        add += 1 if arr_sorted[i][0] == 0 else -1
        continue
    add += 1 if arr_sorted[i][0] == 0 else -1
    D.append( D[-1] + add)
    add = 0

print(max(D))