import numpy as np
import sys

L, R = map(int, input().split())

if( R - L >= 2018):
    print(0)
    sys.exit()

r = np.array(list(i for i in range(L, R+1)))


mins = 2018

for i, ri in enumerate(r):
    for j in range(i+1, len(r)):
        rj = r[j]
        s  = np.mod(ri * rj, 2019)
        if(s < mins):
            mins = s
        if(s == 0):
            print(0)
            sys.exit()



print(mins)
