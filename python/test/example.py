largest = None
smallest = None
num = 0
total = 0
smallestv = int(smallest)
largestv = int(largest)
while True:
    value = input("Enter a number: ")
    if value == "done":
    	break  
    try:
    	rlValue = int(value)
    except:
    	print('Invalid input')
    if rlValue > largestv:
        largestv = rlValue
    if smallestv is None:
        smallestv = rlValue
    elif rlValue < smallestv:
        smallestv = rlValue 
    
    
    

print("Maximum is", largestv)
print("Minimum is", smallestv)