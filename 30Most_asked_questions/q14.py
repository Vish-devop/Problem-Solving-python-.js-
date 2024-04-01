# question: Find the sum of elements in an array. 

# approach(1): iterating through the array and adding each element present into an array into a variables named as summ.
def sum_array(array):
    summ=0
    for i in array:
        summ+=i
    return summ
print(sum_array([1,2,3]))

# approach(2): directly using a sum method 
array=[1,2,3]
print(sum(array))