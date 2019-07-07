
s = input()

a = s.count(s[0])
b = s.count(s[1])
c = s.count(s[2])
d = s.count(s[3])

if(a==b==c==d==2):
    print("Yes")
else:
    print("No")
