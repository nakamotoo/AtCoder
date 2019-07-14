import numpy as np
import sys

N = int(input())

a = np.array(list(map(int, input().split())))

minIndex = [i for i, x in enumerate(a) if x == min(a)]


for argmin in minIndex:

    amin = a[argmin]

    i = argmin
    ai = amin
    ans = [0 for i in range(N)]
    for _ in range(N):
        ans[i] = ai
        if(i == 0):
            i = N-1
        else:
            i-= 1
        anext = a[i]
        tmp = anext - ai/2
        ai = int(2*tmp)

    if(ai == amin):
        print(ans)
        sys.exit()
    else:
        ans = [0 for i in range(N)]
        i = argmin
        ai = 0
        ans = [0 for i in range(N)]
        for _ in range(N):
            ans[i] = ai
            if(i == 0):
                i = N-1
            else:
                i-= 1
            anext = a[i]
            tmp = anext - ai/2
            ai = int(2*tmp)
        if(ai == amin):
            print(ans)
            sys.exit()
