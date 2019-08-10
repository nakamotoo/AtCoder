import sys

s = input()
h = s.count('?')
l = len(s)

if(l == 1):
    if s[0] == '?' or s[0] == '5':
        print(1)
        sys.exit()
    else:
        print(0)
        sys.exit()

max = 0

if(s[0] == '?'):
    max = 10**l
else:
    max = int(s[0]) * (10 **(l-1))


i = 0
ans = 0
# cleans = s.replace("?", "")

def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L

hatena = index_Multi(s, '?')

def str_del(str,index):
    str = str[:index]+str[index+1:]
    return str

while (13*i+5 <= max):
    num = list(str(13 * i + 5))
    if(len(num) < l):
        num = ['0' for i in range(l-len(num))] + num

    for j in hatena:
        num[j] = '?'

    # flag = 1
    # for a, b in zip(s, num):
    #     if(a == '?' or a == b):
    #         continue
    #     else:
    #         flag = 0
    #         break
    # ans += flag
    if("".join(num) == s):
        ans+=1
    i += 1

print(ans % 1000000007)
