# Martina Crkonova, 2019-03-09
# Problem Set 6 2019, Python secondstring, Programming and Scripting, GMIT
# Program which ommit every second word from user input string



# Ask for input and displaye it on new line
my_input = input ('Please enter a sentence :\n')

# Split the input on the base of empty spaces between words
my_splited_input = my_input.split()

# From List my_splited_input select each second word [start,stop, step]  
conv = my_splited_input[::2]

# Print each value from variable conv in one line with empty space between values
for i in conv:
    print(i, end=" ")
