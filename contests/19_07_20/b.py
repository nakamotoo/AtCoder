import math

N, D = map(int, input().split())

a = D+D+1

print(math.ceil(N/a))
