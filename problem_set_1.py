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

#i = int(input ( "Enter the positive integer: "))

# total = 0

# while i > 0:
#     total = total + i
#     i = i - 1

# print(total)



#VERSION 2

i = int(input ( "Enter the positive integer: "))

total = 0
result = 0

while total < i:

    total = total + 1
    result = total + result
    
      
print(result)
