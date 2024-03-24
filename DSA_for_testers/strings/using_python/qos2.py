# qos(2): 
# a) Access all the indivisual characters within a string.
# b) Find the substring from a string. 


# approach(1): this will print all the characters present into the string. 
# string = "Hello"
# for i in range(len(string)):
#     print(string[i])    


# Finding the substring from a string. 
'''
substring means -> 
e.g. -> string = Hello
possible substring for this string would be: 
[h],[he],[hel],[hell],[hello], 
[e],[el],[ell],[ello]
[l],[ll],[llo]
[l],[lo]
[o]

simillarly, from back to starting of string.
'''
# approach(1): using the slicing operator. 
def finding_substring(string): 
    substrings=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substrings.append(string[i:j])
    return substrings
print(finding_substring("hello"))

# approach(2): without using a slicing operator.
def finding_substrings(string):
    substrings=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            new_substring=""
            for k in range(i,j):
                new_substring+=string[k]
            substrings.append(new_substring)
    return substrings
print(finding_substrings("hello"))
# This will run in -> TC: O(n^3) || SC: O(n)

# approach(3): optmized approach => here, I am using a set() : this will help me in avoiding duplicates.
def substrings(string):
    substrings=set()
    for i in range(len(string)):
        substring=""
        for j in range(i,len(string)):
            substring+=string[j]
            substrings.add(substring)
        # Optmization: if the remaining string only has 1 character
        if len(string)-i-1<=0: break
    return list(substrings)
print(substrings("hello"))
            
    