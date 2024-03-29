# qos: sum of digits in a number 

'''
Approach(1): using sum() pre-built function
- TC: O(n^2)
'''
def sum_naive(n):
    total=0
    for digit in str(n):
        total+=(int(digit))
    return total
print(sum_naive(52))

'''
Approach(2): using maths here. 
explantion: 
- I am using a modulo operator (%) to get the 'last digit of the number', 
- and integer division (//) to remove the last digit.

TC: (O(N))
'''
def sum_maths(n):
    total=0
    while n>0:
        total+=n%10 #it's giving me last digit of number.
        n//=10  # this line is removing the last digit. 
    return total
print(sum_maths(123))

'''
Approach(3): Recursive apporach
- It's entirely simillar to approach(2): it's just I am using recursion here. 

- TC: O(n)
'''
def sum_recursive(n):
    if n==0: 
        return 0
    else: 
        return n%10 + sum_recursive(n//10)
print(sum_recursive(123))

print('=========')
# Follow-UP question on this simillar pattern. 

#===========================================

# Follow-Up(1): Count the number of digits. 

# Approach(1) -> Typecasting
number = 12345
print(len(str(number)))

# Approach(2) -> iterating and using a counter. 

#===========================================

# Follow-Up (2): Find the product of digits. 

# A(1): typecast and find prod
def product_number(n):
    prod=1
    for digit in str(n):
        prod*=int(digit)
    return prod
print(product_number(1234))

#===========================================

# Follow-Up(3): Reverse a number / digit 
# e.g -> input =123 || output = 321

# A(1): using simple maths 
def reverse_maths_number(n):
    rem=0
    while n>0:
        rem=rem*10 + n%10
        n=n//10
    return rem
print(reverse_maths_number(1234))

# A(2) : typecast -> slicing operator
def reverse_slicing(n):
    str_n=str(n)
    return str_n[::-1]
print(reverse_slicing(12345))

#===========================================

