K = int(input())

h = K // 60
m = K % 60

#MEMO print(f'{21+h}:{0+m:02d}')
print(f'{21+h}:{str(0+m).zfill(2)}')
