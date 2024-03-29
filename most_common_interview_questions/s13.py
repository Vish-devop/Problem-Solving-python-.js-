# Qos: print the longest substring without repeating characters. 

# Before solving this qos, let's solve this first:- Print all the substrings present into a string.

'''
Using this approach -> Three Nested loops: 
- the outer loop picks a starting character,
- mid-loop considers all the characters on the right of the picked character as the ending character of the subtring. 
- The innermost loop prints characters from the currently picked started point to hte picked ending point. 
TC: O(n^3)
'''
def allSubstring(string):
    
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            for k in range(i,j):
                print(string[k], end=" ")
            print()
            
(allSubstring("abcd"))
print("-----------------------------------")

# Next sub-qos: Print all the non-repeated substrings from a string. 
'''
Here, I am using Approach -> 
- Using substr() function. 
- It will be running 2 loops, the outer loop picks a starting character.
- And, inner loop generates all the substrings starting from the character picked by the outer loop.

- TC: O(n^2)
'''
def nonRepeatingChar(string):
    size=len(string)
    substring=set()
    for i in range(size):
        for j in range(i+1,size+1):
            substr=string[i:j]
            if substr not in substring:
                substring.add(substr)
    return substring
print(nonRepeatingChar("abcdab"))
print("-----------------------------------")
# Next sub-qos: Pring all the repeated substrings from a string. 
'''
This is also simillar to above one only.
TC: O(n^2) 
'''
def repeatingChar(string):
    substring=set()
    repeatingString=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substr=string[i:j]
            if substr not in substring:
                substring.add(substr)
            else: 
                repeatingString.append(substr) 
    return repeatingString
print(repeatingChar("abcda"))
# Next main-qos: print the longest subtsring without repeating characters. 

'''
Approach(1): using a 2-Nested loops.
TC: O(n^2)
'''
def longestSubstring(string):
    longestSubString=""
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substr=string[i:j]
            if len(substr)>len(longestSubString):
                longestSubString=substr
    return longestSubString
print(longestSubstring("abcda"))

'''
Optmized solution:
- Taking 2 pointers: left,right at the ends of the current substring.
- Also taking a set() that will keep track of char in current substring.
- Now, if current char is not in set() then I will add otherwise will continue.
- So, the maximum length of non-repeated substring will be found when a longest character is captured. 

TC: O(n)
'''
def longestSubString_sliding(string):
    left,right=0,0
    maxLength=0
    start=0
    charSet=set()
    while right<len(string):
        if string[right] not in charSet:
            charSet.add(string[right])
            right+=1
            # condition for longest
            if maxLength < right-left:
                maxLength=right-left
                start = left
            else: 
                charSet.remove(string[left])
                left+=1
    return string[start:start+maxLength]
print(longestSubString_sliding("abcabcbb"))



# next main-qos: print both smallest substring without repeating characters. 