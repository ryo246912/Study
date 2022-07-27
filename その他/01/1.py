import sympy

s = input()
s_r = ""
l = list(s)
while len(l) != 0:
    s_r += l.pop()

pi = str(sympy.pi.evalf(1000000))
#MEMO str.find(x):文字列のインデックス位置を検索
print(f"{s}={pi.find(s) - 1}")
print(f"{s_r}={pi.find(s_r)- 1}")