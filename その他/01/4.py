S = input()
l = len(S)
ans = 0

def x(str):
    if len(str) > 2:
        return int(str[:1]) + int(str[1:]) + x(str[1:])
    elif len(str) == 2:
        return int(str[:1]) + int(str[1:])
    else:
        return 0

def y(str , count = 0):
    if len(str) > 2:
        return int(str[:1]) + int(str[1:]) + y(str[1:],count)[1]
    else:
        return int(str[:1]) + int(str[1:]) , count

for i in range(l-1):
    print(y(S[i+1:]))
    # ans += int(S[:i+1]) + int(S[i+1:]) + y(S[i+1:])[1]



print(ans)