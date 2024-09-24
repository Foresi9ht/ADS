def is_prime(a):
    if a <= 1:
        return "NO"
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return "NO"
    return "YES"

a = int(input())
print(is_prime(a))
