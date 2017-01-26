# file name (note same folder as the python program)
inputfileName = "biglist.txt"
# open the file name above - what does the 'r' signify?
f = open(inputfileName, 'r')

# this code will read the whole textfile into a list
# with each line of the text file as an element of the list
listofWords = f.read().splitlines()

print("length of list", len(listofWords))

idx = len(listofWords)-1
print("idx",idx)

import random
print("length of list", len(listofWords))
randomNumber = random.randint(0,len(listofWords)-1)
print("random element", randomNumber)
print(listofWords[randomNumber])
for idx in range(0,len(listofWords)):
    print(str(idx), " ", listofWords[idx])

