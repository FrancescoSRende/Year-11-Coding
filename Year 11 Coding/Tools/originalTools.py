#Description
#Parameters
#Return

#Pre-Conditions
#Post-Conditions


#Description: this function takes an integer and finds and returns its factors
#Parameters: integer
#Returns: a list of ints
#Precondition: number is an int, not a string

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




#Description: this function takes an integer, finds all the numbers beneath it that are
#divisible by 3 or 5 and returns their sum
#Parameters: int
#Returns: int (sum of the numbers divisible by 3 or 5 less)
#Precondition: a is an int, not a float or string

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




#Description: this function takes an integer and returns the sum of all even fibonacci numbers
#less than said integer
#Parameters: int
#Returns: int (sum of the even fibonacci numbers less than the int)
#Precondition: a is an int, not a float or string

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




#Description: this function takes an integer and returns a list of all fibonacci numbers less than the integer
#Parameters: integer
#Returns: a list of integers
#Precondition: a is an integer

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




#Description: this function takes a number and returns true if it is prime, and false if it is not
#Parameters: int
#Returns: boolean
#Precondition: a is an int

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




#Description: this function takes a number and returns true if it is semiprime, and false if it is not
#Parameters: int
#Returns: boolean
#Precondition: a is an int

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





#Description: this function takes an int and returns its largest factor
#Parameters: int
#Returns: int
#Precondition: a is an integer

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
print(projEuler3(578))



print("")





#Description: this function takes two integers and returns an integer which is equal to the larger of the
#original integers plus the difference between the two integers
#Parameters: two ints
#Returns: one int
#Precondition: a and b are ints

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




#Description: this function takes a string and returns true if it only contains the letters I, O, S, H, Z, X or N, and false otherwise
#Parameters: a string
#Returns: a boolean

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




#Description: this function takes a string and returns true if it has double letters (capitals =/= lowercase)
#Parameters: a string
#Returns: a boolean

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





#Description: this function takes a text file name and a list and appends every even element
#to the file then returns a list with each line of the file as an element
#Parameters: string, list
#Returns: list with each line of the text file
#Preconditions: list contains numbers, whether ints or strings

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





#Description: this function takes a hexadecimal number and converts it to base 2
#Parameters: string (hex number)
#Returns: string (base 2 number)
#Precondition: only hexadecimal characters are used

def hexToBase2(s):

    #parallel lists
    HEX = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    BIN = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

    result = ""

    
    for n in range(0,len(s),1):
        for i in range(0,len(HEX),1):
            if HEX[i] == s[n]:
                result = result + BIN[i] + " "
                break #this means that once we find one result, we break out of the
                #most immediate loop structure


    '''for n in range(len(s),-1,-1):
        for i in range(0,len(HEX),1):
            if HEX[i] == s[n]:
                result = BIN[i] + result'''
    #the same loop as above but done in reverse

    '''for i in range(0,len(result),1):
        if (result == "0"):
            return result
        elif (result[i] == "1"):
            return result[i:]'''
    #optional code to remove beginning zeros
    
    return result

print('hexToBase2')
print(hexToBase2('F'))



print("")




#Description: this function takes a binary number and converts it to hexadecimal
#Parameters: string (binary number)
#Returns: string (hexadecimal) number)
#Precondition: only uses '0' and '1'

def base2ToHex(s):

    HEX = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    BIN = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

    result = ""

    extra = len(s) % 4

    for i in range(0,4-extra,1):
        s = "0" + s
    
    for n in range(0,len(s),4):
        for i in range(0,len(BIN),1):
            if BIN[i] == s[n:n+4]:
                result = result + HEX[i]

    if result[0] == "0" and result != "0":
        result = result[1:]
    
    return result

print('base2ToHex')
print(base2ToHex('1111'))



print("")