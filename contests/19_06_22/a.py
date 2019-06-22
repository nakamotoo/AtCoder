s = input()

flag = 0
for i in range(1,4):
    if(s[i] == s[i-1]):
        flag = 1
        break

if flag == 0:
    print("Good")
else:
    print("Bad")
