# question: Find sum of digits in a number

# approach(1): using simple while loop
def findSum_a1(number):
    summ=0
    while number>0:
        summ+=number%10
        number//=10
    return summ
print(findSum_a1(121))

