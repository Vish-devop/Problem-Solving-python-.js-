# Qos: Print the occurances of each character in a string. 

'''
Approach(1): using a dictionary with get()
Explanation(): 
- I am using a dictionary, that will count the characters of a string.
TC: O(n)
'''
def occurances(string):
    seen={}
    for char in string: 
        seen[char]=seen.get(char,0)+1
    return seen
print(occurances("Hello world"))

# But let's say I want the output in this format: H1e1l3o2 1w2r1d1  >> meaning, after key I am mentioning how many times they are getting repeated. 

def print_occurences_differntFormat(string):
    seen={}
    for char in string: 
        seen[char]=seen.get(char,0)+1
    output =""
    for key,value in seen.items():
        output+=key+str(value)
    return output
print(print_occurences_differntFormat("Hello World"))

# Approach(2): this is simillar to above approach -> just a difference is that here I am not using get() method. 

def print_char(string):
    seen = {}
    for char in string: 
        if char not in seen: 
            seen[char]=1 # I am appending the key.
        else:
            seen[char]+=1 # I am incrementing the count of that key.
    
    for key,value in seen.items():
        print(f"{key}:{value}")
print_char("hello world")

# Approach(3): Using a brute-force approach. 

'''
TC: O(n^2)
simple explanation: I just checking each character against every other character present in the string.
'''
def occurences_naive(string):
    for char in string:
        print(f"{char}:{string.count(char)}")
print(occurences_naive("Hello world"))


# Qos: Print only the words in a string sentence ingore the whitespace, comma, and other punctuation. 

# Approach(1): I am creating an extra array, and storing all the symbols that I don't have to print and then, I'm iterating inside the string, and appending the elements that are not present into the extra array; at-end returning the output_string. 

# TC: O(N+M)
def string_without_others(string):
    extra = [" ",",","!","@","#","$",'%','^','&','*','(',')','-','+','{','}',"[","]",";",":","'",'"',"<",",",">",".","/","?",'|']
    output=""
    for char in string: 
        if char not in extra:
            output+=char
        else: 
            continue
    return output
print(string_without_others("Hello World, How are you? Are you working fine?"))