def nth_prime(n):
    primes = []
    is_prime = [True] * (n * 100)
    for p in range(2, len(is_prime)):
        if is_prime[p]:
            primes.append(p)
            if len(primes) == n:
                return p
            for multiple in range(p * p, len(is_prime), p):
                is_prime[multiple] = False

n = int(input())
print(nth_prime(n))
