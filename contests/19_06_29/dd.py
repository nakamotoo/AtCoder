import itertools

N, k = map(int, input().split())

bits = [1 for i in range(k)]
red = [0 for i in range(N-k)]

bits.extend(red)

p = list(set(itertools.permutations(bits,N)))

ans = [0 for i in range(k)]

for item in p:
    i_prev = 0
    count = 0
    for i in item:
        if i == 1 and i_prev == 0:
            count += 1
        i_prev = i
    ans[count-1] += 1

for i in ans:
    print(i % 1000000007 )
