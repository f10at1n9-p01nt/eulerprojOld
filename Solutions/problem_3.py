# Project Euler #3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

import math

def factors(number):
    '''Returns a sorted list of all the factors of number.'''
    factors = []
    for num in range (1, int(math.sqrt(number))+1):
        if number % num == 0:
            factors.append(num)
            factors.append(number/num)
    list.sort(factors)
    return factors


def test_prime(list):
    '''Deletes all non-prime factors in a list.'''
    pos = 0
    while pos < len(list):
        root = int(math.sqrt(list[pos]))
        for num in range(2, root + 1):
            if list[pos] % num == 0:
                list.remove(list[pos])
                pos -= 1
                break
        pos += 1
    return list


print(test_prime(factors(600851475143)))
