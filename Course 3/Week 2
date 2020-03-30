import re

FileName = "Actual.txt"

try:
    handle = open(FileName)
except:
    print('Error, File can not be opened')
    quit()

#Req is the list of Numbers in line
NumInLine = list()
#list of all numbers in .txt file
NumInFile = list()
#Sum of Numbers Extracted
sigma = 0

#Extract Numbers in Each line
for line in handle:
    NumInLine = (re.findall('[0-9]+' , line))
    #Add the numbers in the lines to a list
    for w in NumInLine:
        if w != None:
            NumInFile.append(w)

for x in NumInFile:
    sigma = sigma + int(x)

print(NumInFile)
print (sigma)
