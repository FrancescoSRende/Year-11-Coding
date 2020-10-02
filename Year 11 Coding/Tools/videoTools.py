#SIMPLE TOOL










print('')



#COMPLEX TOOL

#Description: this function takes an integer and returns its largest prime factor
#Parameters: integer a
#Returns: integer

#Declaring a function with a passed variable, an integer a
def projEuler3(a):

    #Declares a variable called factors and initializes it to an empty list
    factors = []

    #Declares a variable called halfish and initializes it to an integer equal to a
    #divided by 2 (rounded up if a is an odd number)
    #The reason for this is that a number's largest factor cannot be larger than
    #half of the number, so it is unnecessary to check every number beneath a
    #Instead, this checks every number less than or equal to half of a
    halfish = round(float(a)/2)

    #Loops from 1 to halfish + 1 (a / 2, rounded up, + 1), incrementing by one each time
    for i in range(1,halfish + 1,1):

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
        #The reason for this is that a number's largest factor cannot be larger than
        #half of the number, so it is unnecessary to check every number beneath it
        #Instead, this checks every number less than or equal to half of the number
        half_kinda = round(float(factors[x])/2)

        #Loops through every number from 2 to half_kinda + 1, incrementing by one each time
        #1 is not a prime number, so it is skipped
        for i in range(2,half_kinda + 1,1):

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