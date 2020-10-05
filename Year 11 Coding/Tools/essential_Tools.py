#Description: this function takes an integer in base 10 and returns a string in base 2
#Parameters: int a
#Returns: string

def base10ToBase2(a):
	
	result = ""

	while a > 0:
		result = str(a % 2) + result
		a = a // 2

	return result


print('base10ToBase2')
print(base10ToBase2(0))
print(base10ToBase2(3))
print(base10ToBase2(104))



print("")





#Description: this function takes a number in base 2 string format and returns the corresponding integer in base 10
#Parameters: string num
#Returns: integer
#Precondition: string only contains '0's and '1's

def base2ToBase10(num):
	total = 0
	i = 1
	while i < len(num):
		total = total + int(str[len(num)-i])*2^(i-1)
		i = i + 1
	return total

print('base2ToBase10')
print(base2ToBase10('101'))
print(base2ToBase10('111111'))



print("")





#Description:  This function takes a string, representing a binary value, and if s is invalid the function returns "-1"
#Parameter: String s
#Return: String

def base2ToHex(s):

	result = ""

	DIC = { "0000":"0",
			"0001":"1",
			"0010":"2",
			"0011":"3",
			"0100":"4",
			"0101":"5",
			"0110":"6",
			"0111":"7",
			"1000":"8",
			"1001":"9",
			"1010":"A",
			"1011":"B",
			"1100":"C",
			"1101":"D",
			"1110":"E",
			"1111":"F"}

	while (len(s)%4 != 0):
		s = "0" + s
	


	for i in range(0, len(s),4):
		v = s[i: i + 4]
		result = result + DIC[v]
#Indexes for dictionaries take an input value, not an index number
#If DIC was a list, then v would have to be a number
#But since DIC is a dictionary, v can be a string
#DIC['0101'] returns the corresponding hex value (on the right) for '0101', which is '5'

	return result


print('base2ToHex')
print(base2ToHex("1011110101")) #2 F 5
print(base2ToHex("1110111110110")) #1 D F 6


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






#Description: this function takes an integer and returns the sum of all of its digits
#Parameters: integer a
#Returns: integer (sum of digits)

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





#Description: this function takes a list of integers and returns the sum of every element that is divisible by 3
#Parameters: list of integers lst
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
#Parameters: list of integers lst, integers a and b
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
#Parameters: list of integers lst, integers a and b
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
#Parameters: list of floats lst
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
#Parameters: string a
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
#Parameters: list of strings lst
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