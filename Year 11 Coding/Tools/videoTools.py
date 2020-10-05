#SIMPLE TOOL

#Description: this function takes an integer and returns the sum of all of its digits
#Parameters: integer
#Returns: integer (sum of digits)


#Declaring a function with a passed variable, an integer a
def sumDigits(a):

    #Declares a variable called total and initializes it to 0
	total = 0

    #Declares a variable called i and initializes it to 0
	i = 0
    
    #Casts the variable a (an integer) to a string so each digit can be accessed individually
	a = str(a) #casting is the process of changing type
    #Since a is essentially a primitive type, we can modify it within the function
    #Without changing it outside the function

	#alternatively: for i in range (0, len(a), 1):
	#count (0, the number we start at), check (len(a), the maximum value, change (1, the value we increment by))

    #This loops from 0 to the length of the now-string variable a
    while i < len(str(a)):

        #This takes each digit of a (ie. a at index i), casts it back to an integer, and adds it to the total
        total = total + int(a[i])

        #This adds 1 to i to move on to the next digit
        i = i + 1
	
    #This returns the total (the sum of all of a's digits)
	return total

print('sumDigits')
print(sumDigits(45))
print(sumDigits(101))
print(sumDigits(3))


print("")








#COMPLEX TOOL

#Description: this function takes an integer greater than 1 and returns its largest prime factor
#Parameters: integer a, greater than 1
#Returns: integer

#Declaring a function with a passed variable, an integer a
def projEuler3(a):

    #Declares a variable called factors and initializes it to an empty list
    factors = []

    #Loops from 1 to a, incrementing by one each time
    for i in range(1,,1):

        #Conditional statement: is a, our integer input, divisible by i? This checks
        #if i is a factor of a
        if a % i == 0:

            #If i is a factor of a, it is appended to the list 'factors'
            factors.append(i)
    

    #Declares a variable called prime_factors and initializes it to an empty list
    prime_factors = []

    #Declares a variable called check and initializes it to 0
    check = 0

    #Loops through every element in the list 'factors', incrementing the index by 1 each time
    for x in range(0,len(factors),1):

        #Declares a variable called half_kinda and initializes it to an integer equal to
        #the element of factors at index x divided by 2 (rounded up if it is an odd number)
        #The reason for this is that a number's largest factor (excluding the number itself) cannot be larger than
        #half of the number, so it is unnecessary to check every number beneath it
        #Instead, this checks every number less than or equal to half of the number
        half_kinda = int(round(float(factors[x])/2))

        #Loops through every number from 2 to half_kinda + 1, incrementing by one each time
        #1 is not a prime number, so it is skipped
        for i in range(2,half_kinda,1):

            #Conditional statement: is the element of factors at index x divisible by i?
            if factors[x] % i == 0:

                #If it is, the check variable is incremented by 1. Check indicates how many factors
                #factors[x] has
                check = check + 1
        
        #Conditional statement: is the check variable equal to zero (in other words,
        #is factors[x] prime?
        if check == 0:

            #If check = 0 (and factors[x] is prime), factors[x] is appended to the list
            #prime_factors and is thus a prime factor of a
            prime_factors.append(factors[x])

    #This returns the element of prime_factors at index -1, in other words, the last element
    #of the list, which is the largest prime factor of the passed variable a
    return prime_factors[-1]
    

print('projEuler3')
print(projEuler3(578))
print(projEuler3(79))
print(projEuler3(1729))