# question: Find the maximum and minimum values in an array. 

# approach(1): without using any prebuilt method. 
def min_max(array):
    min,max=array[0],0
    for i in range(1,len(array)):
        if array[i]>max: 
            max=array[i]
        else: 
            min=array[i]
    return max,min
print(min_max([1,2,3,4,5]))

# approach(2): using prebuilt method. 
def min_max(array):
    maxElement = max(array)
    minElement = min(array)
    return maxElement,minElement
print(min_max([1,2,3,4,5,6,7,8]))