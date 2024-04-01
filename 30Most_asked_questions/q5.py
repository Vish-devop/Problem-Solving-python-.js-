# Question: Check whether a given string is a palindrome or not. 

'''
NOTE: here, the different kind of apporaches will only depend on how differently I am reversing a string.
So, for that, please head to q3 to see different kind of approaches to reverse a string. 
Here, I am just showing a  single method. 
'''
def palindromeString(string):
    return string==string[::-1]
print(palindromeString("olo"))