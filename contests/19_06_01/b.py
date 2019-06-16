S = input()

o_count = 0
x_count = 0
k = len(S)
amari = 15-k

for i in range(len(S)):
    if S[i] == 'o':
        o_count += 1
    if S[i] == 'x':
        x_count += 1

if o_count + amari >= 8:
    print('YES')
else:
    print('NO')
