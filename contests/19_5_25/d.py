import numpy as np
import sys

def input():
    return sys.stdin.readline()[:-1]

n, m = map(int, input().split())

a = np.sort(np.array(list(map(int, input().split()))))

for j in range(m):
    b, newVal = map(int, input().split())
    limit = np.sum(a < newVal)
    if newVal <= a[0]:
        continue
    elif b >= n:
        a = np.sort(np.concatenate([np.full(limit, newVal), a[limit:]]))
    elif limit <= b:
        a = np.sort(np.concatenate([np.full(limit, newVal), a[limit:]]))
    else:
        a = np.sort(np.concatenate([np.full(b, newVal), a[b:]]))

print(np.sum(a))
