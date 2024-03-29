'''
Question: Fibonacci series
'''

# Approach(1): Recursive one 
# TC: O(2^n) - worst approach

def fibo(n):
    # base case
    if n<=1: 
        return n
    else: 
        return fibo(n-1)+fibo(n-2)
print(fibo(3))

# Approach(2): Dynamic Programming
'''
explanation: 
- I am storing the fibo numbers as I can use them later to avoid computation.
TC: O(n) || SC: O(n) 
'''
def fibo_dp(n):
    fib_values = [0,1] + [0]*(n-1)
    for i in range(2,n+1):
        fib_values[i]=fib_values[i-1]+fib_values[i-2]
    return fib_values[n]
print(fibo_dp(3))

# Approach(3): DP but space optmizied
'''
explanation: 
- This is same as above DP approach, it's just here I'm storing the last 2 fibonacci numbers, to reduce the space complexity. 

 SC: O(1)
'''
def fib_dp_space(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
print(fib_dp_space(3))