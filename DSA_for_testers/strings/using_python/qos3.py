# qos: return True if a string is empty. 

# aprroach(1): if the length of the string = 0 ; means it's empty
def empty_string_checker(string):
    if len(string)==0: return True
    return False 
print(empty_string_checker(""))

# approach(2): using the in operator.
def empty_string(string):
    return " " in string
print(empty_string("Lolla"))