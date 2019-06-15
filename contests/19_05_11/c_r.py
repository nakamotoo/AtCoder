# wrong answer...
# 正解はこちら　https://img.atcoder.jp/diverta2019/editorial.pdf

import math
N = int(input())
l = []
for i in range(N):
   l.append(input())

default = sum([i.count('AB') for i in l])

#only末尾Aの数
a = sum([i[-1]=='A' and i[0]!='B' for i in l])
#only先頭Bの数
b = sum([i[0]=='B' and i[-1]!='A' for i in l])
#先頭Bかつ末尾Aの数
ab = sum([i[0]=='B' and i[-1]=='A' for i in l])

num = 0
if ab == 0:
    num = min(a, b)
elif a + b > 0: # a, bの少なくとも一方は0出ない場合
    num = min(a, b) + ab
else:
    num = ab -1

print(num + default)
