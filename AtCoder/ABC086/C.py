N = int(input())
arr = []

t = 0
x = 0
y = 0

#MEMO1: 標準入力はリストで格納しなくても、range内で毎回受け取れる
#MEMO1: for j in range(N):
#MEMO1:     tj , xj , yj = map(int,input().split())

for i in range(N):
    arr.append(
        list(map(int,input().split()))
    )

for j in arr:
    tj = j[0]
    xj = j[1]
    yj = j[2]
    if abs(xj - x)  + abs(yj - y) <= (tj - t) and (abs(xj - x)  + abs(yj - y)  - (tj - t )) % 2 == 0:
        t = tj
        x = xj
        y = yj
        continue
    print('No')
    break
else:
    print('Yes')

