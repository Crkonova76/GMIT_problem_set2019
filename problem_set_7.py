# Martina Crkonova, 2019-03-24
# Problem Set 2019, Python square root, Programming and Scripting, GMIT
# Program which takes a positive floating point number as input and
# outputs an approximation of its square root

#VARIANT A (using library)

# Import math module from library
import math

# Requested input is allocated to variable inp
inp=input("Please provide any POSITIVE floating point number: ")

# math.sqrt(float(inp)) function returns the square root of input number
result = math.sqrt(float(inp))

# The result is printed
print("Variant A:The square root of {} is approx.{}.".format(inp,result))


#VARIANT B (Babylonian method, known as Heron's method)
# Adapted from: https://www.w3resource.com/python-exercises/math/python-math-exercise-18.php

# The basic idea if g is an overestimate to the square root of input number then input/g will 
# be an understimate (or vice versa). The average of these numbers may be expected
# to provide a better approximation of square root
# Refer to https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method 

# Requested input is allocated to variable inp
inp=input("Please provide any POSITIVE floating point number: ")

# The function babylonianalgorithm created
# Variable mata will assign the input number into function babylonianalgorithm
def babylonianalgorithm(data):
    # Return zero if input equals zero
    if(data == 0):
        return 0
    # Local variable assigned to the output of the operation data divided by 2
    g = data/2.0
    # Local variable g2 assigned to output of the operation g + 1
    g2 = g + 1
    # While loop to be true when g does not equal to g2
    while(g != g2):
        # Local variable is output of operation initial input divided by g
        n = data/ g
        # Reassign variable g2 which becomes g
        g2 = g
        # Varaible g calculates average of variables g and n
        g = (g + n)/2
    
    # Return output of the function babylonianalgorithm
    return g

# Local varaible mata assigned to output of function which parse input to type of float
mata = babylonianalgorithm(float(inp))

# Print function by using standard Python build in function .format which passing two parameters
print("Variant B: The square root of {} is approx.{}.".format(inp,mata))