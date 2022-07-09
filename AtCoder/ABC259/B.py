import math

a , b, d = map(int,input().split())
ang = d/180*math.pi

## MEMO math.pi math.sin math.cos
print(f'{a*math.cos(ang)-b*math.sin(ang)} {a*math.sin(ang)+b*math.cos(ang)}')