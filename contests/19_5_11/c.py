# wrong answer...

import math
N = int(input())
l = []
for i in range(N):
   l.append(input())

default = sum(['AB' in i for i in l])

#only末尾Aの数
a = sum([i[-1]=='A' and i[0]!='B' for i in l])
#only先頭Bの数
b = sum([i[0]=='B' and i[-1]!='A' for i in l])
#先頭Bかつ末尾Aの数
ab = sum([i[0]=='B' and i[-1]=='A' for i in l])

if a == b:
    if ab > a:
        print("!")
        num = 2 * a + ab - a -1
    elif ab == a:
        print("!!")
        num = 2 * a
    elif ab < a:
        print("!!!")
        num = 2 * ab + a - ab
else:
    min = min(a, b)
    max = max(a, b)
    gap = abs(a-b)
    if ab <= min:
        print("!!!!")
        num = ab * 2 + min - ab
    elif ab > min:
        print("!!!!!")
        num = min * 2 + ab - min - 1

print(num + default)
