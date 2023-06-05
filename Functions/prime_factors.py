from prime import is_prime

n = int(input())


def is_prime_factors(x):
    for i in range(1, x + 1):
        if x % i == 0 and is_prime(i):
            print(i, end=" ")


is_prime_factors(n)