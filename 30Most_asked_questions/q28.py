# question: Reverse each word present inside a string. 

'''
A simple approach(): 
-> First convert the string into list of string using .split() method. 
-> now, iterate inside the list_of_string, and just reverse the character present into the string. 

TC: O(n) and SC: O(n)
'''
def reverseWord(string):
    words=string.split(' ')
    reversedWord=[word[::-1] for word in words]
    return ' '.join(reversedWord)
print(reverseWord("Hello how are you? "))