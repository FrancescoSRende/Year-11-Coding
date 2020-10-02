#Description
#Parameters
#Return

#Pre-Conditions
#Post-Conditions


#Description: this function takes an integer and finds and returns its factors
#Parameters: integer a
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
#Parameters: int a
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
#Parameters: int a
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
#Parameters: integer a
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
#Parameters: int a
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
#Parameters: int a
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





#Description: this function takes an int and returns its largest prime factor
#Parameters: int a
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
#Parameters: two ints, a and b
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
#Parameters: string a
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
#Parameters: string a
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
#Parameters: string name, list lst
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
#Parameters: string (hex number) s
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
#Parameters: string (binary number) s
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





#Description: this function takes the three constants of a quadratic equation (a,b,c) and returns the zeroes of said quadratic (unless they are imaginary)
#Parameters: three ints a, b and c
#Returns: 1 or 2 ints or a string if the zeroes are imaginary

def solveQuadratic(a,b,c):

    a = float(a)
    b = float(b)
    c = float(c)

    if b**2 >= 4*a*c:

        determinant = ( (b**2) - (4*a*c) ) ** 0.5

        top_add = -b + determinant

        top_subtract = -b - determinant

        bottom = 2*a

        zero_1 = top_add / bottom
        zero_2 = top_subtract / bottom
    

        if zero_1 == zero_2:
            return zero_1
        else:
            print (zero_1)
            print (zero_2)
            return
    
    else:
        return "imaginary solutions"
    

print('solveQuadratic')
print(solveQuadratic(1,1,-1))



print("")




#Description: this function takes a number and returns the greatest possible product using a certain number of its digits
#Parameters: two ints num and a
#Returns: int

def projEuler8ish(num,a):

    a = str(a)

    check_total = 0
    check_9 = 0
    check_8 = 0
    check_7 = 0

    product = 0


    for i in range(0,len(a),1):
        if a[i] == '9':
            check_9 = check_9 + 1
            check_total = check_total + 1

    
    if check_total <= num:    
        for i in range(0,len(a),1):
            if a[i] == '8':
                check_8 = check_8 + 1
                check_total = check_total + 1


        if check_total <= num:

            for i in range(0,len(a),1):
                if a[i] == '7':
                    check_7 = check_7 + 1
                    check_total = check_total + 1


            if check_total <= num:

                for i in range(0,len(a),1):
                    if a[i] == '6':
                        check_6 = check_6 + 1
                        check_total = check_total + 1

                



    product = (9**check_9) * (8**check_8) * (7**check_7)

    return product
    

print('projEuler8ish')
print(projEuler8ish(13,7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450))



print("")






#Description: this function takes an int and returns the sum of all primes less than it
#Parameters: int a
#Returns: int


#NEEDS WORK
def sumPrimes(a):

    primes = []
    check = 0

    for x in range(2,a,1):
        half_kinda = round(float(x)/2) + 1
        for i in range(2,half_kinda,1):
            if x % i == 0 and x != i:
                check = check + 1

        print(str(x) + ", " + str(check))
        
        if check == 0:
            primes.append(x)

    return primes
    

print('sumPrimes')
print(sumPrimes(17))



print("")