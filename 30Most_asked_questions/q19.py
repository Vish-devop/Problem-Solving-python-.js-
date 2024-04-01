# question: Find the duplicate elements in an array. 

# approach(1): typecasting the array into the set and then substring array from the set. 
def duplicate_finder(array):
    seen=set()
    for char in array: 
        if char in seen: 
            return char 
        seen.add(char)
    return -1
print(duplicate_finder([1,2,3,3,2,5]))

# approach(2): using 2-pointer approach
def duplicate_finder_2P(array):
    left=0
    for i in range(1,len(array)):
        if array[i]==array[left]:
            return array[left]
        else: left+=1
print(duplicate_finder([1,2,2,3,3,2,5]))

# approach(3): using hashmap; condition I'm applying that keys having values greater than 1 are duplicate.
def duplicate_finder_hashmap(array):
    seen={}
    for digit in array:
        seen[digit]=seen.get(digit,0)+1
    
    for key,value in seen.items():
        if value>=2:
            return key
print(duplicate_finder_hashmap([1,2,3,3,4,4,5]))