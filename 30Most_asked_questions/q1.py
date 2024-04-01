# Swapping (2) numbers. 

# Approach(1):- Using a 3rd variable 
def swap_a1(a,b):
    temp=a
    a=b
    b=temp
    return a,b
print(swap_a1(5,4))

# Approach(2):- Without using a 3rd variable :- using math operators. 
def swap_math(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
print(swap_math(4,5))

# Approach(3):- using python method
def swap_slicing(a,b):
    a,b=b,a
    return a,b
print(swap_slicing(6,7))

# Approach(4):- using bitwise operator.
def swap_bitwise(a,b):
    a=a^b
    b=b^a
    a=a^b
    return a,b
print(swap_bitwise(10,11))