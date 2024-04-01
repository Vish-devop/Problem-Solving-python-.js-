# quesion: print fibonacci series 

# approach(1): Iterative approach 
def fibo_iteative(number):
    a,b=0,1
    for _ in range(number):
        print(a,end=" ")
        a,b=b,a+b
    # print()
print(fibo_iteative(12))

# approach(2): recursive approach
def fibo_recusion(number):
    if number<=1: 
        return number
    else: 
        return fibo_recusion(number-1)+fibo_recusion(number-2)
for i in range(10):
    print(fibo_recusion(i), end=" ")