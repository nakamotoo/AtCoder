import sys

N = int(input())
a = list(map(int, input().split()))

val1 = a[0]
val2 = a[0] ^ a[0]

for i in range(1, N):
    val1 = val1 ^ a[i]
    val2 = val2 ^ a[i] ^ a[i]

if( val1 == val2):
    print("Yes")
else:
    print("No")
