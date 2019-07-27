import numpy

N = int(input())

a = list(map(int, input().split()))

b = [0 for i in range(N)]

ans = []

# print(a)

l = N//2

for i in range(l+1, N+1):
    b[i-1] = a[i-1]
    if a[i-1] == 1:
        ans.append(i)

ind = l
for _ in range(l):
    # print("ind" , str(ind))
    # print("b")
    # print(b)
    ai = a[ind - 1]
    iter = N // ind - 1
    s = 0
    for j in range(1, iter+1):
        s += b[ind + j * ind - 1]
    # print("s = " + str(s))
    if (s % 2) == ai:
        b[ind - 1] = 0
    else:
        b[ind - 1] = 1
        ans.append(ind)

    if ind == 1:
        break
    else:
        ind -= 1
# print("b")
# print(b)
m = sum(b)
# print("m")
print(m)

if m != 0:
    for c in ans:
        print(c, end =" ")
