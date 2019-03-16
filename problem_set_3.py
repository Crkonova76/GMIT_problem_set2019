# Martina Crkonova, 2019-02-28
# Problem Set 2019, Python divisors, Programming and Scripting, GMIT
# Program printing all numbers from range 1,000 and 10,000 that are divisible by 6 but not 12

# The For loop, variable i is assigned the range of numbers between 1000 and 10000


# Print function just displayes the description of the output
print("Numbers divisible by 6 but not 12 are:")

# For Loop in which is nested if statements. 
# For loop runs for values in range between 1000 and 10000
for i in range (1000,10000):
    # If the first statement (number is divisible by 6 without the reminder)is true,
    # code moves to second condition
    # If is false, code check next value from range until the statement is true
    if i % 6 == 0:
        # If the first statement (number is divisible by 12 without the reminder)is
        # true code moves to statement continue, which returns the control to for 
        # loop for next value in range
        # if false, code moves to else statement
        if i % 12==0:
            continue  
        # prints the numbers divisible by 6 only 
        else:              
            print(i, end=" ")
