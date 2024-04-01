# question: Count the occurences of characters in a string. 

''' 
I'm using a very simple approach here; 
Approach() here is: 
-> I'll be using a hashmap that will typecast the string into key-value pairs.
-> From here, I'll just return the values of a string (values means occurences)

TC: O(n) and SC: O(n) 
'''
def occurencesCounter(string):
    seen={}
    for char in string: 
        seen[char]=seen.get(char,0)+1
    
    return f"{seen.keys()}:{seen.values()}"
print(occurencesCounter("hello"))
