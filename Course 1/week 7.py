Largest = None
Smallest = None
while True:
    num = input("Enter a Number: ")
    if (num == 'done'):
        break
    else:
        try:
            number = float(num)
        except:
            print("Invalid input")
            continue
        #Smallest Value
        if Smallest is None:
            Smallest = number
        elif (number < Smallest):
            Smallest = number
        #Largest Value
        if Largest is None:
            Largest = number
        elif (number > Largest):
            Largest = number

print("Maximum is", int(Largest))
print("Minimum is", int(Smallest))
