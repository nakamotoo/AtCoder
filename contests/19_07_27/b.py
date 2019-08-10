import sys

n = int(input())

p = list(map(int, input().split()))

ps = sorted(p)

count = 0

for a, b in zip(p, ps):
    if(a != b):
        count += 1
    if(count > 2):
        print("NO")
        sys.exit()
        break

print("YES")
