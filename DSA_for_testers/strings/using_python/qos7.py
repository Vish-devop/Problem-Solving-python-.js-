# questions: 
# a) Print most frequent character with how many time they got repeated inside the string. 

# approach(1): using dictionary
def frequent_character(string):
    seen={}
    # storing the characters of string into dictionary
    for char in string: 
        seen[char]=seen.get(char,0)+1
    # finding the most frequent char 
    max_value=0
    max_char=""
    for key,value in seen.items():
        if max_value<value:
            max_value=value
            max_char=key
    return max_char,max_value
print(frequent_character("hello"))

# approach(2)-> using a pre-built function that's simillar to dictionary -> counter. 
from collections import Counter 
def frequent_element_using_counter(string):
    char_count=Counter(string)
    most_freq_char=char_count.most_common(1)[0][0] #getting first element with most_common list
    most_freq_value=char_count.most_common(1)[0][1]
    return most_freq_char,most_freq_value
print(frequent_element_using_counter("How are you?"))

# approach(3): using list and sorting -> but this is very-less efficient. 

# b) find first non-repeating character
# first-non repeating character in simple terms means -> first character in string which is having 1 value. 

# approach()-> for this i am using dictionary. 
def first_non_repeating_char(string):
    seen={}
    for char in string:
        seen[char]=seen.get(char,0)+1

    for key,value in seen.items():
        if value==1:
            return key 
            break
print(first_non_repeating_char("hello"))
