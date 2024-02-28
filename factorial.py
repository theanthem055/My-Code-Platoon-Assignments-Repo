# create a method that takes an integer as an input

def factorial(num):
    total = 1
    if(num < 0):
        return "Factorial on negative numbers is not possible, please enter a positive number."
    for num in range(1, num+1):
        total *= num
    return total




print(factorial(0))
