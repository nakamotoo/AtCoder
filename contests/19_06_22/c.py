

a, b, c, d = map(int, input().split())


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

cd = lcm(c, d)

div_c = b // c - (a-1)//c
div_d = b // d - (a-1)//d
div_cd = b // cd - (a-1)//cd
count = b - a + 1 - div_c - div_d + div_cd
print(count)
