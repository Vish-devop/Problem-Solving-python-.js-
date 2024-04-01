# question: Find the factorial of a number. 

# approach(1): using a recursion. 
def factorial(number):
    if number<=1:
        return 1 
    else: 
        return number*factorial(number-1)
print(factorial(3))

# approach(2): Iterative approach
def fact_iterative(number):
    result=1
    for i in range(2,number+1):
        result*=i
    return result 
print(fact_iterative(3))

# approach(3): using python pre-built module: math.factorial()
import math 
def fact_method(number):
    return math.factorial(number)
print(fact_method(3))