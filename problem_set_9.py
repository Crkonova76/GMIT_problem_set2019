# # Martina Crkonova, 2019-03-18
# Problem Set 2019, Python second, Programming and Scripting, GMIT
# Program which outputs every second line form text file


# variable which indicates which line to start with
lines = 5

# Open file function opens MobyDick text file, stored in the project directory in read format
with open('MobyDick.txt', 'r') as f:

    # Assign a local variable to function f.readlines (returns a list containing the lines)
    my_data = f.readlines()

    # For loop to go through each text row in my_data variable 
    for line in my_data:
        # Increase number of lines by one
        lines += 1
        #if the reminder of lines equal zero, condition is true, the text in the row will be printed
        if lines %2 == 0:
            print(line)