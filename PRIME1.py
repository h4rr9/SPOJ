import itertools

primes = set()

def check_prime(n):
    for p in primes:
        if not n % p:
            return False
    return True

def prime_sieve():
    for n in itertools.count(2):
        if n > 10**9:
            break
        if check_prime(n):
            primes.add(n)
