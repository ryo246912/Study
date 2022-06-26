count = input()
num = list(map(int , input().split()))

cnt = 0

while sum([x % 2 for x in num]) == 0:
    cnt += 1
    num = [x/2 for x in num]

print(cnt)
