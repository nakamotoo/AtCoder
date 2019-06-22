N, M = map(int, input().split())

flag = [ 0 for i in range(N+1)]
dp = [0 for i in range(N+1)]

for _ in range(M):
    a = int(input())
    flag[a] = 1


dp[0] = 1
if flag[1] == 1:
    dp[1] = 0
else:
    dp[1] = 1;

for i in range(2, N+1):
    if flag[i] == 1:
        dp[i] = 0
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[N])
