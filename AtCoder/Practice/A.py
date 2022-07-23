a = int(input(""))

#MEMO1: x = map()のように変数一つだとxはmap objectになる
#MEMO1: x ,y ,z = map(int, input("").split()) 
#MEMO2: 内包表記:(int(x) for x in input("").split())
# b,c = map(int, input("").split())
b,c = (int(x) for x in input("").split())

s = input("")

print(f"{a + b + c} {s}")