# N:整数
# f(x):各桁の和
# xに対して、f(2x)が最大になるMとそれに対する最小のx

N = int(input())

M = N * 2

s = N // 4
a = N % 4
x = int("".join([str(a)]+['4']*s))

# s = (M-8) // 9
# a = (M-8) % 9
# if M > 8:
#     x2 = int("".join([str(a)]+['9']*s+['8']))
# else:
#     x2 = int(M)

print(M)
print(x)