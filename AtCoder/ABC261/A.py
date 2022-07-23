l1 , r1 , l2 , r2 = map(int,input().split())

if l1 > l2:
    bf = (l2,r2)
    af = (l1,r1)
else:
    bf = (l1,r1)
    af = (l2,r2)

if bf[1] < af[0]:
    print(0)
elif bf[1] <= af[1]:
    print(bf[1]-af[0])
else:
    print(af[1]-af[0])
