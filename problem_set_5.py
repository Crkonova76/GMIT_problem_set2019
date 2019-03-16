a = int (input ("Input positive integer: "))


for i in range (2,a-1):
    if a == 1:
        print(a," is not a Prime Number")
    elif a == 2:
        print(a, " is a Prime Number")
    elif a % i==0:
        print(a, "is not a Prime Number")
        break

else:
    print(a, " is a Prime Number")

# a = int (input ("Input positive integer: "))

# if a > 1:
#     for i in range(2,a):
#         if a % i == 0:
#             print('it is not prime')
#
#             break
#     else:
#          print('its prime')
# else:
#     print('number is not prime')