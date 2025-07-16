#Write a function to add two numbers.
def fun(a,b):
    return a+b
result=fun(3,6)
print(result)

#Write a function that returns the square of a number
def square(a):
    return a*a
results=square(4)
print(results)

#Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, so not prime

    return True  # No divisors found, it is prime


# Test the function
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, so not prime

    return True  # No divisors found, it is prime


# Test the function
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
