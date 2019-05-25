N, M = map(int, input().split())

lmax = 0
rmin = N
for i in range(M):
    l, r = map(int, input().split())
    if l > lmax:
        lmax = l
    if r < rmin:
        rmin = r

if lmax > rmin:
    print(0)
else:
    print(rmin-lmax+1)
