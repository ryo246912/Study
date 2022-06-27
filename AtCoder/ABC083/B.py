N , A , B = map(int ,input().split()) 

total = 0

def keta (x):
	return x % 10

for x in range(N + 1):
	##MEMO 10**n
	sum = keta(x // 10000) + keta(x // 1000) + keta(x // 100) + keta(x // 10)+ keta(x)
	##MEMO A <= sum <= B
	if A <= sum <= B:
		total += x

print(total)