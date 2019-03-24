
# import math
#
# inp=input("Please provide any POSITIVE floating point number: ")
#
# result = math.sqrt(float(inp))
#
# print("The square root of {} is approx.{},".format(inp,result))


inp=input("Please provide any POSITIVE floating point number: ")

def babylonianalgorithm(data):
    if(data == 0):
        return 0

    g = data/2.0
    g2 = g + 1
    while(g != g2):
        n = data/ g
        g2 = g
        g = (g + n)/2

    return g

mata = BabylonianAlgorithm(float(inp))

print("The square root of {} is approx.{},".format(inp,mata))

