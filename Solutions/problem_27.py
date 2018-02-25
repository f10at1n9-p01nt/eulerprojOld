from numpy.polynomial.polynomial import polyval

def check_prime(num):
    '''Returns True if num is prime and False if composite.'''
    for factor in range(2, int(num**(1/2))+1):
        if num % factor == 0:
            return False
    return True


def generate_primes(num):
    '''Returns a list of all primes from 1 to num.'''
    primes = []
    for i in range(1, num+1):
        if check_prime(i):
            primes.append(i)
    return primes


def quadratics(b_list):
    '''docstring'''

print(generate_primes(1000))
# 3 * 5**2 + 2 * 5 + 1
print(polyval(5,[1,2,3]))
