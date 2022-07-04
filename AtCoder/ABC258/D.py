## WA×1あり
N , X = map(int,input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))

ans = a = arr[0][0] + arr[0][1] * X
for i in range(1,N):
    a = a + arr[i][0] + (arr[i][1] - arr[i-1][1]) * (X-i)
    if a < ans:
        ans = a

print(ans)