import sys

N = int(input())

info = []

hmax = 0
for i in range(N):
    x = list(map(int, input().split()))
    if(x[2]  > hmax):
        hmax = x[2]
    info.append(x)

H = hmax

H
while(1):
    for cx in range(101):
        for cy in range(101):
            for item in info:
                x = item[0]
                y = item[1]
                h = item[2]
                H = abs(x-cx) + abs(y-cy) + h
                if(max([H - abs(x-cx) -abs(y-cy), 0]) != h):
                    flag = 0
                    break
                else:

    if(flag == 1) :
        print(cx, cy, H)
        break
    else:
        H += 1
