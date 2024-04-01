# Question: Sort element in an array using built-in methods.

#  for this, python provides (2) methods: sort() and sorted() 

# The simple difference b/w these two is this: sort() modified the list in place, and sorted() returns a new sorted list. 

def sortList(array):
    s1=array.sort()
    s2=sorted(array)
    return s1,s2
print(sortList([1,2,3,2,4]))