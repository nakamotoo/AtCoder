N, M = map(int, input().split())
k = []
s = []
for i in range(M):
    inp = list(map(int,input().split()))
    k.append(inp[0]) # 0 - M-1
    s.append(inp[1:]) # s[i] index: 0 - k-1

p = list(map(int,input().split()))

bits = [format(i,'b').zfill(N) for i in range(2**N)]

count = 0
for bit in bits:
    d = 1
    for i in range(M):
        sum = 0
        for sl in s[i]:
            sum = sum + int(bit[sl-1])
        if sum % 2 != p[i]:
            d = 0
            break
    count += d

print(count)
