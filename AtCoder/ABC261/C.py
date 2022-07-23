N = int(input())
S = {}

for i in range(N):    
    s = input()
    cnt = S.get(s,0)
    m = f"({cnt})" if cnt != 0 else ""
    print(f"{s}{m}")    
    S.update({s:cnt+1})