 710 Bytes
  
#ASSIGNMENT 3.1
##On Using Functions as float and int
hours = input("Enter Hours:")
h = float(hours)
Pay = input("Enter Pay Rate:")
P = float(Pay)
try:
    h = float(hours)
    P = float(Pay)
except:
    print("Error, please Enter numeric input")

if (h <= 40):
    print(h * P)
else:
    # x is the Number of Hours Above 40
    x = h - 40
    print((1.5 * x * P) + (40 * P))
    
  
  
  
#ASSIGNMENT 3.3
##On Looping Using elif
Score = input("Enter Score: ")
S = float(Score)
try:
    S = float(Score)
except:
    print("ERROR, Enter numeric score")
if(S > 1):
    print("Error, Out of Range")
elif (S > 0.9):
    print('A')
elif(S >= 0.8):
    print('B')
elif(S >= 0.7):
    print('C')
else:
    print('F')
