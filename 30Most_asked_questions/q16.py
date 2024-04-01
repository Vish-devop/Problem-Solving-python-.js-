# question: Check the equality of two arrays. 

# Approach(1): Directly comparing  the two arrays. 

def equal_array(a1,a2):
    return a1==a2
print(equal_array([1,2,31],[1,2,3]))

# Approach(2): iterative approach 
def equalArray_iterative(a1,a2):
    # edge case
    if len(a1)!=len(a2): return False 
    for digit in range(len(a1)):
        if a1[digit]!=a2[digit]: 
            return False      
    return False 
print(equalArray_iterative([1,2,3],[1,2,3]))    
