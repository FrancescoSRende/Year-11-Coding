import requests
import json
from pprint import pprint

#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//API_Keys//fixerkey.txt","r")
#each ..// moves up one 'level' (ie. from tools to Year 11 Coding)


#read is an instance method for file objects
#instance method means it can only work if it is being called with a variable
key = file.read()


#get is a static/class method in the request module
#get is being called with the requests module and does not require a variable to work
resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)


#Converts response to JSON
#json is an instance method, here being called with the variable 'data'
data = resp.json()


pprint(data)
#pprint uses 'pretty print' to print the data in a much more organized manner

print(data["base"])


for keys in data["rates"]:
    print("Currently, 1 " + data["base"] + " is equal to " + str(data["rates"][keys]) + " " + keys)