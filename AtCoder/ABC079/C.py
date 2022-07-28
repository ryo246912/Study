#MEMO1: list(map(int,list(input()))):連結した文字列を数字の配列に
ABCD = list(map(int,list(input())))

for i in range(8):
    ans = ABCD[0]
    f = f'{ABCD[0]}'
    for j in range(3):
        if (i>>j & 1):
            ans += ABCD[j+1]
            f += f'+{ABCD[j+1]}'
        else:
            ans -= ABCD[j+1]
            f += f'-{ABCD[j+1]}'
    if ans == 7:
        f += "=7"
        print(f)
        break