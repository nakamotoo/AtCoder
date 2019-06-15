N = int(input())

l = []

for i in range(N):
    s , p = map(str, input().split())
    p = 100-int(p)
    if p == 100:
        l.append(s+str(999))
    elif p < 10:
        l.append(s+str(0)+str(p))
    else:
        l.append(s+str(p))
l_new = sorted(l)
# print(l)
# print(l_new)
for i in l_new:
    print(l.index(i)+1)
