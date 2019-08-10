n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
anext = a[n]

sum = 0

for i in range(n):
    ind = n - i - 1
    if b[ind] <= anext:
        sum += b[ind]
        anext = a[ind]
        continue
    elif (b[ind] > anext) and (b[ind] < anext + a[ind]):
        sum += b[ind]
        anext = anext + a[ind] - b[ind]
        continue
    else:
        sum += anext + a[ind]
        anext = 0

print(sum)
