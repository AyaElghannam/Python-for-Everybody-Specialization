#Assignment 8.4
fname = input("Enter file name: ")

try:
	fh = open(fname)
except:
    print('Error, could not open: ',fname)
    quit()
    
lst = list()
for line in fh:
    line = fh.read()
    line = line.split()
    for w in line:
    	if w not in lst:
        	lst.append(w)
lst.sort()
print(lst)


#Assignment 8.5
fname = input("Enter file name: ")
if len(fname) < 1:
   fname = "mbox-short.txt"
    
try:
	fh = open(fname)
except:
    print("Error, Invalid Input")
    quit()
    
lst = list()
count = 0
for line in fh:
    line = line.strip()
    if line.startswith('From '):
       lst = line.split()
       print (lst[1])
       count = count + 1
print("There were", count, "lines in the file with From as the first word")
