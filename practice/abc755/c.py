from collections import Counter

n = int(input())

v = list(map(int, input().split()))

e = v[0::2]
o = v[1::2]


ec = Counter(e)
oc = Counter(o)
em = ec.most_common()
om = oc.most_common()

count = 0

if em[0][0] != om[0][0] :
    count = n - em[0][1] - om[0][1]
elif em[0][1] >= om[0][1]:
    count = n - em[0][1] - oc[1][1]
else:
    count = n - om[0][1] - ec[1][1]


print(count)
