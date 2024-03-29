# Qos: Remove duplicate element from an array. 

'''
A1: using 2-pointers. 
explanation: 
<> as, 2pointer approach is good in sorted arrays, so I am first sorting the array. 
1-pointer will be placed at 0th index of an array, and 
2nd pointer is placed at last index of an array. 
If both are same, I'll move my 1st pointer, but if they are not same, i'll move my right pointer.

TC: O(n log n)
'''
def remove_duplicate(array):
    # base case: 
    if len(array)==0:
        return array
    
    # sorting out the array
    array.sort()
    i=0

    # using 2-pointers for finding
    for j in range(1,len(array)):
        if array[j]!=array[i]:
            i+=1
            array[i]=array[j]

    return array[:i+1]
print(remove_duplicate([1,1,2,3]))

# A(2): converting the array in set() : as set() do not contain any duplicates. 

array=[1,2,3,1]
print(set(array))

# A(3): Using a hashmap
'''
explanation: 
- in the a(1), where I am using a 2-pointer approach, I'm first sorting out the array.
- But, let's say the condition is that we aren't allowed to sort the array. 
- There, how we will do ?

- So, here we will using a hashmap, and placing all the elements that are seen into hasmamp, then removing the elements having the frequency>1.

TC: O(n)
'''
def remove_duplicate_hasmap(array):
    seen=set()
    output = []
    for num in array: 
        if num not in seen: 
            output.append(num)
            seen.add(num)
    return output
print(remove_duplicate_hasmap([1,2,3,1]))
