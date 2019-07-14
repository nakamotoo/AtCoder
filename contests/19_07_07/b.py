import numpy as np

N, D = map(int, input().split())

xs = []

for _ in range(N):
    xs.append(list(map(int, input().split())))

xs = np.array(xs)

count = 0

for i, xi in enumerate(xs):
    for j in range(i+1, N):
        # print("i=" + str(i))
        # print("j=" + str(j))
        xj = xs[j]
        tmp = xi - xj
        tmp2 = tmp ** 2
        d = np.sqrt(np.sum(tmp2))
        if d - int(d) == 0:
            count += 1

print(count)
