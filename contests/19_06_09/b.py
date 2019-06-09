N = int(input())

num = list(map(int, input().split()))

min = 10000000


for t in range(1, N):
    pre = num[:t]
    post = num[t:]

    if pre[-1] == post[0]:
        continue
    else:
        presum = sum(pre)
        postsum = sum(post)
        gap = abs(presum-postsum)
        if gap < min:
            min = gap

print(min)
