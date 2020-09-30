#Description
#Parameters
#Return

#Pre-Conditions
#Post-Conditions


#remember to use terminology like instance method in the video
#ensure you demonstrate your knowledge of the terminology
#don't forget pre/post conditions

def readFileToList(name):

	file = open(name,"r")

	l = []

	for line in file: 
		l.append(line.strip())
	
	return l


print('readFileToList')
print(readFileToList("toolsText.txt"))



print("")





def writeListToFile(name, lst):

	file = open(name, "w")

	for i in range(0, len(lst), 1):
		file.write(str(lst[i])+"\n")
	
	file.close()
	file = open(name,"r")

	l = []

	for lst in file: 
		l.append(lst.strip())
	
	return l


print('writeListToFile')
print(writeListToFile("toolsText.txt", ['1', '2', '3', 'the violation of the Geneva Convention']))



print("")





def appendListToFile(name, lst):

	file = open(name, "a")

	for i in range(0, len(lst), 1):
		file.write(str(lst[i])+"\n")

		'''write() can both write and append, depending on if the file = open() function
		has "a" (for append) or "w" (for write)'''
		
	file.close()
	file = open(name,"r")

	l = []

	for lst in file: 
		l.append(lst.strip())
	
	return l


print('appendListToFile')
print(appendListToFile("toolsText.txt", ['the erosion of the institution of state sovereignty', 'the knowledge that seeking the favor of another means the murder of self']))



print("")







def appendSortedListToFile(name, lst):

	file = open(name, "a")

	for i in range(0, len(lst), 1):
		lst[i] = int(lst[i])

	lst.sort()	

	for i in range(0, len(lst), 1):
		file.write(str(lst[i])+"\n")
	
	file.close()
	file = open(name,"r")

	l = []

	for lst in file: 
		l.append(lst.strip())
	
	return l


print('appendSortedListToFile')
print(appendSortedListToFile("toolsText.txt", ['9','4','1729','12']))



print("")