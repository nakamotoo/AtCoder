n, k = map(int, input().split())
maxPossible = (n - 2) * (n - 1) // 2
if k > maxPossible:
    print(-1)
    exit()
ret = []
for i in range(2, n + 1):
    ret.append((1, i))
add = []
for i in range(2, n):
    for j in range(i + 1, n + 1):
        add.append((i, j))
for i in range(maxPossible - k):
    ret.append(add[i])
print(len(ret))
print('\n'.join('%d %d' % (u, v) for u, v in ret))
