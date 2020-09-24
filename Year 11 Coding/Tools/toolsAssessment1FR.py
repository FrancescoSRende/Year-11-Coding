#remember to use terminology like instance method in the video
#ensure you demonstrate your knowledge of the terminology
#don't forget pre/post conditions

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


def findModSum4(lst):

    total = 0
	for i in range(0,len(lst),1):
        lst[i] = str(lst[i])
        lst[i] = lst[i].replace(".", "")
        #This collapses the string by removing the dots

        while n < len(lst[i]):
		    total = total + int(lst[n])
		    n = n + 1
            
    return total

print('findModSum4')
print(findModSum4([1.2, 2.32, 10.1]))



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