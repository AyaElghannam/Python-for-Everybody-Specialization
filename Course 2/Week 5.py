#Assignment 9.4

name = input("Enter file:")
if len(name) < 1 :
   name = "mbox-short.txt"
    
try:
    handle = open(name)
except:
    print('Error , File Can not be opened')
    exit()
    
Req = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        Req[words[1]] = Req.get(words[1] , 0) + 1

proEmail = None
proCount = None
for key, value in Req.items() :
    if proCount is None or value > proCount :
        proEmail = key
        proCount = value

print(proEmail, proCount)

	
