#Description: this takes two lists of strings and adds the strings at the same index together to create a new list of strings.
#If one list is longer than the other, then the none-paired indices will be added to the new list
#Parameters: list (of strings) a, list (of strings) b
#Returns: list of strings
#Postcondition: two passed lists remain unchanged

def mergeStrings(a,b):

    result = []

    #Two separate cases, one where the lists have different lengths (the more complicated case)
    #and one where they have the same length (the easier case)

    if len(a) != len(b):
        
        big = a
        small = b

        if len(b) > len(a):
            big = b
            small = a

        i = 0

        while i < len(small):
            result.append(big[i] + small[i])
            i = i + 1

        for x in range(len(small),len(big),1):
            result.append(big[x])

    else:
        for i in range(0,len(a),1):
            result.append(a[i] + b[i])

    return result

    
    

print('mergeStrings')
print(mergeStrings(["cat","dog","fish"],["one"]))
print(mergeStrings(["red","green"],["six","seven"]))
print(mergeStrings([],["one","two","three"]))



print("")







#Description: this function takes a list of names and a string with a name and looks to see if that name is in the list (ie. if the person was present)
#It returns "present" if the person's name appears once, "absent" if their name does not appear and "tampering has occurred" if the person's name appears more than once
#Parameters: list lst, string name
#Returns: string ("present", "absent" or "tampering has occurred")
#Precondition: both list and string are in lowercase
#Postcondition: passed list remains unchanged

def attendance(lst,name):

    if name == "":
        return "tampering has occurred"

    check = 0

    for i in range(0,len(lst),1):
        if lst[i] == name:
            check = check + 1

    if check == 0:
        return "absent"
    elif check == 1:
        return "present"
    else:
        return "tampering has occurred"
    

print('attendance')
print(attendance(["john","frank","lisa"], "edward"))
print(attendance(["john","frank","edward","lisa"], "edward"))
print(attendance(["edward","john","frank","edward","lisa"], "edward"))
print(attendance([], "edward")) #Important 'null' test case
print(attendance(["edward"], "edward"))
print(attendance(["john","frank","lisa"], "")) #Other 'null' test case



print("")








#Description: this function takes a string and an integer, which is matched with an index in a list of genre names, which is then matched with a corresponding 'quintessential' band for said genre in the dictionary
#The function checks if the string matches the corresponding band name in the dictionary
#Note that both num and band are assigned to values after the function has begun
#Furthermore, a two-dimensional list is used to ensure that a valid band name is input for each genre
#Parameters: integer num, string band
#Returns: string
#Postcondition: passed list and dictionary remain unchanged

def quintessentialBands():

    genres = ["metalcore", "melodic metalcore", "blackened death metal", "progressive metal"]

    quintBands = {
        "metalcore": "converge",
        "melodic metalcore": "killswitch engage",
        "blackened death metal": "behemoth",
        "progressive metal": "opeth"

    }

    generalBands = [["converge", "norma jean", "parkway drive"], ["killswitch engage", "poison the well", "as i lay dying"], ["behemoth", "belphegor", "skeletonwitch"], ["opeth", "tool", "dream theater"]]

    print("Here are the genres available to you: \n")
    for x in quintBands:
        print(x)

    num = int(input("Input the index of the genre you've chosen: "))
    
    if isinstance(num, int) == False:
        return "Invalid index, try again."

    if num >= len(quintBands):
        return "invalid input, too high"

    band = input("Now input a band name, in all lowercase, if you could: ")
    band = band.lower()

    genre = genres[num]

    check = 0

    for i in range(0,len(generalBands[num]),1):
        if band == generalBands[num][i]:
            check = check + 1
    
    if check == 0:
        return band + "? are you sure that's an actual " + genre + " band?"

    quintBand = quintBands.get(genre)

    if quintBand == band:
        return "great taste in music, my dude. " + quintBand + " is an incredible " + genre + " band."
    else:
        return "your taste in music is lacking, old chum. sure " + band + " is a good " + genre + " band, but they're nothing compared to " + quintBand

    
    

print('quintessentialBands')
print(quintessentialBands())



print("")