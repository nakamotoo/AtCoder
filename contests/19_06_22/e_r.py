# https://img.atcoder.jp/abc131/editorial.pdf

import sys

n, k = map(int, input().split())

maxPossible = (n-2) * (n-1) // 2

if k > maxPossible:
    print(-1)
    sys.exit()
ret = []

# うに(1が中心)
for i in range(2, n+1):
    ret.append((1, i))

# maxPossible - k 個の辺を追加
count = 0
for i in range(2, n+1):
    if count == maxPossible - k:
        break
    for j in range(i+1, n+1):
        ret.append((i, j))
        count += 1
        if count == maxPossible - k:
            break

print(len(ret))
for u, v in ret:
    print(u, v)
