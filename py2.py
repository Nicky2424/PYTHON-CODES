def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def primes_till(n):
    return [i for i in range(2, n+1) if is_prime(i)]

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num): primes.append(num)
        num += 1
    return primes

N = int(input("Enter N: "))

print("\nA) Prime check:", "Prime" if is_prime(N) else "Not Prime")
print("B) Primes till N:", *primes_till(N))
print("C) First N primes:", *first_n_primes(N))

        print(num, end=" ")
        count += 1
    num += 1

