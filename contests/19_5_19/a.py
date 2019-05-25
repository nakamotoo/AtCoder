N, K = map(int, input().split())

S = input()

pre = S[0:K-1]

behind = S[K:]

new = pre+S[K-1].lower() + behind

print(new)
