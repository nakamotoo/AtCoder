N, L = map(int, input().split())

sum = 0
min = 100000
min2 = 0
for i in range(0, N):
    aji = L+i
    sum += aji
    if(abs(aji) < min):
        min = abs(aji)
        min2 = aji

print(sum - min2)
