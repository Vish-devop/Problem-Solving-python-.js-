# question: Count number of digits in a number. 

# appproach(1): converting into string, and then using len() function to count.
def countdigits_a1(number):
    stringNumber=str(number)
    return len(stringNumber)
print(countdigits_a1(121))

# approach(2): using a while loop
def countdigits_a2(number):
    count=0
    while number>0:
        number//=10
        count+=1
    return count 
print(countdigits_a2(124))