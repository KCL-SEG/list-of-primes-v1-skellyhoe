"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    i = 0

    while i < number_of_primes:
        prime = True
        for j in range(2, num):
            if num % j == 0:
                prime = False

        if prime:
            list.append(num)
            i = i + 1

        num = num + 1
    return list
