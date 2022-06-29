s = input()

##MEMO 変数命名の一例
##MEMO dm = 'dream'
##MEMO dmr = 'dreamer'
##MEMO es = 'erase'
##MEMO esr = 'eraser'

#解き方1
s = s.replace('eraser', '')
s = s.replace('erase', '')
s = s.replace('dreamer', '')
s = s.replace('dream', '')

if not s:
    print("YES")
else:
    print("NO")

#解き方2
while s != "":
    if(s[-5:] == "dream" or s[-5:] == "erase"):
        s = s[:-5]
    elif s[-6:] == "eraser":
        s = s[:-6]
    elif s[-7:] == "dreamer":
        s = s[:-7]
    else:
        break
if s == "":
    print("YES")
else:
    print("NO")

#解き方3
while s != "":
    if(s[-5:] == "dream" or s[-5:] == "erase"):
        s = s[:-5]
        continue
    if s[-6:] == "eraser":
        s = s[:-6]
        continue
    if s[-7:] == "dreamer":
        s = s[:-7]
        continue
    else:
        break

if s == "":
    print("YES")
else:
    print("NO")