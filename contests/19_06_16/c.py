W, H, x, y = map(int, input().split())

max = W*H/2.0

a = W/2
b = H/2

gap = 0.000000001
flag = 0

if(abs(x-a) < gap and abs(y-b) < gap):
    flag = 1

print('{:.6f} {}'.format(max, flag))
