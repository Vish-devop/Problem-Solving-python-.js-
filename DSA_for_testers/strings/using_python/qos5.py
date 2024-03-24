# qos-> 
# a) reverse a string 

# approach(1): using slicing operator
def reverse_a_string(string): 
    return string[::-1]
print(reverse_a_string("hello"))

# approach(2): without using slicing opeator -> in that case, using for loop
def reverse_using_loop(string):
    reversed_string=""
    # iterating the string from back
    for i in range(len(string)-1,-1,-1):  #starts at len(string)-1, go down to 0.
        reversed_string+=string[i]
    return reversed_string
print(reverse_using_loop("hello"))

# b) check for palindrome
#  palindrome means, the reversed_string == normal string -> e.g. : aba

# approach(): creating a variable: reversed_string and comparing that with the normal string. 
def palindrome_checker(string):
    reversed_string=string[::-1]
    return reversed_string==string
print(palindrome_checker("hello")) #return false 
print(palindrome_checker("aba")) #returns true