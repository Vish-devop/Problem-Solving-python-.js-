# question: removing white spaces from the string. 

# Approach() is very simple here: while iterating inside the string, if I found a white space, I'll just skip that. 

def removingWhiteSpaces(string):
    newString=""
    for char in string:
        if char==" ":
            continue
        else: 
            newString+=char
    return newString
print(removingWhiteSpaces("Hello How are you"))