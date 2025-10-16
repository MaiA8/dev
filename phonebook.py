from cs50 import get_string
# user = {
#     "name":"Mai",
#     "age":26
#     "country":"Egypt"
# }
# print( user['name'] )

# people = {
#     "Mai":"01000",
#     "Medo":"12345"
# }
# # "key":"value"
# name = get_string("name: ")
# if name in people:
#     print(f"Number: {people[name]}")
# r = only read
# w = only write (clear old data)
# a = append "only write add and save old data"
# r+ = read and write
# w+ = read and write  and create and clear old data
# open file, do what you want, close file
# a+ = read and write and same as a

# file = open("test.txt","a")

# #data = file.readable()
# #data = file.read()
# #print(data)
# print(file.readable())
# file.close()


# with open("test.txt","r") as file:
#     file.read()

import csv

file = open("phonebook.csv","a")

name = input("name: ")
number = input("number: ")

#csv.writer(file).writerow()

writer = csv.writer(file)
writer.writerow([name,number])
file.close()