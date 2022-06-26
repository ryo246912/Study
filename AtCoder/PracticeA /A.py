a = int(input(""))

# b,c = map(int, input("").split())
b,c = (int(x) for x in input("").split())

s = input("")

print(f"{a + b + c} {s}")