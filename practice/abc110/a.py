a, b, c = map(int, input().split())

sum = a + b + c
v1 = sum + 9*a
v2 = sum + 9*b
v3 = sum + 9*c
print(max([v1,v2,v3]))
