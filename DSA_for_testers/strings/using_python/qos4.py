# qos: return the concatenation of two strings. 

# approach1 -> using (+) operator.
def concatenate(s1,s2):
    return s1+s2
print(concatenate("hello","world"))

# approach2 -> using loop
def add_strings(s1,s2):
    new_string=""
    for i in s1: 
        new_string+=i
    for j in s2: 
        new_string+=j
    return new_string
print(add_strings("Hello","word"))



# another qos: conver the string into UpperCase and then into LowerCase() 

# approach(1): using the pre-built function. 
def uppercase_lowercase_string(string):
    upper_string=string.upper()
    lower_string=string.lower()

    return upper_string,lower_string
print(uppercase_lowercase_string("hellO"))


    