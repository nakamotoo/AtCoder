import math

n, k = map(int, input().split())

prob = 0

if n < k:
    for  i in range(1, n+1):
        prob += 0.5**math.ceil(math.log2(k/i)) * (1/n)
    print(prob)
else:
    for  i in range(1, k):
        prob += 0.5**math.ceil(math.log2(k/i)) * (1/n)
    print(prob + (n-k+1)/n)
