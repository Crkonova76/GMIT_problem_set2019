# Martina Crkonova, 2019-03-01
# Problem Set 4 2019, Python collatz, Programming and Scripting, GMIT


# User input assigned to variable i
i = int ( input ("Please enter a positive integer: "))

# Empty collection 
collection = []

# Simple validation to verify if the input contains positive integer
if i < 0:
    print (" Entered integer ", i ," is negative number . Input a positive integer next time.")

# Local variable to assigne initial value used in print function   
initial = i

# While loop to be true until i is bigger than 1
while i > 1:
    
    # If reminder of i is zero, divide i by 2
    # The output append to collection
    if i % 2 == 0:
        i = i// 2 
        collection.append(i)
    # If reminder of i is one, provide operation below
    # Add result to the collection
    elif i % 2 == 1:
        i = i * 3 + 1
        collection.append(i)
# Print output of the operation
print ("An initial positive integer is {} and the output is: {}" .format(initial,collection))


