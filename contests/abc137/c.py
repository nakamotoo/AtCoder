from collections import Counter
import json

N = int(input())
ss = []
c = []

for _ in range(N):
    s = input()
    ss.append("".join(sorted(s)))

sum = 0

for i , v in Counter(ss).items():
    sum += (v*(v-1)//2)
print(sum)
