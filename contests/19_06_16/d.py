import sys

def input():
    return sys.stdin.readline()[:-1]

N, K = map(int, input().split())
a = list(map(int, input().split()))

from itertools import accumulate
count = 0
acum = list(accumulate(a))

if(acum[-1] < K):
    print(0)
    sys.exit()

for i in range(N-1, -1, -1):
    if acum[i] >= K:
        count += 1
    else:
        break

for i in range(N):
    for j in range(N-1, i, -1):
        s = acum[j]-acum[i]
        if s >= K:
            count += 1
        else:
            break

print(count)
