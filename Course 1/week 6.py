##On Using Functions
##On Using Try Except
def computepay(h, r):

    if (h <= 40):
        fees = h*r
    else:
        x = h - 40
        fees = (x*r*1.5) + (40*r)
    return fees

hours = input("Enter Hours:")
hrs = float(hours)
Pay = input("Enter the Rate: ")
P_R = float(Pay)

try:
    hrs = float(hours)
    P_R = float(Pay)
except:
    print("Error, Enter a Numeric Value")

p = computepay(hrs, P_R)
print("Pay",p)
