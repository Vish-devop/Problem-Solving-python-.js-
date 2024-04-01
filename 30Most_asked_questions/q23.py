# question: Remove junk of special characters from a string. 

'''
I'll be using a very simple appraoch here:
-> I'll store all the special characters in a list/array.
-> I'll iterate through the string, and if the characters inside string are not the special characters then, I would be adding those inside a new string, else continue. 

TC: O(n) and SC: O(n)
'''
def removing_specialCharacters(string):
    special_chars=special_characters = [
    '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/',
    ':', ';', '"', "'", '<', '>', ',', '.', '?'
                                       
                                       ]
    newString=""
    for char in string: 
        if char not in special_characters:
            newString+=char
        else: 
            continue 
    return newString
print(removing_specialCharacters("Hello! How are you? "))