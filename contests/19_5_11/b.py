# passed

import math
input = input().split()
r = int(input[0])
g = int(input[1])
b = int(input[2])
N = int(input[3])

count = 0
# print(N/r)
# print(math.ceil(N/r))
for x in range(math.ceil(N/r+0.0001)):
    for y in range(math.ceil((N-x*r)/g + 0.0001)):
        # print(str(x), str(y))
        if  (N - x*r - y*g) % b == 0:
            count +=1

print(count)
