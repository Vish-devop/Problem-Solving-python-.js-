# question: applying the linear search 

# Linear search is like I am having a single pointer and I would be iterating inside the array until I find the target element. 

def linearSearch(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return f"The element is present at this index: {i}"
print(linearSearch([1,2,3,4,5],4))

