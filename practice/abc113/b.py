N = int(input())
T, A = map(int, input().split())
h = list(map(int, input().split()))


min = 10000
mini = 0

for i, x in enumerate(h):
  val = T - x*0.006
  gap = abs(A-val)
  if gap < min:
    min = gap
    mini = i

print(mini+1)
