K = int(input())

h = K // 60
m = K % 60

print(f'{21+h}:{str(0+m).zfill(2)}')