import sys

a, b = map(int, input().split())

if(a == b):
    print(0)
    sys.exit()
elif(abs(a+b) % 2 == 0):
    print(abs(a+b)//2)
else:
    print("IMPOSSIBLE")
