# question: Print even and odd numbers from an array. 

# approach(1): iterating through the array, and taking (2) extra arrays that will store the even and odd elements present into an array.

def even_odd_array_elements(array):
    even,odd=[],[]
    for i in range(len(array)):
        if array[i]%2==0: 
            even.append(array[i])
        else: 
            odd.append(array[i])
    return even,odd
print(even_odd_array_elements([1,2,3,4]))
