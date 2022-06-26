A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0

for x in range(A + 1):
	for y in range(B+ 1):
		z = (X - (500 * x + 100 * y)) // 50 
		if x <= A and y <= B and z <= C and x >= 0 and y >= 0 and z >= 0 and X == 500 * x + 100 * y + 50 * z:
			cnt += 1

print(cnt)