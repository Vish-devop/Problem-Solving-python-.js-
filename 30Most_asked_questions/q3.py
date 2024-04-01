# Qos: Reverse a string 

# Approach(1): using slicing operator
def reverseStr_slicing(string):
    return string[::-1]
print(reverseStr_slicing("Hello"))

# Approach(2): using 2-pointers
def reverseStr_2Pointers(string):
    listString=list(string)
    left,right=0,len(string)-1
    while left<right:
        listString[left],listString[right]=listString[right],listString[left]
        left+=1
        right-=1
    return ''.join(listString)
print(reverseStr_2Pointers("hello"))

# Approach(3): using a stack 
def reverseStr_stack(string):
    stack=[]
    outputstring=""
    
    for char in string: 
        stack.append(char)
    for char in stack: 
        outputstring+=stack.pop() 
    return outputstring
print(reverseStr_stack("hello"))

# Approach(4): Using the reversed() function and join()
def reverseStr_reversed_join(string):
    return ''.join(reversed(string))
print(reverseStr_reversed_join("hello"))

# Approach(5): Using a for-loop
def reverseStr_forLoop(string):
    reversedString=""
    for char in string: 
        reversedString=char + reversedString
    return reversedString
print(reverseStr_forLoop("hello"))

# Approach(6): using a recursion
def reverseStr_usingRecursion(string):
    if len(string)==0:
        return string 
    else: 
        return reverseStr_usingRecursion(string[1:])+string[0]