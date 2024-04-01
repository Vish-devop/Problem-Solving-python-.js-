# Approach(1): using while loop

def reverse_a1(number):
    reversed_num=0
    while number>0:
        digit=number%10
        reversed_num=reversed_num*10+digit
        number//=10
    return reversed_num
print(reverse_a1(125))

# Approach(2): using string slicing 
def reverse_a2(number):
    return int(str(number)[::-1])
print(reverse_a2(125))

# Approach(3): using recursion
def reverse_recursion(number):
    if number<10:
        return number
    else: 
        return int(str(number%10) + str(reverse_recursion(number//10)))
print(reverse_recursion(125))

# Approach(4): using a stack 
def reverse_stack(number):
    stack=list(str(number))
    stack.reverse()
    return int(''.join(stack))
print(reverse_stack(125))

# Approach(5): using math and loop
def reverse_math_loop(number):
    reversed_number=0
    for _ in str(number):
        digit = number%10
        reversed_number=reversed_number*10+digit
        number//=10
    return reversed_number
print(reverse_math_loop(125))