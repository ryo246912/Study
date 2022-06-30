a = int(input(""))

#MEMO x ,y ,z = map(int, input("").split()) → 変数一つの場合はmap objectになる
#MEMO (int(x) for x in input("").split())
# b,c = map(int, input("").split())
b,c = (int(x) for x in input("").split())

s = input("")

print(f"{a + b + c} {s}")