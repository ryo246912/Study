S = input()

start = 0
length = len(S)

# dream dreamer erase eraser

# dreamer|erase
# dreamer|eraser
# dreamer|dream
# dreamer|dreamer

# eraser|eraser
# eraser|erase
# eraser|dream
# eraser|dreamer

# [dream|er]ase
# [dream|er]aser
# dream|dream
# dream|dreamer

# erase|eraser
# erase|erase
# erase|dream
# erase|dreamer

## 完全一致でないと条件漏れあり
while 'dream' in S[start :start  + 10] or 'erase' in S[start :start  + 10]:
    search = S[start :start  + 10]
    if 'dreamerase' == search:
        start += 5
        continue
    if 'dreamer' == search[0:7]:
        start += 7
        continue
    if 'eraser' == search[0:6]:
        start += 6
        continue
    if 'dream' == search[0:5] or 'erase' == search[0:5]:
        start += 5

if start == length:
    print('YES')
else:
    print('NO')
