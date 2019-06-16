a, b, c = map(int, input().split())

v1 = a + b
v2 = b + c
v3 = c+a

v = [v1,v2,v3]
print(min(v))
