# qos: 
# a) remove duplicates

# approach(1): using set() datastructure, that automatically returns non-duplicate characters. 
def remove_duplicates_using_set(string):
    return "".join(set(string))
print(remove_duplicates_using_set("hello"))

# approach(2): using 2-pointer approach
def remove_duplicates_using_2Pointer(string):
    char_list=list(string)
    i,j=0,1 #inializing pointers at the first 2 indexes
    while j<len(char_list): 
        if char_list[i]!=char_list[j]:  
            i+=1   #moving the first pointer by 1-place
            char_list[i]=char_list[j]  #placing the unique char at the correct place
        else: 
            j+=1
    return "".join(char_list[:i+1])
print(remove_duplicates_using_2Pointer("hello"))



# b) count vowels 

# approach(1): I am taking a new_string and storing vowels inside that, after that I'll check if new_string is present in orginal_string, then return true else false 

def vowel_finder(string):
    vowels="aeiouAEIOU"
    vowel_list=[]
    for char in string: 
        if char in vowels: 
            vowel_list.append(char)
    return vowel_list 
print(vowel_finder("hello"))

# approach(2): using a list comprehension 
def vowel_finder_using_lc(string):
    vowels="aeiouAEIOU"
    return [char for char in string if char in vowels]
print(vowel_finder_using_lc("Hello, World"))

# approach(3): using (in) with set() -> why set? because i don't want duplicacy of characters. 
def vowel_finder_using_set(string):
    vowels=set("aeiouAEIOU")
    return [char for char in string if char in vowels]
print(vowel_finder_using_set("How are you?"))
