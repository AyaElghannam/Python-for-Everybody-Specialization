#Assignment 7.1
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
	line = line.rstrip()
inp = fh.read()
Out = inp.upper()
print(Out)



#Assignment 7.2
fileName = input("Enter file name:\t")
try:
    fileHand = open(fileName)
except:
    print('File could not be found:', fileName)
    quit()

total = 0
count = 0
for line in fileHand :
    if line.startswith('X-DSPAM-Confidence') :
        line = line[line.find('0'):].rstrip()
        total += float(line)
        count += 1
print('Average spam confidence:', total/count)
