import itertools

N, k = map(int, input().split())



bits = [format(i,'b').zfill(N) for i in range(2**N)]

ans = [0 for i in range(k)]

for item in bits:
    if item.count('1') != k:
        continue;
    else:
        i_prev = "0"
        count = 0
        for i in item:
            if i == "1" and i_prev == "0":
                count += 1
            i_prev = i
        ans[count-1] += 1

# for i in ans:
#     print(i % 1000000007 )

print(ans)
