import math

a , b, d = map(int,input().split())
ang = d/180*math.pi

## MEMO1: pi/sin/cosの使い方
## MEMO1: math.pi math.sin math.cos
print(f'{a*math.cos(ang)-b*math.sin(ang)} {a*math.sin(ang)+b*math.cos(ang)}')