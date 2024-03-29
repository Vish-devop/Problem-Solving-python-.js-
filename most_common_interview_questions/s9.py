# Qos: Swap two integers using a temperory variable. 

'''
Approach(1): 
-> I am using a temp variable and interchanging the values of both the variables with temp varaible. 

-> TC: O(N)
'''
def swap_brute(a,b):
    temp=a
    a=b
    b=temp
    return (f"a:{a},b:{b}")
print(swap_brute(5,4))

# Qos: Swap two integers without using a 3rd variable. 

'''
Approach(1): using the normal python syntax of swapping using tuple unpacking. 

TC: O(1)
'''
def swap_normally(a,b):
    a,b=b,a
    return (f"a:{a},b:{b}")
print(swap_normally(10,8))

'''
Approach(2): using the (+) and (-) operator.

TC: O(1)
'''
def swap_plus(a,b):
    a=a+b
    b=a-b
    a=a-b
    return (f"a:{a},b:{b}")
print(swap_plus(12,13))

'''
Approach(3): Using bitwise XOR.

TC: O(1)
'''
def swap_usingXOR(a,b):
    a^=b
    b^=a
    a^=b
    return (f"a:{a},b:{b}")
print(swap_usingXOR(13,15))


# Ques: Swap 2 string using a temp variable. 

def swap_string(a,b):
    new=a
    a=b
    b=new
    return (a,b)
print(swap_string("hello", "hey"))