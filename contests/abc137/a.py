import sys


a, b = map(int, input().split())
v1 = a+b
v2 = a-b
v3 = a*b

print(max([v1,v2,v3]))
