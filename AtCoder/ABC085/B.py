N = int(input())
d = []

#MEMO input()をN回実施
#MEMO for i in range(N):
#MEMO     d.append(int(input()))

for i in range(N):
    d.append(int(input()))

print(len(set(d)))
