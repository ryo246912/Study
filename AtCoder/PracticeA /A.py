a = int(input("a:"))

# b,c = map(int, input("b,c:").split())
b,c = (int(x) for x in input("b,c:").split())

s = input("s:")

print(f"{a + b + c} {s}")