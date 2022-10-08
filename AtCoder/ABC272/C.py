N = input()

EVEN_MAX = 0
EVEN_SUB_MAX = 0
ODD_MAX = 0
ODD_SUB_MAX = 0

for _x in input().split():
    x = int(_x)
    if x % 2 == 0 and x > EVEN_SUB_MAX:
        if x > EVEN_MAX:
            EVEN_SUB_MAX = EVEN_MAX
            EVEN_MAX = x
        else:
            EVEN_SUB_MAX = x
    elif x % 2 == 1 and x > ODD_SUB_MAX:
        if x > ODD_MAX:
            ODD_SUB_MAX = ODD_MAX
            ODD_MAX = x
        else:
            ODD_SUB_MAX = x
    else:
        pass

MAX = max((EVEN_MAX+EVEN_SUB_MAX,ODD_MAX+ODD_SUB_MAX))

if MAX % 2 == 0:
    print(MAX)
else:
    print("-1") 
