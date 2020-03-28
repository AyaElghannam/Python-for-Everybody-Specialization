##Assignment 10.2
name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"

try:
	handle = open(name)
except:
    print('Error, File can not be opened')
    exit()

dct = dict()

for line in handle:
    if line.startswith('From '):
        line = line.split()
        time = line[5].split(':')
        dct[time[0]]= dct.get(time[0] , 0) + 1
           
for v, k in sorted(dct.items()):
    print (v, k)
