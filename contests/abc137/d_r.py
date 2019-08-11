from heapq import heappush, heappop

n, m = map(int, input().split())

works = []

for _ in range(n):
    a, b = map(int, input().split())
    works.append((a, b))

works.sort(reverse = True)

hq = []
ans = 0

for i in range(1, m+1):
    while works and works[-1][0] <= i:
        a, b = works.pop()
        heappush(hq, -b)
    if hq:
        b = -heappop(hq)
        ans += b

print(ans)
