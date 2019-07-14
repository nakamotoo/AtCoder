import sys

n, m , x, y= map(int, input().split())

X = list(map(int, input().split()))

Y = list(map(int, input().split()))

xm = max(X)

ym = min(Y)


for z in range(x+1, y+1):
    if(z > xm and z <= ym):
        print("No War")
        sys.exit()


print("War")
