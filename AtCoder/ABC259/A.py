N , M , X , T , D = input().split()

# Xまで成長
#  X < M < N
#  M < X < N

if int(M) >= int(X):
    print(int(T))
else:
    print(int(T)-(int(X)-(int(M)))*int(D))