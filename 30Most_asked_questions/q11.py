# Question: Check given number is prime or not. 

# Approach(1): Basic method of checking divisibility of all numbers getting divisible from 2 up to the number itself.
def primeNumber_checker(number): 
    if number<=1: return False 
    for i in range(2,number):
        if number%i==0: 
            return False 
    return True      
print(primeNumber_checker(5))

# Approach(2): using a python library:: isprime() 
