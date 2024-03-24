# qos(1): Finding the length of a string. 

#Approach(1): using pre-built function -> len() 
def find_length(string):
    return len(string)
print(find_length("hello"))  #output: 5

# Approach(2): without using len() -> so, I would be using a counter. 
def length_string(string): 
    count=0
    for i in range(len(string)):
        count+=1
    return count 
print(length_string("hello"))  #output: 5
'''
Explanation: 
- I declared a count varaible and initialized that to 0. 
- Then, within a for loop, starting from 0 to end of string, I am increasing that count by 1.
- And at last returing the string. 
'''