N = int(input())
d = list(map(int, input().split()))

d = sorted(d)

i = N//2 - 1
j = N//2

print(d[j] - d[i])
