
N = int(input())


a = []
for _ in range(N):
    n = int(input())
    a.append(n)

sorted = sorted(a)

max1 = sorted[-1]
max2 = sorted[-2]

for i in a:
    if i == max1:
        print(max2)
    else:
        print(max1)
