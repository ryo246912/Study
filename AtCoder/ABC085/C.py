N , Y = map(int,input().split())

# Y = 10000 * a + 5000 + b + 1000 * c
# N = a + b + c

# y = 10 * x + 5 * y + c
# c = y % 5
# N = a + b + y % 5

flag = False
ans = '-1 -1 -1'

for x in range(Y // 10000 + 1):
    if x > N: break
    for y in range((Y - 10000 * x) // 5000 + 1):
        if x + y > N: break
        if (Y - 10000 * x - 5000 * y) / 1000 == N - x - y:
            ans = f'{x} {y} {N - x - y}'
            flag = True
            break

##MEMO ループを途中で切り上げる方法として、def():にしてreturnで返すようにする
##MEMO x = (-1,-1,-1) => *x = "-1 -1 -1"
print(ans)