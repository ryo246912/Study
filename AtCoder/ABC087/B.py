A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0

##MEMO 繰り返しの場合、適宜break入れると処理回数を減らせて、実行時間を短くできる？
##MEMO if true: break
for x in range(A + 1):
	if X - 500 * x < 0: break
	remain = X - 500 * x
	for y in range(B+ 1):
		if remain - 100 * y < 0: break
		for z in range(C+1):
			if X == 500 * x + 100 * y + 50 * z:
				cnt += 1

print(cnt)