import sys

k, x = map(int, input().split())

a = [str(i) for i in range(x-k+1, x+k)]

print(" ".join(a))
