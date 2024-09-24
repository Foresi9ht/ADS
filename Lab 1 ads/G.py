def nth_prime(n):
    primes = []
    is_prime = [True] * (n * 100)
    for p in range(2, len(is_prime)):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, len(is_prime), p):
                is_prime[multiple] = False
    return primes

def nth_superprime(n):
    primes = nth_prime(1000)
    superprimes = [primes[i - 1] for i in primes]
    return superprimes[n - 1]

n = int(input())
print(nth_superprime(n))
