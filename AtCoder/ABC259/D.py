#FIXME 008.txtだけTLEで通らない
N = int(input())
sx ,sy ,tx ,ty = map(int,input().split())
si = ti = -1
arr = []

##MEMO1: タプルtuple()
##MEMO1: X = [tuple(map(int, input().split())) for i in range(N)]
for i in range(N):
    #MEMO 2:変数命名xyr = tuple(map(int,input().split()))
    X = tuple(map(int,input().split()))
    arr.append(X)
    x,y,r = X
    if (x - sx) ** 2 + (y - sy) ** 2 == r ** 2:
        si = i
    if (x - tx) ** 2 + (y - ty) ** 2 == r ** 2:
        ti = i

#MEMO 2:変数命名seen
s = [si]
seen = {si}

#MEMO 3:一度チェック済を判定するには、別途集合を用意してチェックしたら格納して確認する
while len(s) != 0:
    _i = s.pop()
    x, y, r = arr[_i]
    if (x-tx)**2 + (y-ty)**2 == r**2:
        print("Yes")
        break
    for j in range(N):
        if j in seen:
            continue
        xj, yj, rj = arr[j]
        if (r - rj)**2 <= (x - xj)**2 + (y - yj)**2 <= (r + rj)**2:
            seen.add(j)
            s.append(j)
else:
    print('No')

# for j in range(N):
#     x = []
#     for k in range(N):
#         if j == k:
#             continue
#         if (arr[j][2] - arr[k][2]) ** 2 <= (arr[j][0] - arr[k][0])**2 + (arr[j][1] - arr[k][1])**2 <= (arr[j][2] + arr[k][2]) ** 2:
#             x.append(k)
#     arr2.append((arr[j],x))

# t = arr2[si][1]

# while len(t) != 0:
#     s = t.pop()
#     t += arr2[s][1]
#     if ti in t:
#         print('Yes')
#         break
# else:
#     print('No')






