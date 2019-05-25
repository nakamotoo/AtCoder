# 一個親のノードのidを格納
N = int(input())
id = [num for num in range(N)]
weight = [0 for num in range(N-1)]

def root(x):
    while x != id[x]:
        x = id[x]
    return x

for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    id[u] = v
    weight[u] = w

print(weight)
