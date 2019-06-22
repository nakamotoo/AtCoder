import sys

N = int(input())

w = []

limit = 0

for _ in range(N):

    ai, bi = map(int, input().split())
    w.append((ai, bi))

w = sorted(w, key=lambda x:x[1])

now = 0
for v in w:
    limit = v[1]
    now += v[0]
    if now > limit:
        print('No')
        sys.exit()

print('Yes')
