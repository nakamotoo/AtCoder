s = int(input())

ss = []

ss.append(s)
i = 1

def has_dup(list):
    return len(list) != len(set(list))

while(has_dup(ss) == False):
    if(ss[-1] % 2 == 0):
        ss.append(ss[-1]/2)
    else:
        ss.append(3*ss[-1]+1)
    i += 1

print(i)
