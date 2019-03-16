from datetime import datetime

now = datetime.today()

day = now.strftime("%d")


def formating(day):
    if day == "1" or day == "21" or day == "31":
        return "st"
    elif day=="2" or day == "22":
        return "nd"
    elif day == "3":
        return "rd"
    else:
        return "th"


print(now.strftime("%A, %B %d{} %Y at %I:%M %p".format(
    formating(day))))