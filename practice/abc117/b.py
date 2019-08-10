n = int(input())

l = list(map(int, input().split()))

a = max(l)

s = sum(l) - a

if(a < s):
    print("Yes")
else:
    print("No")
