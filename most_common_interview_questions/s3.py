# Print prime numbers

'''
Approach(1): 
- Simple Brute-force approach 
-TC: O(n^2) ||
'''
def prime_brute(n):
    for num in range(2,n+1):  # I started with 2, because prime number start with 2. 
        if all(num%2!=0 for i in range(2,num)):
            print(num)
prime_brute(5)

'''
Approach(2): 
- Using an algorithm : Eratosthenes
- TC: O(nlog log n)
- Explanation: It will work by iterating and makring the multiple of primes as composite, starting from the first prime_number 2.
'''
def eratoshtenes(n):
    sieve=[True]*(n+1)
    prime=2
    while prime*prime <=n:
        if sieve[prime] == True: 
            for i in range(prime*prime, n+1,prime):
                sieve[i]=False
            prime+=1
        for prime in range(2,n+1):
            if sieve[prime]:
                print(prime)
eratoshtenes(5)
