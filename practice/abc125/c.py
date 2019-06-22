# https://atcoder.jp/contests/abc125/submissions/6047044

import functools
import math

N = int(input())

a = list(map(int, input.split()))

gcd = functools.reduce(math.gcd, a)

max = 0

for i in a:
    gcd = functools.reduce(math.gcd, a)
print(gcd)
