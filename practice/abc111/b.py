N = int(input())

x = N
while(1):
    s = str(x)
    if(s[0] == s[1] == s[2]):
        print(x)
        break
    else:
        x += 1
