n, m = map(int, input().split())

x = list(map(int, input().split()))

gap = []


if( n >= m):
    print(0)
    exit()
else:
    x = sorted(x)
    for i in range(m-1):
        gap.append(x[i+1] - x[i])
    gaps = sorted(gap)

print(sum(gaps[:m-n]))
