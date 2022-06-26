A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0

import itertools

#MEMO itertools.product(range(A+1), range(B+1), range(C+1))でforをネストしなくてもいい
for x, y ,z in itertools.product(range(A+1), range(B+1), range(C+1)):
	if X == 500 * x + 100 * y + 50 * z:
		cnt += 1

print(cnt)