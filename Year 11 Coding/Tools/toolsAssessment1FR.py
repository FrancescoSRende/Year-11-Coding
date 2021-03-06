#Description
#Parameters
#Return

#Pre-Conditions
#Post-Conditions

#remember to use terminology like instance method in the video
#ensure you demonstrate your knowledge of the terminology
#don't forget pre/post conditions




#Description: this function takes a list of integers and returns the sum of every element that is divisible by 3
#Parameters: list of integers
#Returns: integer (sum of elements divisible by 3)

def findModSum1(lst):

    l = []
    for i in range(0,len(lst),1):
        if lst[i] % 3 == 0:
            l.append(lst[i])

    sum = 0
    for i in range(0,len(l),1):
        sum = sum + l[i]

    return sum

print('findModSum1')
print(findModSum1([3,4,6,7,9]))



print("")




#Description: this function takes a list of integers and two integers and returns the sum of every element between the two integers
#Parameters: list of integers
#Returns: integer (sum of elements between a and b)

def findModSum2(lst,a,b):
    max = a
    min = b
    if a < b:
        max = b
        min = a

    l = []

    for i in range(0,len(lst),1):
        if lst[i] > min and lst[i] < max:
            l.append(lst[i])

    sum = 0
    for i in range(0,len(l),1):
        sum = sum + l[i]

    return sum

print('findModSum2')
print(findModSum2([3,4,6,7,9], 1, 8))



print("")




#Description: this function takes a list of integers and two integers and returns the sum of every element divisible by both integers
#Parameters: list of integers
#Returns: integer (sum of elements divisible by a and b)

def findModSum3(lst,a,b):
    
    l = []

    for i in range(0,len(lst),1):
        if lst[i] % a == 0 and lst[i] % b == 0:
            l.append(lst[i])

    sum = 0
    for i in range(0,len(l),1):
        sum = sum + l[i]

    return sum

print('findModSum3')
print(findModSum3([3,4,6,7,12], 1, 3))



print("")





#Description: this function takes a list of floats and returns the sum of all the digits of the floats
#Parameters: list of floats
#Returns: integer (sum of every digit)

def findModSum4(lst):

    total = 0
    for i in range(0,len(lst),1):
        lst[i] = str(lst[i]).replace(".", "")
        #This collapses the string by removing the dots
        n = 0
        while n < len(lst[i]):
            total = total + int(lst[i][n])
            #lst[i][n] first finds the element of lst at index i then finds the character
            #at index n
            n = n + 1

    return total

print('findModSum4')
print(findModSum4([1.2, 2.32, 10.3]))



print("")




#Description: this function takes a string and returns it in reverse
#Parameters: string
#Returns: string (original string but backwards)

def reverseWordA(a):

    result = ""
    for i in range(0,len(a),1):
        result = result + a[len(a)-1-i]

    return result

print('reverseWordA')
print(reverseWordA("cat"))



print("")




#Description: this function takes a list of strings and returns a string of every word in the list backwards
#Parameters: list of strings
#Returns: string (every element, backwards, concatenated)

def reverseWordB(lst):

    result = ""
    for i in range(0,len(lst),1):
        for n in range(0,len(lst[i]),1):
            result = result + lst[i][len(lst[i])-1-n]

    return result

print('reverseWordB')
print(reverseWordB(["cat", "dog"]))



print("")