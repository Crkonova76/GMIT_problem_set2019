#Martina Crkonova, 2019-02-28
#Problem Set 2019, Programming and Scripting, GMIT
#Program that outputs whether or not today is a day that begins with the letter T

# import datetime library
import datetime

# datetime.datetime.today().weekday() function returns integer
# My if statement with using datetime function as condition
# if statement to recognize if days are 1 or 3
# 
if datetime.datetime.today().weekday() == 3 or datetime. \
        datetime.today().weekday() == 1:
    # If condition is true the message in this section will be printed
    print("Yes-today begins with T.")
else:
    # If condition about is not true the message in else condition will
    # be printed
    print("No-Today does not begin with a T.")