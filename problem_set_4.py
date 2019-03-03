# Martina Crkonova, 2019-03-01
# Problem Set 4 2019, Python collatz, Programming and Scripting, GMIT



i = int ( input (" Please enter a positive integer: "))

collection = []

if i < 0:
    print (" Entered integer ", i ," is negative number . Input a positive integer next time.")
    
initial =i

while i > 1:
    
    if i % 2 == 0:
        i = i// 2 
        collection.append(i)
    
    elif i % 2 == 1:
        i = i * 3 + 1
        collection.append(i)
print ("An initial positive integer is {} and the output is: {}" .format(initial,collection))


