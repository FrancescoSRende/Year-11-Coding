def isEven(a):
	if a % 2 == 0:
		return True
	else:
		return False

print('Is 0 even?')
print(isEven(0))
print('Is 15 even?')
print(isEven(15))


def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

print(missing_char('Converge', 3))
print(missing_char('metal', 2))



def base2To10(str):
	total = 0
	i = 1
	while i < len(str) - 1:
		total = total + int(str[len(str)-i])*2^(i-1)
		i = i + 1

print(base2To10('101'))
print(base2To10('111111'))