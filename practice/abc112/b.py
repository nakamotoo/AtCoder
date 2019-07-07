N, T = map(int, input().split())

minc = 10000
for i in range(1, N+1):
	c, t = map(int, input().split())
	if t <= T and c < minc:
		minc = c

if minc == 10000:
	print('TLE')
else:
	print(minc)
