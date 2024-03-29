#qos -> 

# a) capitalize first letter of each word

# approach(1): using pre-built method -> .title() || this method makes the first character of the string capital.

def capitialize_first_letter_string(string):
    return string.title()
print(capitialize_first_letter_string("Hello World"))

# approach(2): using a loop.
def capitialize(string):
    result=""
    is_first_word=True
    for char in string: 
        if char.isspace():
            is_first_word=True  
        elif is_first_word:
            result+=char.upper()
            is_first_word=False 
        else: 
            result+=char
    return result 
print(capitialize("hello,world! how are you?"))



# b) Write a function to convert a string to Pig Latin (simplified version: move the first consonant cluster to the end of the word and add "ay"). (e.g., "hello" becomes "ellohay")
