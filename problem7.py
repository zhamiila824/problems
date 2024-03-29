# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime(n):
    if type(n) != int:
        return 'Input must be Integer'
    elif n < 0:
        return 'Number must be positive'
    primes = 0
    n_prime = 1
    while primes < n:
        n_prime += 1
        if is_prime(n_prime):
            primes += 1
    return n_prime


print(prime(10001))
