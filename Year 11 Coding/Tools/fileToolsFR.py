#Description
#Parameters
#Return

#Pre-Conditions
#Post-Conditions


#remember to use terminology like instance method in the video
#ensure you demonstrate your knowledge of the terminology
#don't forget pre/post conditions






#Description: this function takes a string, specifically the name of a text file and
#returns a list with each line in the function as a separate element of the list
#Parameters: a string with the name of a text file
#Returns: a list with with each line in the function as a separate element of the list
#Precondition: the string is a valid name of a text file


def readFileToList(name):

	file = open(name,"r")

	l = []

	for line in file: 
		l.append(line.strip())
	
	return l


print('readFileToList')
print(readFileToList("toolsText.txt"))



print("")








#Description: this function takes a text file name and a list and writes each element of the
#list to the file on a new line, then returns a list with each line of the file as an element
#Parameters: string (file name), list
#Returns: list with each line of the text file


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





#Description: this function takes a text file name and a list and appends each element of the
#list to the file on a new line, then returns a list with each line of the file as an element
#Parameters: string (file name), list
#Returns: list with each line of the text file

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





#Description: this function takes a text file name and a list and sorts the list before
#appending each element of the list to the file on a new line, then returns a list with
#each line of the file as an element
#Parameters: string (file name), list
#Returns: list with each line of the text file

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