# Qos: Check a given number is palindrom or not. 

# Approach(1): just reverse a number and check original nubmer is equal to reversed or not. 
def palindrome_a1(number):
    original_number=number
    reversed_number=0
    while number>0:
        digit = number%10
        reversed_number=reversed_number*10+digit 
        number//=10
    
    return reversed_number==original_number 
print(palindrome_a1(1211))

# Approach(2): Converting to string and using slicing operator
def palindrome_a2(number):
    stringNumber=str(number) 
    return stringNumber==stringNumber[::-1]
print(palindrome_a2(121))