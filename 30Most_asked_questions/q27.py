# question: count words in a string.

'''
Approach(): 
-> Just iterate inside an array.
-> Considering a counter variable that is assigned to 0.
-> while iterating inside the array, increase the value of counter.
-> return counter.

TC: O(n) | SC: O(1)
'''
def count_words(string):
    counter=0
    for char in string.split(" "): 
        counter+=1
    return counter 
print(count_words("Hello how are you? Hope you're doing great!"))