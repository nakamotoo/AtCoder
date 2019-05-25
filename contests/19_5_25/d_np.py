import numpy as np
import sys

def input():
    return sys.stdin.readline()[:-1]

n, m = map(int, input().split())

a = np.array(list(map(int, input().split())))

for j in range(m):
    b, newVal = map(int, input().split())
    if newVal <= a[0]:
        continue
    elif b >= n:
        a = np.sort(np.where(a < newVal, newVal, a))
    else:
        a0, a1 = np.split(a, [b])
        a0_new = np.where(a0 < newVal, newVal, a0)
        a = np.sort(np.concatenate([a0_new, a1]))

print(np.sum(a))
