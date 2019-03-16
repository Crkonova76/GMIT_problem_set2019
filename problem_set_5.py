# Martina Crkonova, 2019-03-07
# Problem Set 5 2019, Python Primes, Programming and Scripting, GMIT
#Program check whether or not the input is prime number 

"""
Prime number definition, source: https://en.wikipedia.org/wiki/Prime_number
A prime number (or a prime) is a natural number greater than 1 that cannot
be formed by multiplying two smaller natural numbers.A natural number greater
than 1 that is not prime is called a composite number.

"""
# Variable a is created to which is assigned a positive integer,provided as
# user input 
a = int (input ("Input positive integer: "))

# For loop checks for i in range from 2 to a less 1 integer
for i in range (2,a-1):
    # a equal 1, print value of a is not a Prime Number
    if a == 1:
        print(a," is not a Prime Number")
    # a equal 2, print value of a is a Prime Number
    elif a == 2:
        print(a, " is a Prime Number")
    # if reminder of a divisible by i is Zero (so is whole number),
    # print value of a is not a Prime Number
    elif a % i==0:
        print(a, "is not a Prime Number")
        #if above condition is true, stop checking 
        break
#If any of above conditions is fulfiled,print value of a is not a Prime Number 
else:
    print(a, " is a Prime Number")

