#this one takes a band name and a genre, then looks at the band's wikipedia page
#to tell you if the band is that genre

#pre-condition: string inputs, valid band and genre names

def findFactors(a):
    l = []
    halfish = round(float(a)/2)
    for i in range(1,halfish + 1,1):
        if a % i == 0:
            l.append(i)
    
    l.append(a)

    return l

print('findFactors')
print(findFactors(783))



print("")





def projEuler1(a):
    l = []
    sum = 0
    for i in range(3,a,1):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
    
    for i in range(0,len(l),1):
        sum = sum + l[i]

    return sum

print('projEuler1')
print(projEuler1(1000))



print("")



def projEuler2(a):

    fibonacci = [1,2]
    sum = 0

    while fibonacci[-1] < a:
        f_i = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(f_i)
    
    del fibonacci[-1]

    for i in range(0,len(fibonacci),1):
        if fibonacci[i] % 2 == 0:
            sum = sum + fibonacci[i]

    print(fibonacci)

    return sum

print('projEuler2')
print(projEuler2(4000000))



print("")




def fibonacciGenerator(a):

    fibonacci = [1,2]
    sum = 0

    while fibonacci[-1] < a:
        f_i = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(f_i)
    
    del fibonacci[-1]

    return fibonacci

print('fibonacciGenerator')
print(fibonacciGenerator(700))



print("")



def isPrime(a):
    halfish = round(float(a)/2)
    check = 0
    for i in range(2,halfish + 1,1):
        if a % i == 0:
            check = check + 1
        
    if check > 0:
        return False
    else:
        return True
    

print('isPrime')
print(isPrime(31))



print("")





def isSemiPrime(a):
    halfish = round(float(a)/2)
    check = 0
    for i in range(2,halfish + 1,1):
        if a % i == 0:
            check = check + 1
        
    if check == 2:
        return True
    else:
        return False
    

print('isSemiPrime')
print(isSemiPrime(32))



print("")




def projEuler3(a):

    factors = []
    halfish = round(float(a)/2)
    for i in range(1,halfish + 1,1):
        if a % i == 0:
            factors.append(i)
    
    prime_factors = []
    check = 0
    for x in range(0,len(factors),1):
        half_kinda = round(float(factors[x])/2)
        for i in range(2,half_kinda + 1,1):
            if factors[x] % i == 0:
                check = check + 1
        
        if check == 0:
            prime_factors.append(factors[x])

    return prime_factors[-1]
    

print('projEuler3')
print(projEuler3(625))



print("")



def nextInLine(a,b):
    max = a
    min = b
    if a < b:
        max = b
        min = a
    
    diff = max - min

    return max + diff

print('nextInLine')
print(nextInLine(5,9))



print("")



def rotatingLetters(a):
    check = 0
    for i in range(0,len(a),1):
        if a[i] != 'I' and a[i] != 'O' and a[i] != 'S' and a[i] != 'H' and a[i] != 'Z' and a[i] != 'X' and a[i] != 'N':
            check = check + 1
        
    if check == 0:
        return "YES"
    else:
        return "NO"

print('rotatingLetters')
print(rotatingLetters('SHINS'))



print("")




def hasDoubleLetters(a):
    check = 0
    for i in range(1,len(a),1):
        if a[i] == a[i-1]:
            check = check + 1

    if check > 0:
        return True
    else:
        return False

print('hasDoubleLetters')
print(hasDoubleLetters('oooo'))



print("")





def appendEvenNumbers(name, lst):

    file = open(name, "a")

    for i in range(0, len(lst), 1):
        if int(lst[i]) % 2 == 0:
            file.write(str(lst[i])+"\n")

	#write() can both write and append, depending on if the file = open() function
	#has "a" (for append) or "w" (for write)
		
    file.close()
    file = open(name,"r")

    l = []

    for lst in file: 
        l.append(lst.strip())
	
    return l


print('appendEvenNumbers')
print(appendEvenNumbers("toolsText.txt", ['3', 4, '6', 7]))



print("")