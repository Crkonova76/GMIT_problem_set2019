# # Martina Crkonova, 2019-03-02
# Problem Set 2019, Python sumupto, Programming and Scripting, GMIT
# Program calculating sum of all numbers between given number and one

"""
For solving of this problem I used two different algorithms.
Variable i is by using input function asking for the positive integer. 
In both cases while loop was used.

1,  Variable Total was assigned Zero. The condition in while loop is checking until i is higher than 0. 
    Once the i is equal or lower than 0, then the variable total will be printed. 
    Inside the loop i is reduced by one each cycle and added to total. 

2,  I used two variables-total and result, both set up as Zero. The condition for terminating the loop is when total is lower than i.
     Once the total is higher than i, then the variable result will be printed. 
     Inside the while loop is total is increased by 1 each cycle and then tthis total is added to result.

"""


#VERSION 1

#Created variable i which is asking to input positive integer
i = int(input ( "Enter the positive integer: "))

# To variable total is assigned value Zero. 
# Zero selected as the input number would be the starting integer in computation in below 
# while loop
total = 0

#While loop set up, running until condition i>0 is fulfilled
#when i>0, to total is added i and i is decreased by 1.
#The condition is checked again
#when i=or is < 0, while loop is completed, the total will be printed
while i > 0:
    total = total + i
    i = i - 1

print("The output of Version 1 is {}".format(total))



#VERSION 2

#Created variable i which is asking to input positive integer
i = int(input ( "Enter the positive integer: "))

# Variables total and result are created with assigned value Zero
total = 0
result = 0

# While loop set up, running until condition is fulfilled (total <i)
# If the condition is not met, the program increse total by 1.
# Variables total and result are added
# When total equals or is bigger than i, while loop is completed.
# Result will be printed

while total < i:
    total = total + 1
    result = total + result
    
      
print("The output of Version 2 is {}".format(result))
