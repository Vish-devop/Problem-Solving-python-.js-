# Qos(1): Reverse a string.
# e.g. -> string = Hello world  || output: sretset olleH
'''
Approach(1) - using slicing operator
TC: O(n) || SC: O(1)
'''
string="Hello testers"
print(string[::-1]) 

'''
Approach(2) - using 2 pointer approach
TC: O(n) || SC: O(n)
Short explanation: 
- I am using 1 pointer to track the start of the word, and second to find the end of the word. 
- Once I have teh start and end of a word, I am reversing that word. 
'''
def reverse_string(string):
    word = string.split(' ') #  ['Hello', 'world']
    for i in range(len(word)):
        word[i]=word[i][::-1] #here, reversing is completed. 
    return ' '.join(word[::-1])
print(reverse_string("Hello world"))


'''
A follow-up question here, 
input_string = hello testers 
output_string = testers hello  // here, you just have to swap the words present into a string. 
'''

#Approach(1): using slicing
def reverse(s):
    s=s.split(' ')
    s=s[::-1]
    return ' '.join(s)
print(reverse("Hello testers"))

# Using 2 pointers approach
def reverse_using_2Pointers(s):
    s=s.split(' ')
    left,right=0,len(s)-1
    while left<right: 
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return ' '.join(s)
print(reverse_using_2Pointers("Hello testers"))