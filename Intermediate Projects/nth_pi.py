import math

'''This project prompts the user to enter a number and prints
    pi to with the input amount of decimal places.
    This program is only as accurate as the input of pi. '''


def betterPi():
    #impliment method to calculate higher precision pi
    pass

pi = math.pi
n = str(input("Enter your desired number of decimal places: "))
f ="." + str(n) + "f"

print(format(math.pi, f))