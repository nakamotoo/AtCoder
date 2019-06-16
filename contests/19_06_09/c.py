import scipy.misc as scm

N, M = map(int, input().split())

a_s = []
flag = False

for i in range(M):
    a_m = int(input())
    a_s.append(a_m)
    if(i > 0 and a_m == a_s[i-1]+1):
        flag = True
        print(0)
        break


if not flag:
    way = 1
    now = 0
    for a in a_s:
        # print("a = " + str(a))

        step = a - 1 - now
        # print("now = " + str(now))
        # print("step = " + str(step))
        w = 0
        for i in range(step//2+1):
            # print(str(step-i) + " C " + str(i))
            # print (scm.comb(step-i, i))
            w += scm.comb(step-i, i)
        if(w != 0):
            way = w * way
        now = a+1
        # print(w)

    step = N - now
    # print("way = " + str(way))
    w = 0
    for i in range(step//2+1):
        # print(str(step-i) + " C " + str(i))
        # print (scm.comb(step-i, i))

        w += scm.comb(step-i, i)
    print("w = " +str(w))
    if(w != 0):
        way = w * way

    print(int(way % 1000000007))
