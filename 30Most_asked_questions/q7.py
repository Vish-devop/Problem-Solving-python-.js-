# question: Count number of even and odd digits in a number

#approach(1): using a while loop
def countEvenOdd_a1(number):
    evenCount,oddCount=0,0
    while number>0:
        number//=10
        if number%2==0:
            evenCount+=1
        else: 
            oddCount+=1
    return evenCount,oddCount
print(countEvenOdd_a1(124))

# approach(2): convering into string and then returning length of even and odd numbers 
def countEvenOdd_a2(number):
    evenCount,oddCount=0,0
    stringNumber=str(number)
    for digit in stringNumber:
        if int(digit)%2==0: 
            evenCount+=1
        else: 
            oddCount+=1
    return evenCount,oddCount
print(countEvenOdd_a2(124))