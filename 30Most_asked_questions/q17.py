# question: Find the misssing number in an array. 

# CASE 1: 
# Taking  the condition that array is sorted.
def missingNumber_finder(array):
    left=0
    right=1
    while right<len(array):
        if array[right]-array[left]!=1:
            return array[left]+1
        else: 
            left+=1
            right+=1
print(missingNumber_finder([1,2,4,5]))

# CASE2: 
# Condition is that array is not sorted. 
def missingNumber_finder(array):
    # in case of unsorted array, it becomes bit hard to find missing number, so it's better to sort the array first : but this will increase the time complexity of the array. 
    sortedArray=sorted(array)
    left=0
    right=1
    while right<len(sortedArray):
        if sortedArray[right]-sortedArray[left]!=1:
            return sortedArray[left]+1
        else:
            left+=1
            right+=1
print(missingNumber_finder([1,3,6,2,4]))