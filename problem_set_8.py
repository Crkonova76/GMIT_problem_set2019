# Martina Crkonova, 2019
# Problem Set 2019, Python formated datetime, Programming and Scripting, GMIT


# Import a module named datetime
from datetime import datetime

# Create variable now which import the current date in format year-month-day time hrs:min:sec
now = datetime.today()

# Variable day which by strftime() method convert variable now into string
# This will enable us to use string day output into function formating (day)
day = now.strftime("%d")

# Function formating (day) is used to determinate ordinal indicator
# This is used in print statement
# If statement used to identify and allocate the ordinal indicator to the string day 
def formating(day):
    if day == "1" or day == "21" or day == "31":
        return "st"
    elif day=="2" or day == "22":
        return "nd"
    elif day == "3":
        return "rd"
    else:
        return "th"

# Print the output in designated format
print(now.strftime("%A, %B %d{} %Y at %I:%M %p".format(
    formating(day))))