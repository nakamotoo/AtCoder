# 尺取り法 O(n)
import sys

def input():
    return sys.stdin.readline()[:-1]

N, K = map(int, input().split())
a = list(map(int, input().split()))

count = 0
right = 0
sum = 0
for left in range(N):
    while(sum < K):
        if right == N:
            break
        else:
            sum += a[right]
            right += 1
    if sum < K:
        break
    count += N - right + 1
    sum -= a[left]

print(count)
