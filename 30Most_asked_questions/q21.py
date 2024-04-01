# Question: Sort the elements in an array using bubble sort. 

'''
Algorithm of Bubble sort: 
1. Start with the first element in the array.
2. Compare the current element with the next element. 
3. If the current element is greater than the next element, swap them. 
4. Move to the next element and repeat the steps 2-3 until the end of the array is reached.
5. Go back to the start of the array and repeat steps 2-4 until no swaps are needed, which indicates that the array is sorted. 

TC: O(n^2) 
'''
def bubble_sort(array):
    for i in range(len(array)):
        swapped = False 
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swapped=True
        if not swapped: 
            break
    return array
print(bubble_sort([1,2,5,3,2,1]))