
N, X = map(int, input().split())

ls = list(map(int, input().split()))

count = 1
dis = 0

for l in ls:
    new_dis = dis + l
    if(new_dis <= X):
        count += 1
        dis  = new_dis
    else:
        break

print(count)
