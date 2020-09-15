def isEven(a):
	if a % 2 == 0:
		return True
	else:
		return False


print("")
print('isEven')
print('Is 0 even?')
print(isEven(0))
print('Is 15 even?')
print(isEven(15))


print("")



def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

print('missingChar')
print(missing_char('Converge', 3))
print(missing_char('metal', 2))


print("")



def base2To10(str):
	total = 0
	i = 1
	while i < len(str):
		total = total + int(str[len(str)-i])*2^(i-1)
		i = i + 1
	return total

print('base2To10')
print(base2To10('101'))
print(base2To10('111111'))



print("")




def sumDigits(a):
	total = 0
	i = 0
	a = str(a) #casting is the process of changing type
	#alternatively: for i in range (0, len(a), 1):
	#count (0, the number we start at), check (len(a), the maximum value, change (1, the value we increment by))

	while i < len(str(a)):
		total = total + int(a[i])
		i = i + 1
	
	return total

print('sumDigits')
print(sumDigits(45))
print(sumDigits(101))
print(sumDigits(3))


print("")



def sumDigitsVersion2(a):
	total = 0

	while (a > 0):
		total = total + a % 10
		a = a // 10 #integer division, which divides and chops off the decimals
		# 367 / 10 = 36.7, but 367 // 10 = 36
	
	return total

print('sumDigitsVersion2')
print(sumDigitsVersion2(45))
print(sumDigitsVersion2(101))
print(sumDigitsVersion2(3))



print("")



def scaleElementsA(a,b):
	i = 0
	for i in range (0, len(b), 1):
		b[i] = b[i] * a
	return b


print('scaleElementsA')
print(scaleElementsA(2, [1,2,3]))
print(scaleElementsA(3, [4,3]))
print(scaleElementsA(0, [4,5,6,7]))



print("")



def scaleElementsB(a,b):
	i = 0
	z = []
	for i in range (0, len(b), 1):
		z.append(b[i] * a)
		z = z
	return z


print('scaleElementsB')
print(scaleElementsB(2, [1,2,3]))
print(scaleElementsB(3, [4,3]))
print(scaleElementsB(0, [4,5,6,7]))



print("")





def addStringsSmallLarge(a,b):
	if len(a) < len(b):
		return b + a
	else:
		return a + b


print('addStringsSmallLarge')
print(addStringsSmallLarge('aaa', 'bb'))
print(addStringsSmallLarge('aaa', 'bbbb'))
print(addStringsSmallLarge('aaa', 'bbb'))



print("")