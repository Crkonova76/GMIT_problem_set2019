# Martina Crkonova, 2019-02-28
# Problem Set 2019, Python divisors, Programming and Scripting, GMIT
# Program printing all numbers from range 1,000 and 10,000 that are divisible by 6 but not 12

# The For loop, variable i is assigned the range of numbers between 1000 and 10000

"""
1, Print function used to show the description of the output
2, I used For loop, in which I assigned to variable i the range of numbers between 1000 and 10000
3, I decided to use nested if condition, when If the first statement (number is divisible by 6 without the reminder)is:
         true - code moves to second condition 
         false - code check next value from range until the statement is true
4, If second condition (number is divisible by 12 without the reminder)is: 
        true - code moves to statement continue, which returns the control to for loop for next value in range
        false - code moves to else statement
5, Else statement prints the numbers divisible by 6 only
"""


print("Numbers divisible by 6 but not 12 are:")

for i in range (1000,10000):
    if i % 6 == 0:
        if i % 12==0:
            continue  
        else:              
            print(i, end=" ")
